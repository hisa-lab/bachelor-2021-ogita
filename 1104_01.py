#1 から 100 までの自然数の内、3 の倍数であれば Fizz、5 の倍数であれば Buzz、15 の倍数であれば FizzBuzz、
#それ以外の値はそのまま出力するプログラムを作成しなさい。

def true(x):
    
    if x % 3 == 0:
        print("Fizz")

    elif x % 5 == 0:
        print("Buzz")

    elif x % 15 == 0:
        print("FizzBuzz")

    else:
        print(x)

        true(6)
        true(10)
        true(30)

