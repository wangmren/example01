# import random
#
#
# def bubble_sort(li):
#     for i in range(len(li)-1):
#         exchange = False
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]
#                 exchange = True
#         print(li)
#         if not exchange:
#             return
#
#
# li = [random.randint(0, 15) for i in range(15)]
# print(li)
# bubble_sort(li)


















def maopao(li):
    for i in range(len(li)-1):

        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
        print(li)

li = [1, 4, 6, 5, 8, 3, 9, 7, 2]
maopao(li)

