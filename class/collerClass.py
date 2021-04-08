#매직펑션 caller 태스트 해본 케이스
class CallerClass():

    def __init__(self):
        self.newNumber = 12

    # __call__을 사용한 경우 ()할경우 바로 적용된다
    def __call__(self):
        return self.newNumber + 12


if __name__ == "__main__":
    newCaller = CallerClass()
    print(newCaller())