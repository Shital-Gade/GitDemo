# 1
print(bin(1024))
print(hex(1024))
# 2
print(round(5.23222, 2))
# 3
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())
# 4
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))
# 5
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.difference(set2))
# 6
set1.union(set2)
# 7
{x: x ** 3 for x in range(5)}
# 8
list1 = [1, 2, 3, 4]

list1.reverse()

print(list1)
# 9
list2 = [3, 4, 2, 5, 1]

list2.sort()

print(list2)
