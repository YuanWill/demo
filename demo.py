# TempStr = input("请输入带有符号的温度：")
# if TempStr[-1] in ['F','f']:
#     C = (eval(TempStr[0:-1])-32)/1.8
#     print("转化后的温度就是{:.2f}C".format(C))
# elif TempStr[-1] in ['C','c']:
#     F = 1.8*eval(TempStr[0:-1])+32
#     print("转化后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")

    
def fab(max): 
    n = 0
    a = 0
    b = 1
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        print(a,b)
        n = n + 1

if __name__ == "__main__":
    for n in fab(6): 
        print(n)
