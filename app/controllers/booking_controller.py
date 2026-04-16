from app.services.booking_service import BookingService
from app.views.user_view import UserView

class BookingController:
    """Контроллер бронирования"""
    
    def __init__(self):
        self.service = BookingService()
        self.view = UserView()
    
    def create_booking(self, request_data: dict):
        """
        Обрабатывает запрос на бронирование.
        request_data = {user_id, session_id, seat_ids}
        """
        user_id = request_data.get("user_id")
        session_id = request_data.get("session_id")
        seat_ids = request_data.get("seat_ids", [])
        
        booking = self.service.book_tickets(user_id, session_id, seat_ids)
        
        if booking:
            return self.view.show_confirmation_page(booking)
        else:
            return self.view.show_error_page("Некоторые места уже заняты")
    
    def get_user_bookings(self, user_id: int):
        """Заглушка: получение истории бронирований"""
        bookings = self.service.booking_repo.find_by_user_id(user_id)
        return self.view.show_bookings_history(bookings)