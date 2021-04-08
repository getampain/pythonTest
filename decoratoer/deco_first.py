#이미 만들어져 있는 코드를 수정하지 않고 레퍼함수를 사용해서 여러기능을 사용하기 위하여 쓴다.


def decoration_function(innerFunction):

    def is_it_work():
        print("함수가 호출되기전입니다.")
        return innerFunction()

    # 마지막에 리턴해줄 경우에는 ()를 붙이지 않고 함수 자체를 리턴해준다.
    return is_it_work

#@데코레이션을 사용해준다.
@decoration_function
def printFunction_1():
    print("hello world?")


#@데코레이션을 사용해준다.
@decoration_function
def printFunction_2():
    print("god with be you world?")

if __name__ == "__main__":
    printFunction_1()
    printFunction_2()


