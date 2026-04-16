class GuestView:
    """Представление для гостя (неавторизованного пользователя)"""
    
    def show_movies_list(self, movies):
        """Показывает список фильмов"""
        print("=== Список фильмов ===")
        for movie in movies:
            print(f"- {movie.title}")
    
    def show_sessions_list(self, sessions):
        """Показывает расписание сеансов"""
        print("=== Расписание сеансов ===")
        for session in sessions:
            print(f"- Зал {session.hall}: {session.start_time}")
    
    def show_login_prompt(self):
        """Приглашение ко входу"""
        print("Для бронирования войдите в систему")