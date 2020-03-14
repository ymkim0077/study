import simpy 
import numpy as np 

def business_process(env, activity_lst):
    while True:
        for act in activity_lst:
            ## activity의 수행 시간은 triangulat dist를 따르며, 
            print('start {} at {:6.2f}'.format(act, env.now))
            activity_time = np.random.triangular(left=3, right=10, mode=7)
            yield env.timeout(activity_time)
            print('end   {} at {:6.2f}'.format(act, env.now))
            
            ## activity를 transfer하는데 일정 시간이 소요된다고 가정함.
            activity_transfer_time = np.random.triangular(left=1, right=3, mode=2)
            yield env.timeout(activity_transfer_time)
        print("#"*30)
        print("process end")
        ## 만약 여기 return 을 넣으면 여기서 generator가 그대로 종료됨 
        ## 만약 n 번 수행하고 싶다면, while True 를 for 문으로 변경하고, 몇 번 종료 후 끝내는 형태로 해도 괜찮을듯. 
        return 'over'

## environment setting
env = simpy.Environment()

bp1 = business_process(env, activity_lst=[ "activity_{}".format(i) for i in range(1, 6)])
env.process(bp1)

env.run(until=100)