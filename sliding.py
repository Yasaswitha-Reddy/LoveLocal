nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 4
res = []
for i in range(len(nums)-k):
    temp = nums[i:i+k]
    res.append(max(temp))
print(res)