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