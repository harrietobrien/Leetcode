class Solution:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.test()

    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        digits1 = list(num1[::-1])
        digits2 = list(num2[::-1])
        for i in range(len(digits1)):
            n1 = ord(digits1[i]) - ord('0')
            for j in range(len(digits2)):
                n2 = ord(digits2[j]) - ord('0')
                product += n1 * n2 * 10 ** (i + j)
        return str(product)

    def test(self):
        print(self.multiply(self.num1, self.num2))


num1 = "2"
num2 = "3"
s = Solution(num1, num2)