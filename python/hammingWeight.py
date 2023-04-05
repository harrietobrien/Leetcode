class Solution:
    def __init__(self, n):
        self.n = n
        self.test()

    def hammingWeight(self, n: int) -> int:
        binary: str = bin(n)[2:]
        return binary.count('1')
        # return str(bin(n)).count("1")

    def test(self):
        print(self.hammingWeight(self.n))


'''
bin(0o0000000000000000000000010000000)
--> '0b1000000000000000000000'
'''
ns = [0o0000000000000000000000000001011,
      0o0000000000000000000000010000000,
      11111111111111111111111111111101]
for n in ns:
    s = Solution(n)
