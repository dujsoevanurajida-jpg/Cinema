class Movie:
    """Модель фильма"""
    
    def __init__(self, id: int = None, title: str = "", duration: int = 0, genre: str = ""):
        self.id = id
        self.title = title
        self.duration = duration
        self.genre = genre
    
    def get_info(self) -> str:
        return f"{self.title} ({self.duration} мин, {self.genre})"
    
    def get_sessions(self) -> list:
        return []