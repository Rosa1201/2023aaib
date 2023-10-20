class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d ={}
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        #print(d) #可以印看看,字母出現在次數統計結果

        for c in t:
            if c not in d: 
                return c 
            if d[c] == 0: 
                return c 
            else:
                d[c] = d[c] - 1 

        return"" #這行沒寫也沒關係