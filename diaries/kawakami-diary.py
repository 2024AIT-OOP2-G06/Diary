from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "班員に助けられながらも、githubのmargeやpullrequestsの意味ややり方を学ぶことができた。"

    def get_author(self):
        return "Yuiya"
