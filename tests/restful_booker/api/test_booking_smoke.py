def test_get_bookings(booking_service, booking_id):
    response = booking_service.get_bookings()
    assert response.status_code == 200
    # Verify that the response contains a list of bookings
    assert isinstance(response.json(), list)
    booking_ids = [booking.get("bookingid") for booking in response.json()]
    # Verify that an item from the list has bookingid property
    assert any("bookingid" in booking for booking in response.json())
    print(f"GET Bookings: Found {len(booking_ids)} bookings")


def test_get_booking_by_id(booking_service, booking_id):
    response = booking_service.get_booking_by_id(booking_id)
    assert response.status_code == 200
    # Verify that the response contains the expected booking details
    assert response.json().get("firstname") == "PyTestAPI"
    assert response.json().get("lastname") == "AC"
    assert response.json().get("totalprice") == 100
    assert response.json().get("depositpaid") is True
    assert response.json().get("bookingdates") == {
        "checkin": "2023-01-01",
        "checkout": "2023-01-10",
    }
    assert response.json().get("additionalneeds") == "Breakfast"
    print(f"GET Booking ID {booking_id}: Found booking details.")


def test_create_booking(booking_service):

    payload = {
        "firstname": "Sophie",
        "lastname": "Cunningham",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-10"},
        "additionalneeds": "Breakfast",
    }
    response = booking_service.create_booking(payload)
    assert response.status_code == 200

    # Verify that the response contains the expected booking details
    assert response.json().get("booking").get("firstname") == "Sophie"
    assert response.json().get("booking").get("lastname") == "Cunningham"
    assert response.json().get("booking").get("totalprice") == 150
    assert response.json().get("booking").get("depositpaid") is True
    assert response.json().get("booking").get("bookingdates") == {
        "checkin": "2023-01-01",
        "checkout": "2023-01-10",
    }
    assert response.json().get("booking").get("additionalneeds") == "Breakfast"
    print(f"POST Booking: Created booking with ID {response.json().get('bookingid')}")


def test_update_booking(booking_service, booking_id, auth_token):
    payload = {
        "firstname": "Sophie",
        "lastname": "Cunningham",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-15"},
        "additionalneeds": "Lunch",
    }
    response = booking_service.update_booking(booking_id, payload, auth_token)
    assert response.status_code == 200

    # Verify that the response contains the updated booking details
    assert response.json().get("firstname") == "Sophie"
    assert response.json().get("lastname") == "Cunningham"
    assert response.json().get("totalprice") == 200
    assert response.json().get("depositpaid") is False
    assert response.json().get("bookingdates") == {
        "checkin": "2023-01-01",
        "checkout": "2023-01-15",
    }
    assert response.json().get("additionalneeds") == "Lunch"
    print(f"PUT Booking ID {booking_id}: Updated booking details.")


def test_delete_booking(booking_service, booking_id, auth_token):
    response = booking_service.delete_booking(booking_id, auth_token)
    assert response.status_code == 201
    # Verify that the booking was deleted successfully
    response = booking_service.get_booking_by_id(booking_id)
    assert response.status_code == 404
    print(f"DELETE Booking ID {booking_id}: Booking deleted successfully.")
