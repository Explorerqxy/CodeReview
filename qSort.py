import random
class Solution:
    def Partition(self, data, length, start, end):
        if data == [] or length < 0 or start < 0 or end > length:
            return None

        index = random.randint(start, end)
        data[index], data[end] = data[end], data[index]

        small = start - 1
        for index in range(start, end):
            if data[index] < data[end]:
                small += 1
                if small != index:
                    data[index], data[small] = data[small], data[index]

        small += 1
        data[small], data[end] = data[end] , data[small]

        return small

if __name__ == '__main__':
    data = [1,3,6,2,5,9,7,4,8]
    a = Solution()
    res = a.Partition(data,9,0,8)
    print(data)
    print(res)
    def qsort(data, length, start, end):
        if start == end:
            return
        index = a.Partition(data, length, start, end)
        if index > start:
            qsort(data, length, start, index-1)
        if index < end:
            qsort(data, length, index+1, end)
    qsort(data, 9,0,8)
    print(data)