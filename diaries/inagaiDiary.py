from diaries.AbstractDiary import AbstractDiary

class InagakiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-03"

    def get_summary(self):
        return "みんなには是非とも頑張ってほしい...特にコーディングとか()"

    def get_author(self):
        return "Inagai"