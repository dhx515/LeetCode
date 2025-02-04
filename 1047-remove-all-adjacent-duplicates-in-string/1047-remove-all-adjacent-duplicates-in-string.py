class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            # 스택이 비어 있지 않고, top과 현재 문자가 같으면 pop (중복 제거)
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)  # 스택에 추가
        
        return "".join(stack)  # 스택에 남은 문자들을 문자열로 변환