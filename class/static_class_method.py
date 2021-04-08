
#스태틱 메소드와 기본 메소드인 클래스 메소드의 차이를 파악하기 위함
#스태틱 메소드 같은 경우에는 합치는 ()를 사용하여 __init__을 하지 않아도 함수를 사용 가능하다
#이걸 쓰느니 다른 방법을 통하여 공통적으로 사용되는 함수들을 import를 하여 사용하면 되지않냐는 논점에 대해서 토론이 있을정도로 
#독특한 방법이다.


class StaticMethodClass():

    #해당 데코레이션을 사용함으로 init 없이 사용한다
    #마찬가지로 class 메소드의 기본인자인 self를 사용하지 않아도 된다.
    @staticmethod
    def sumFunc(numa, numb):
        return numa + numb
    
    #해당 데코레이션을 사용함으로 init 없이 사용한다    
    #마찬가지로 class 메소드의 기본인자인 self를 사용하지 않아도 된다.
    @staticmethod
    def subFunc(numa, numb):
        return numa - numb


if __name__ == "__main__":
    #init 없이 사용한다    
    tempNum = StaticMethodClass.subFunc(12,2)
    print(tempNum)
    #init 없이 사용한다    
    tempNum = StaticMethodClass.sumFunc(2,45)
    print(tempNum)




