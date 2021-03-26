import time
import multiprocessing

def innerLoop(i_num):
    for j in range(0, 10):
        time.sleep(delay_time)
        print(str(i_num) + " : " + str(j) + " \n")


star_time = time.time()
delay_time = 1.0






#print("nowTime : %s" % (time.time() - star_time))
#time.sleep(3)
#print(123)

#

if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=5)
    pool.map(innerLoop, range(0,10) )

    #normal case 
    """
    for i in range(1, 100):
        for j in range(1, 100):
            time.sleep(delay_time)
            print(str(i) + " : " +str(j))
    """


    print("nowTime : %s" % (time.time() - star_time))
    