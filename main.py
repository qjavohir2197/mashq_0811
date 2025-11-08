#1-misol
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, numbers))
print(result)

#2-misol
numbers = [-3, -1, 0, 2, 4, 6]
result = list(map(lambda x: x*2, filter(lambda x: x > 0, numbers)))
print(result)

#3-misol
words = ["salom", "dunyo", "python"]
result = list(map(lambda s: s.upper(), words))
print(result)

#4-misol
numbers = [3, 4, 6, 9, 12, 15, 20]
result = list(filter(lambda x: x % 3 == 0, numbers))
print(result)

#5-misol
import math
ebob = lambda a, b: math.gcd(a, b)
print(ebob(24, 36))
