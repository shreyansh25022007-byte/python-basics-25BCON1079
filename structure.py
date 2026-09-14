class FactorialData:
    def __init__(self, n):
        self.n = n
        self.result = 1

data = FactorialData(5)

for i in range(1, data.n + 1):
    data.result *= i

print(f"Factorial of {data.n} = {data.result}")
