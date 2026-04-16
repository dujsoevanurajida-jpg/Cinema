from app.controllers.booking_controller import BookingController

def main():
    print("=== Кинотеатр: бронирование билетов (MVC) ===\n")

    # Имитация POST-запроса от клиента
    request_data = {
        "user_id": 101,
        "session_id": 5,
        "seat_ids": ["3:5", "3:6", "3:7"]
    }

    controller = BookingController()
    result = controller.create_booking(request_data)

    print("\nРезультат контроллера передан в представление.")

if __name__ == "__main__":
    main()