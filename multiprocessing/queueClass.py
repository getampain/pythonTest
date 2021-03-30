#프로세스간의 자원 공유 방법중 하나인 큐를 사용한 방법


import time
from multiprocessing import Process, Queue

def f(q, now_user):

    #큐를 입력하며 put으로 입력한다
    q.put([42, None, 'hello', now_user])
    q.put([30, None, 'hello world', now_user])
    q.put([12, None, 'hello heaven', now_user])
    time.sleep(10)



if __name__ == '__main__':

    #정보를 공유할 큐를 생성해준다 큐는 fifo 형태를 원칙으로 한다
    q = Queue()

    #프로세스를 만들 때 생성한 큐를 넣어준다.
    p = Process(target=f, args=(q, "amy", ))
    p2 = Process(target=f, args=(q, "bob", ))


    p.start()
    p2.start()

    #데이터를 가지고 올땐 get을 통하여 입력한것을 가지고 오며 먼저 입력한 값이 먼저 나온다
    print(q.get())    # prints "[42, None, 'hello']"
    print(q.get())    # prints "[42, None, 'hello']"
    print(q.get())    # prints "[42, None, 'hello']"
    print(q.get())    # prints "[42, None, 'hello']"
    print(q.get())    # prints "[42, None, 'hello']"
    print(q.get())    # prints "[42, None, 'hello']"
    
    p.join()
    p2.join()
    
    print("mp end!")