from multiprocessing import Process, Pipe
import time


#Pipe() 함수는 파이프로 연결된 한 쌍의 연결 객체를 돌려주는데 기본적으로 양방향(duplex)이다.
def send_function(conn_send, function_name):
    conn_send.send(["hello??", function_name, ])
    conn_send.close()


def receive_functin(conn, function_name):
    #받아오지 못할경우 recv() 사용 시 에러뜸 그걸위한 익셉션
    try:
        print([conn.recv(), function_name])
    except Exception as ex:
        print(122)
        print (ex)
    time.sleep(1)

    try:
        print([conn.recv(), function_name])
    except Exception as ex:
        print (ex)
    print(1223)

if __name__ == '__main__':
    #Pipe()함수가 반환하는 객체는 시작과 끝을 의미한다 즉 반드시 2개의 값이 있어야 한다.?
    #1개로 읽고 쓰려고하면 데이터의 손실을 야기할수있다.*****
    parent_conn, child_conn = Pipe()
    #이렇게 한개만 있으면 어떤 결과를 의미할까?
    test_conn = Pipe()


    p = Process(target=send_function, args=(child_conn, "wook", ))
    p2 = Process(target=receive_functin, args=(parent_conn, "sang", ))
    
    p2.start()
    time.sleep(0.5)
    p.start()
    
    
    p.join()
    p2.join()
    print("process end")