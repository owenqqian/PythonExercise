'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
set_ = set()
list_ = [1, 2, 3, 4]

for x in list_:
    for y in list_:
        for z in list_:
            if x != y and y != z and x != z:  # 排除相同数字的情况
                num = x * 100 + y * 10 + z
                set_.add(num)

print("满足条件的三位数：", set_)
print("共有", len(set_), "个满足条件的三位数。")
