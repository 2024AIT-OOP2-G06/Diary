from diaries.AbstractDiary import AbstractDiary

class KatoDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日も寒いです"

    def get_author(self):
        return "Kato"
