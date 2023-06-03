import sys

nums = []
for n in sys.stdin:
    if n.__class__ == int:
        nums.append(n)
    else:
        break
print(f"Сумма: {sum(nums)}")
