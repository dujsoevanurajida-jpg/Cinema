class UserView:
    """Представление для авторизованного пользователя"""
    
    def show_confirmation_page(self, booking):
        """Страница подтверждения бронирования"""
        message = f"""
        ===== ПОДТВЕРЖДЕНИЕ БРОНИРОВАНИЯ =====
        Номер брони: {booking.id}
        Сеанс: {booking.session_id}
        Места: {[s.get_id() for s in booking.seats]}
        Сумма к оплате: {booking.total_price()} руб.
        Статус: {booking.status}
        =======================================
        """
        print(message)
        return message
    
    def show_error_page(self, error_text):
        """Страница с ошибкой"""
        error_msg = f"[ОШИБКА] {error_text}"
        print(error_msg)
        return error_msg
    
    def show_bookings_history(self, bookings):
        """Показывает историю бронирований"""
        print("=== ИСТОРИЯ БРОНИРОВАНИЙ ===")
        if not bookings:
            print("У вас пока нет бронирований")
        else:
            for booking in bookings:
                print(f"Бронь #{booking.id}: сеанс {booking.session_id}, мест: {len(booking.seats)}")
        return bookings