'''
@Author: your name
@Date: 2020-01-27 23:32:18
@LastEditTime : 2020-01-28 00:11:17
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \my_algorithm_note\kmp.py
'''


class KMP(object):
    def __init__(self, t, p):
        '''
        @description: t:主字符串，p:匹配字符串
        @param {type} 
        @return: 
        '''
        self.t = t
        self.p = p

    def cal_next(self):
        next = [-1 for _ in range(len(self.p))]
        j = -1
        for i in range(len(self.p)):
            if j == -1 or self.p[i] == self.p[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return next

    def search(self):
        i = j = 0
        next = self.cal_next()
        while i < len(self.t) and j < len(self.p):
            if j == -1 or self.t[i] == self.p[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(self.p):
            return i - j
        else:
            return -1


if __name__ == '__main__':
    kmp = KMP('ababcabcacbab', 'abcac')
    print(kmp.search())
