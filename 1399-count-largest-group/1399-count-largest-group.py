class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        def digit_sum(num):
            return sum(int(d) for d in str(num))
        
        groups = defaultdict(int)  # {digit_sum: count}
        
        for i in range(1, n + 1):
            groups[digit_sum(i)] += 1  # 각 자릿수 합 그룹의 크기 증가

        max_size = max(groups.values())  # 가장 큰 그룹 크기 찾기
        return sum(1 for size in groups.values() if size == max_size)  # 해당 크기를 가진 그룹 개수 반환