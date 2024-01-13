class Solution(object):
    def numberOfSteps(self, num):
        if num == 0:
            return 0
        
        step_counter = 1
        cur_number = num
        while True:
            
            
            if cur_number <= 1:
                break
            
            step_counter += 1
            
            if cur_number%2 == 0:
                cur_number //= 2
            else:
                cur_number -= 1
                
        return step_counter