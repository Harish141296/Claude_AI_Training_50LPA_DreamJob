"""
write a function that takes a list of numbers and returns the top 3 highest values without using sort()
"""

class Solution:
    def __init__(self, ls):
        print("write a function that takes a list of numbers and returns the top 3 highest values without using sort()")
        self.ls = ls 
        
    def method1(self)-> list[int]:
        # with bubble sort
        print(self.ls) 
        top1, top2, top3 = 0, 0, 0 
        len_of_arr = len(self.ls)
        if len_of_arr and len_of_arr < 2 : 
            top1 = self.ls[0]
            return [top1,top2,top3]
        if len(self.ls) < 3 : 
            top1 = max(self.ls)
            top2 = self.ls[0] if self.ls[0] != top1 else self.ls[1]
            return  [top1,top2,top3]
        
        left, right = 0, len_of_arr -1 
        while right > left:
            for i in range(right):
                if self.ls[i] > self.ls[i + 1]:
                    self.ls[i], self.ls[i + 1] = self.ls[i + 1], self.ls[i]
            right -= 1

            print(self.ls) 
        
        top1,top2,top3 = self.ls[-1], self.ls[-2], self.ls[-3]
        return (top1, top2, top3)
            
        
    def method2(self) -> list[int]:
        # without sorting 
        top1, top2, top3 = float('-inf'),float('-inf'),float('-inf')
        len_of_arr = len(self.ls)
        if len_of_arr and len_of_arr < 2 : 
            top1 = self.ls[0]
            return [top1,top2,top3]
        if len(self.ls) < 3 : 
            top1 = max(self.ls)
            top2 = self.ls[0] if self.ls[0] != top1 else self.ls[1]
            return  [top1,top2,top3]

        max_count = 3
        initializer = 0 
        max_ls = [top1, top2, top3]
        while initializer < max_count: 
            maximum = float('-inf')
            for i in range(len_of_arr):
                if self.ls[i] > maximum:
                    maximum = self.ls[i]
            max_ls[initializer] = maximum
            self.ls.remove(maximum)
            initializer += 1
            len_of_arr -= 1 
            
        return max_ls
            
if __name__ == '__main__':
    ls = [10,2,3,1,14,15,4,8]
    sol = Solution(ls)
    top_3:list[int] = sol.method1()
    print(top_3)
    top_3:list[int] = sol.method2()
    print(top_3)