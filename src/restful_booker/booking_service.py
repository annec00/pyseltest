from src.common.api_service import APIService


class AuthenticationError(Exception):
    """Raised when the Restful Booker API does not return an auth token."""


class BookingService(APIService):
    """Service class for interacting with the Restful Booker API."""

    def __init__(self, base_url: str):
        super().__init__(base_url)

    def authenticate(self, username: str, password: str) -> str:
        """Authenticate and obtain a token."""
        payload = {"username": username, "password": password}
        response = self.post("/auth", data=payload)
        # /auth returns HTTP 200 even for bad credentials (body: {"reason": ...}),
        # so the presence of a token is what actually signals success.
        token = response.json().get("token") if response.ok else None
        print("Authentication called... ")
        if not token:
            raise AuthenticationError(
                f"Authentication failed (HTTP {response.status_code}): {response.text}"
            )
        return token

    def get_bookings(self):
        """Get a list of all bookings."""
        return self.get("/booking")

    def get_booking_by_id(self, booking_id: int):
        """Get details of a specific booking by ID."""
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, booking_data: dict):
        """Create a new booking with the provided data."""
        return self.post("/booking", data=booking_data)

    def update_booking(self, booking_id: int, booking_data: dict, auth_token: str):
        """Update an existing booking with the provided data."""
        headers = {"Cookie": f"token={auth_token}"}
        return self.put(f"/booking/{booking_id}", data=booking_data, headers=headers)

    def delete_booking(self, booking_id: int, auth_token: str):
        """Delete a booking by ID."""
        headers = {"Cookie": f"token={auth_token}"}
        return self.delete(f"/booking/{booking_id}", headers=headers)
