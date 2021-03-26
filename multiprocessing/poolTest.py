#멀티프로세싱 pool 기능 실험해보기
#20210326 swyoo
##################################

import time
import multiprocessing

from functools import partial

def innerLoop(userName, dictionOrd, i_num):
    for j in range(0, 10):
        time.sleep(delay_time)
        print(userName + str(i_num) + " : " + str(j) + " \n")


star_time = time.time()
delay_time = 1.0






#main에서 시작되지 않으면 pool은 작동하지 않는다
if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=5)

    #partial을 통하여 함수에 미리 변수를 채워둔다
    func = partial(innerLoop, "hello? : ", {"abc":123, "def":456})
    pool.map(func, range(0,10))

    #normal case 
    """
    for i in range(1, 100):
        for j in range(1, 100):
            time.sleep(delay_time)
            print(str(i) + " : " +str(j))
    """


    print("nowTime : %s" % (time.time() - star_time))
    