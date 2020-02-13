'''
@Author: your name
@Date: 2020-01-30 20:39:33
@LastEditTime : 2020-01-31 17:54:04
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \my_algorithm_note\Sort.py
'''
# 各种排序算法实现

l = [10, 4, 2, 1, 8, 5, 7, 6]
sl = [1, 2, 4, 5, 6, 7, 8, 10]


def bubble_sort(il):
    # 冒泡排序
    n = len(il)
    for i in range(1, n):
        flag = True
        for j in range(n - i):
            if il[j] > il[j + 1]:
                flag = False
                il[j], il[j + 1] = il[j + 1], il[j]
        if flag:
            break
    return il


def quick_sort(il):
    # 快速排序
    def quicksort(list, low, high):
        if low < high:
            q = partion(list, low, high)
            quicksort(list, low, q - 1)
            quicksort(list, q, high)

    def partion(list, start, r):
        i = start - 1
        for j in range(start, r):
            if list[j] <= list[r]:  # j都是小于r的数、i都是大于r的数
                # i+1的位置是左哨兵的位置，大于标点
                # j的位置是右哨兵的位置，小于标点
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i + 1], list[r] = list[r], list[i + 1]  # j遍历一遍后，i是小于r的边界，i+1便大于r了
        return i + 1

    quicksort(il, 0, len(il) - 1)
    return il


def insert_sort(il):
    # 插入排序
    for i in range(1, len(il)):
        key = il[i]
        for j in range(i, -1, -1):
            # 当前位置是j，j-1为探查位置
            if il[j - 1] > key:
                il[j] = il[j - 1]
            else:
                break
        il[j] = key
    return il


def bubble_sort1(il):
    length = len(il)
    flag = False
    for i in range(0, length):
        for j in range(1, length - i):
            if il[j - 1] > il[j]:
                il[j], il[j - 1] = il[j - 1], il[j]
                flag = True
            if not flag:
                break
    return il


def quick_sort1(il):
    def quicksort(l, low, high):
        if low < high:
            q = partion(l, low, high)
            quicksort(l, low, q - 1)
            quicksort(l, q, high)
        return l

    def partion(l, start, r):
        i = start - 1
        for j in range(start, r):
            if l[j] <= l[r]:
                i += 1
                l[i], l[j] = l[j], l[i]
        l[i + 1], l[r] = l[r], l[i + 1]
        return i + 1

    return quicksort(il, 0, len(il) - 1)


if __name__ == "__main__":
    result = quick_sort1(l)
    print(result)
    if result == sl:
        print('Done')
    else:
        print('Error')
