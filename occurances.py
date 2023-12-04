nums = [1,2,2,3,3,3,2,7,7,7,7,7,8]
n = len(nums)
target = n//3
dict1 = {}
for i in nums:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1, set(nums), target)
res = []
for i in set(nums):
    if dict1[i] > target:
        res.append(i)
print(res)