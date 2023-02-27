def my_median(sample):
     n = len(sample)
     index = n // 2

     if n % 2:
         return sorted(sample)[index]
     return sum(sorted(sample)[index - 1:index + 1]) / 2

print("median dari data tersebut adalah :")
print(my_median([0, 0, 1, 2, 2, 2, 6]))