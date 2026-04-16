class SeatRepository:
    """Репозиторий для работы с местами"""
    
    def __init__(self):
        self._seats = {}  # хранилище мест (заглушка)
    
    def find_by_session_and_seats(self, session_id: int, seat_ids: list) -> list:
        """
        Проверяет доступность мест.
        Возвращает список доступных мест.
        """
        available = []
        for seat_id in seat_ids:
            seat = self._seats.get(seat_id)
            if seat and seat.is_available:
                available.append(seat)
        return available
    
    def mark_as_booked(self, seats_list: list) -> None:
        """Блокирует места после бронирования"""
        for seat in seats_list:
            seat.is_available = False
        print(f"[SeatRepository] Заблокированы места: {[s.get_id() for s in seats_list]}")
    
    def save(self, seat) -> None:
        """Сохраняет место (заглушка)"""
        self._seats[seat.get_id()] = seat