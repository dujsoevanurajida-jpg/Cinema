class BookingRepository:
    """Репозиторий для работы с бронированиями"""
    
    def __init__(self):
        self._bookings = []  # хранилище броней (заглушка)
        self._next_id = 1
    
    def save(self, booking) -> object:
        """Сохраняет бронирование и возвращает его с присвоенным ID"""
        if booking.id is None:
            booking.id = self._next_id
            self._next_id += 1
        self._bookings.append(booking)
        print(f"[BookingRepository] Сохранено бронирование #{booking.id}")
        return booking
    
    def find_by_id(self, booking_id: int):
        """Находит бронирование по ID"""
        for booking in self._bookings:
            if booking.id == booking_id:
                return booking
        return None
    
    def find_by_user_id(self, user_id: int) -> list:
        """Находит все бронирования пользователя"""
        return [b for b in self._bookings if b.user_id == user_id]