'''
@Author: your name
@Date: 2020-01-29 21:39:11
@LastEditTime : 2020-01-30 13:41:48
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \my_algorithm_note\DP_throw_egg.py
'''

"""
有一种玻璃杯质量确定但未知，需要检测。   
有一栋100层的大楼，该种玻璃杯从某一层楼扔下，刚好会碎。   
现给你两个杯子，问怎样检测出这个杯子的质量，即找到在哪一层楼刚好会碎？
"""
# link1:https://zhuanlan.zhihu.com/p/92288604
# link2:https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247484557&idx=1&sn=739d80488fe1169a9c9ca26ecfcdfba6&chksm=fa0e6b0ccd79e21a1c2b0d99db69f6206cddddfe2367742e9de1d7d17ec35a5ce29fa4e30d63&token=110841213&lang=zh_CN#rd

# 1、二分查找法
# 2、分段查找法：10楼丢一次，20楼丢一次，碎了就逐层测试
# 3、动态规划
"""
我们可以将这样的问题简记为 W(n,k) ，其中 n 代表可用于测试的杯子数，k 代表被测试的楼层数。对于问题 W(2,10)， 我们可以如此考虑
将第 1 个杯子，在第 i 层扔下（ i 可以为 1～k 的任意值），如果碎了，则我们需要用第 2 个杯子，解决从第 1 层到第 i-1 层楼的 子问题 W(1,i-1)；
如果这个杯子没碎，则我们需要用这两个杯子，解决从 i+1 层到第 100 层的子问题 W(2,100-i)。
用公式来描述就是：
W(n, k) = 1 + min{max(W(n -1, x -1), W(n, k - x))}, x in {2, 3, ……，k}
"""

# 动态规划代码实现


def superEggDrop(K: int, N: int):

    memo = dict()

    def dp(K, N) -> int:
        # base case
        if K == 1:
            return N
        if N == 0:
            return 0
        # 避免重复计算
        if (K, N) in memo:
            return memo[(K, N)]

        res = float('INF')
        # 穷举所有可能的选择
        for i in range(1, N + 1):
            res = min(res,
                      max( # 这里的max是指最坏情况
                          dp(K, N - i),
                          dp(K - 1, i - 1)
                      ) + 1
                      )
        # 记入备忘录
        memo[(K, N)] = res
        return res

    return dp(K, N)


# 二分法代码实现
def superEggDrop(self, K: int, N: int) -> int:

    memo = dict()

    def dp(K, N):
        if K == 1:
            return N
        if N == 0:
            return 0
        if (K, N) in memo:
            return memo[(K, N)]

        # for 1 <= i <= N:
        #     res = min(res,
        #             max(
    #                     dp(K - 1, i - 1),
    #                     dp(K, N - i)
        #                 ) + 1
        #             )

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1)  # 碎
            not_broken = dp(K, N - mid)  # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res

    return dp(K, N)
