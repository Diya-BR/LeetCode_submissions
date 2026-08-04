class Solution:
    def fib(self, n: int) -> int:
        fib = [0,1]
        for i in range(2,n+1):
            fib.append(fib[len(fib)-2]+fib[len(fib)-1])
            print(fib)
        return fib[n]


        