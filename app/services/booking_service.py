from app.repositories.seat_repository import SeatRepository
from app.repositories.booking_repository import BookingRepository
from app.models.booking import Booking

class BookingService:
    """Сервис бронирования (бизнес-логика)"""
    
    def __init__(self):
        self.seat_repo = SeatRepository()
        self.booking_repo = BookingRepository()
    
    def book_tickets(self, user_id: int, session_id: int, seat_ids: list):
        """
        Основной метод бронирования билетов.
        Возвращает объект Booking или None при ошибке.
        """
        print(f"[BookingService] Начало бронирования: user={user_id}, session={session_id}, seats={seat_ids}")
        
        # Проверка доступности мест
        available_seats = self.seat_repo.find_by_session_and_seats(session_id, seat_ids)
        
        if len(available_seats) != len(seat_ids):
            print("[BookingService] Ошибка: некоторые места уже заняты")
            return None
        
        # Создание бронирования
        booking = Booking(
            id=None,
            user_id=user_id,
            session_id=session_id,
            seats=available_seats
        )
        
        # Сохранение бронирования
        saved_booking = self.booking_repo.save(booking)
        
        # Блокировка мест
        self.seat_repo.mark_as_booked(available_seats)
        
        print(f"[BookingService] Бронирование успешно: #{saved_booking.id}")
        return saved_booking
    
    def cancel_booking(self, booking_id: int, user_id: int) -> bool:
        """Заглушка: отмена бронирования"""
        booking = self.booking_repo.find_by_id(booking_id)
        if booking and booking.user_id == user_id:
            booking.cancel()
            return True
        return False