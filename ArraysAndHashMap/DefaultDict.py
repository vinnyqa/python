from collections import defaultdict

class Solution:
    def dummy(self):
        d = defaultdict(list)
        d['fruits'].append('apple')
        print(d)
        d['vegetables'].append('carrot')
        print(d)
        print(d['juices'])

sol = Solution()
print(sol.dummy())