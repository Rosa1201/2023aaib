class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0 #迴圈前面ans=0
        while n>0: #剝皮法一次撥一層皮(第7週)
            ans += n%2 #撥下來的屑屑收起來
            n = n // 2 #洋蔥剝皮後變小了
        return ans #迴圈後面 ans拿來用