class Solution(object):
    def sortByBits(self, arr):
        arr.sort(key=self.custom_sort_key)
        return arr
    
    def custom_sort_key(self, num):
        bit_count = bin(num).count('1')
        return (bit_count, num)