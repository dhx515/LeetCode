class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        dict=Counter(words[0])
        for key in dict.keys():
            c=0
            for i in words:
                if key in i:
                    dict[key]=min(dict[key],i.count(key))
                    c+=1
            if c!=len(words):
                dict[key]=0
        for key in dict.keys():
            if dict[key]>0:
                for i in range(dict[key]):
                    ans.append(key)
        return (ans)