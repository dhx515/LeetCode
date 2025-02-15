class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split('-'))

        # 윤년 판단 함수
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        # 월별 누적 일수 (윤년 여부에 따라 다름)
        if is_leap(year):
            prefix_days = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]  # 윤년 (2월 29일)
        else:
            prefix_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]  # 평년 (2월 28일)

        # 해당 월까지의 합 + 주어진 날짜(day)
        return prefix_days[month - 1] + day