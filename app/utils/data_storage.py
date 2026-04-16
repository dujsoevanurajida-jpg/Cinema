class DataStorage:
    """Заглушка для хранения данных (в реальности - работа с БД)"""
    
    @staticmethod
    def save_booking(booking_data):
        """Сохраняет бронирование"""
        print(f"[Storage] Сохраняем бронь: {booking_data}")
    
    @staticmethod
    def get_movies():
        """Получает список фильмов"""
        return []
    
    @staticmethod
    def get_sessions():
        """Получает список сеансов"""
        return []