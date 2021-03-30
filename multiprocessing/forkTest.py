#윈도우에서는 fork 기능이 사용불가능한것으로 알고있는대 python fork 기능을 사용가능할지 test 코드
#

# 불가능하다 ㅋ 예상대로임
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':


    mp.set_start_method('fork')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()