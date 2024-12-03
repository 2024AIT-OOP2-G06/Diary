from diaries.AbstractDiary import AbstractDiary

class YuyaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "授業を受けた。難しかった。"

    def get_author(self):
        return "Yuya"
