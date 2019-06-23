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

#Hash,一般称作“散列”， 就是把任意长度的输入，通过散列算法，变成固定长度的输出。
#在Python中，字典是通过哈系表实现的，通常字典也被认为是可变的哈希表，是该语言中
#惟一的映射类型。
字典创建了两个数组，一个数组下放key，另一个数组下放对应的value。实现集合的方式叫做Hash Set，实现字典的方式
叫做Hash Map/Table（注：Map指的就是通过key来寻找value的过程）
在字典中，key是唯一的值，如果一元素作为key，当遇到两个元素相同时，则只保留最后记录元素的下标o

