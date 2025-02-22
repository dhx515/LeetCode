class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # 요일 매핑 리스트
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # 날짜 객체 생성 후 요일 인덱스 가져오기
        return days[datetime.date(year, month, day).weekday()]