class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        liste=text.split()
        result=[]

        for i in range(len(liste)):
            if i+1<len(liste)-1 and liste[i]==first and liste[i+1]==second:
                result.append(liste[i+2])
            
        
        return result