from datetime import datetime

class Session:
    """Модель сеанса"""
    
    def __init__(self, id: int = None, movie_id: int = None, hall: str = "", 
                 start_time: datetime = None, price: int = 300):
        self.id = id
        self.movie_id = movie_id
        self.hall = hall
        self.start_time = start_time
        self.price = price
    
    def get_available_seats(self) -> list:
        return []
    
    def get_booked_seats(self) -> list:
        return []