import multiprocessing as mp

"""
python 에서 멀티프로세스는 3가지 방법이 가능하다

spawn : 완전 새로운 인터프리터 프로세스를 실행한다. fork, forkserver에 비해서 다소느림
fork : os.fork기능을 사용한다(윈도우는 해당기능이 없지않나? 어떻게 작동함???) 
forkserver : 서버프로세스가 실행하는방법 역순으로 안전성이 떨어진다 spawn이 가장안전

set_start_method() 어떤 방법을 사용할지 지정하며 프로그램당 1번 사용 가능하다
그러나 예외적으로 그런 기능이 필요한 경우가 있는데, 

예를 들면 library내에서 mp 사용 시, user의 mp.context와 충돌을 방지해야하므로
 multi context를 지원해야한다. 이런 경우에는 mp.get_context()를 이용할 수 있지만, 서로 다른 context의 프로세스 끼리는 서로 호환이 되지 않는다.
"""

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()