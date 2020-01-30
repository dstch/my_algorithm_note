'''
@Author: your name
@Date: 2020-01-30 20:39:33
@LastEditTime : 2020-01-30 23:42:41
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
        for j in range(n-i):
            if il[j] > il[j+1]:
                flag = False
                il[j], il[j+1] = il[j+1], il[j]
        if flag:
            break
    return il


def quick_sort(il):
    # 快速排序
    def quicksort(list, low, high):
        if low < high:
            q = partion(list, low, high)
            quicksort(list, low, q-1)
            quicksort(list, q, high)

    def partion(list, start, r):
        i = start-1
        for j in range(start, r):
            if list[j] <= list[r]:
                # i+1的位置是左哨兵的位置，大于标点
                # j的位置是右哨兵的位置，小于标点
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i+1], list[r] = list[r], list[i+1]
        return i+1
    quicksort(il, 0, len(il)-1)
    return il


if __name__ == "__main__":
    print(quick_sort(l))
