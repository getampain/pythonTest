from multiprocessing import Process
import os


#개별 프로세스의 id를 확인하기 위한 값
def info(title):
    print(title)
    print('module name : ', __name__)
    print("parnet process : ", os.getppid())
    print("process id : ", os.getpid())


def f(name):
    info("function f")
    print('hello', name)
    print("===="*10)

if __name__ == '__main__':
    #멀티프로세스 이전값을 확인하기 위한 항목
    info('main line')
    print("\n")

    p = Process(target=f, args=('bob',))
    p2 = Process(target=f, args=('suji',))

    p.start()
    p2.start()

    #print(12325)

    p.join()
    p2.join()
    
    #print(123256)