#가변 함수 *arg

def args_func(*arg):
    print(*arg)

args_func("kim")
args_func("kim","park")

# kwargs

def kwargs_func (**kwargs):
    print(kwargs)

kwargs_func(name1="kim", name2="park", name3="lee")

def example_mul(arg1, arg2 ,*arg, **kwargs):
    print(arg1, arg2 , arg, kwargs)

example_mul("sangjun", "yujin", "sang","jun",sangjun="male",yujin="female")

#중첩함수

def nested_func(num):
    def func_in_func(num):
        print('>>>',num)
    print("in func")
    func_in_func(num + 421)

nested_func(10000)

#int형 list로 반환

def change_func(x : int) -> list :
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1 ,y2 ,y3]
    
print(change_func(5))

def chang_func2 (x : float) -> int :
    y1 = x * 10.2
    y2 = x * 20.5
    return (y1, y2)

print(chang_func2(1.3))

# 정수형으로 왜 안바뀌었을까,,
    
