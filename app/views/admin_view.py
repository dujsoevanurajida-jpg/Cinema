class AdminView:
    """Представление для администратора"""
    
    def show_admin_panel(self):
        """Показывает панель администратора"""
        print("=== Панель администратора ===")
        print("1. Управление фильмами")
        print("2. Управление сеансами")
        print("3. Просмотр отчётов")
        print("4. Выход")
    
    def show_reports(self, reports):
        """Показывает отчёты"""
        print("=== Отчёты ===")
        for report in reports:
            print(report)