
class Solution:

    def f1(self, a: int, b: int) -> int:
        return a + b
    
    def f2(self, a: int, b: int) -> int:
        return a if a >= b else b
    
    def f4(self, a: int, b: int):
        ar = (a + b) / 2
        ge = (a * b) ** 0.5
        go = 2 / (1 / a + 1 / b)
        return ar, ge, go
    
    def f10(self, son: int, raqam: int) -> int:
        return son * 10 + raqam
    
    def f16(self, n: int) -> int:
        p = 1
        for i in range(1, n + 1):
            p *= i
        return p
    
    def f34(self):
        return """"Hello Python'"""

    def f89(self, son: int) -> int:
        onlik = son // 10
        birlik = son % 10
        return birlik * 10 + onlik
    
    def f1551(self):
        """Hello, CPython"""
        return "Hello, CPython"
    
 
def main() -> None:
    solution = Solution()

    # Input data type
    # int
    # a = int(input())
    # b = int(input())
    # c = int(input())

    # Output:
    print(dir(solution))

if __name__ == "__main__":
    main()
