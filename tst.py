lst = [1,2,3,4,5,6]

def longestrecString(s):
    if len(s) <= 1:
        return s
    res = 0
    maxlen = 0
    if s[0] == s[1]:
        res = s[0:2]
    dp = [False for i in range(len(s))]*len(s)
    for j in range(2,len(s)):
        dp[j][j] = True
        for i in range(j):
            dp[i][j] = s[i] == s[j] and(j-i <= 2 or dp[i+1][j-1])
            if dp[i][j] and j-i+1 > maxlen:
                maxlen = j-i+1
                res = s[i:j+1]
    return res
    return maxlen

def Numberof1(n):
    count = 0
    flag = 1
    while (flag):
        if (n&flag):
            count += 1
        flag = flag << 1
    return count
 #循环32次
 def NumberOf1(n):
     count = 0
     while(n):
         count += 1
         n = (n-1)&n
     return count

def a(f):
    return False
def a(h,j):
    return True


if __name__ == '__main__':
    # lst.reverse()
    # print(lst)
    #
    print(a(123))