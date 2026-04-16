class Seat:
    """Модель места в кинозале"""
    
    def __init__(self, row: int = 0, number: int = 0, is_available: bool = True, session_id: int = None):
        self.row = row
        self.number = number
        self.is_available = is_available
        self.session_id = session_id
    
    def get_id(self) -> str:
        return f"{self.row}:{self.number}"
    
    def book(self) -> bool:
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def release(self) -> None:
        self.is_available = True