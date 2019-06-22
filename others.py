#（python）给定一个整数数组和一个目标值，找出数组中和为目标值的两个数--算法
# def solution(nums, target):
#     if len(nums)<2:
#         return
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return[i,j]

# def solution(nums, target):
#     dict1 = {}
#     for i in range(len(nums)):
#         num = target - nums[i]
#         if num not in dict1:
#             dict1[nums[i]] = i
#         else:
#             return [dict1[num], i]
def solution(nums, target):
    if len(nums)< 2:
        return []
    dict1 = {}
    for i in range(len(nums)):
        dict1[nums[i]] = i
        # if dict1.has_key(target-nums[i]):
        if (target - nums[i]) in dict1:
            return [i, dict1[target-nums[i]]]



