# def six(numder):
#     long = len(str(numder))
#     l = []
#     num = 0
#     for i in range(1, long+1):
#         num = numder % 10
#         l.append(num)
#         numder = int(numder/10)
#     result = 0
#     for i in range(0, long):
#         result = result + l[i]*pow(16,i)
#     return result
# for i in range(10, 10000):
#     res = six(i)
#     if res%i == 0:
#         print(i)
#         break
#
#
# a = []
# with open('text.txt', 'r', encoding='UTF-8') as f:
#     a = f.readlines()
# f = [[0] * 70 for _ in range(70)]
# for i in range(1,31):
#     for j in range(1, 61):
#         if (i-1) >= 0 and (j - 1) >= 0:
#             f[i][j] = max(f[i-1][j],f[i][j-1]) + int(a[i-1][j-1])
#         elif i - 1 >= 0:
#             f[i][j] = f[i-1][j]+int(f[i-1][j-1])

#
#
#
# t = int(input())
# c = int(input())
# s = int(input())
# speed = float(c/t)
# surplus = s-c
# res = int(surplus/speed)
# print(res)
#
# temp = []
# list = []
# n = int(input())
# for i in range(n):
#     list.append(input())
# for k in range(n):
#     if k not in temp:
#         temp.append(list[k])
# print(temp)
#
# def check(str):
#     if (str== str[::-1]):
#         return 1
#     else:
#         return 0
# def nixu(str):
#     a = list(str)
#     a.reverse()
#     return (''.join(a))
# str = input("请输入一个字符：")
# res = []
# temp = []
# n = len(str)
# if n==1:
#     res = str
# else:
#     if (check(str)):
#         res = str
#     else:
#         temp = list(str)
#         print(temp)
#         for i in range(n):
#             Str = str
#             Str += nixu(temp[0:i+1])
#             print("str",str)
#             if(check(Str)):
#                 res = Str
#             break
#
# print(res)
#
#
# N = 110
# a = [[0]*N for _ in range(N)]
# n, m = map(int,input().split())
# for i in range(1,n+1):
#     a[i][1:m+1] = list(input())
#
# def check(i, j, ix, jy, len):
#     target = a[i][j]
#     x, j= i, j
#     for k in range(1,len + 1):
#         x = x + ix
#         y = y + jy
#         if x < 1 or x > n or y<1 or y >n:
#             return False
#         if a[x][y] != target:
#             return False
#     return True
#
# res = 0
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         for len in range(1,min(n,m)//2+1):
#             if(check(i,j,-1,-1,len) and check(i,j,-1,1,len) and check(i,j,1,1,len) and check(i,j,1,-1,len))
#                 res += 1
#
# print(res)
#
# def ch(n1,n2):
#     number = n1
#     n1 = n2
#     n2 = number
#     return n1,n2
# n = int(input())
# l = []
# str = input()
# l = str.split(' ')
# dj = 0
# for i in range(0,n):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             ((l[i],l[j])) = ch((l[i],l[j]))
#             dj = dj + int((l[i],l[j]))
# print(dj)





































