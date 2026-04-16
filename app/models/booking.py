from datetime import datetime

class Booking:
    """Модель бронирования"""
    
    def __init__(self, id: int = None, user_id: int = None, session_id: int = None, 
                 seats: list = None, created_at: datetime = None):
        self.id = id
        self.user_id = user_id
        self.session_id = session_id
        self.seats = seats or []
        self.created_at = created_at or datetime.now()
        self.status = "confirmed"
    
    def total_price(self, base_price: int = 300) -> int:
        return len(self.seats) * base_price
    
    def cancel(self) -> None:
        self.status = "cancelled"
    
    def confirm_payment(self) -> None:
        self.status = "paid"