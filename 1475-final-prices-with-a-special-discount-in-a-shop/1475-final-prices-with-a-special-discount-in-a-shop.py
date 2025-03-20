class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        answer = prices[:]
        stack = []  # 스택에는 아직 할인이 적용되지 않은 인덱스 저장
        
        for i in range(n):
            # 스택의 top 값보다 현재 값이 작거나 같다면 할인 적용
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                answer[idx] -= prices[i]
            
            stack.append(i)  # 현재 인덱스를 스택에 저장
        
        return answer