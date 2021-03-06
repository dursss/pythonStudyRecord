# 第9天学习
# 偏函数
# 在介绍函数参数的时候，通过设置参数的默认值，可以降低函数调用的难度，而偏函数也可以做到这一点
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
# 但是int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换

# print(int('12345', base=16))
#
#
# def int2(x, base=2):
#     return int(x, base)
#
#
# print(int2('10001001010101101011011110'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2()

import functools

int2 = functools.partial(int, base=2)
print(int2('100101010110'))

# 所以，简单总结，functools函数就是把函数的某些参数固定住，返回一个新的函数，调用这个新函数会更简单

# 为了编写可维护的代码，我们把很多函数分组，放到不同的文件里，，这样，每个文件包含的代码就相对比较少，python每一个.py就叫做一个模块

# 每一个包下都要有一个__init__.py文件，否则python就把这个目录当成普通目录了，__init__.py可以是空文件，也可以有代码。因为每一个__init__.py本身就是一个模块
# 而它的模块名就是包名
