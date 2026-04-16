from app.views.user_view import UserView

class AuthController:
    """Контроллер аутентификации"""
    
    def __init__(self):
        self.view = UserView()
    
    def login(self, email: str, password: str) -> bool:
        """Заглушка: вход в систему"""
        print("[AuthController] Вызван метод login()")
        # TODO: реализовать аутентификацию
        return True
    
    def logout(self) -> None:
        """Заглушка: выход из системы"""
        print("[AuthController] Вызван метод logout()")
        pass
    
    def register(self, name: str, email: str, password: str) -> bool:
        """Заглушка: регистрация пользователя"""
        print(f"[AuthController] Регистрация: {name}, {email}")
        return True