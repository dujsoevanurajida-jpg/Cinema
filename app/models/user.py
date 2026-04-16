class User:
    """Модель пользователя"""
    
    def __init__(self, id: int = None, name: str = "", email: str = "", role: str = "guest"):
        self.id = id
        self.name = name
        self.email = email
        self.role = role  # guest, user, admin
    
    def login(self, email: str, password: str) -> bool:
        """Заглушка: аутентификация пользователя"""
        print(f"[User] Попытка входа: {email}")
        return True
    
    def logout(self) -> None:
        """Заглушка: выход из системы"""
        print("[User] Выход из системы")
    
    def get_bookings(self) -> list:
        """Заглушка: получение списка броней"""
        return []