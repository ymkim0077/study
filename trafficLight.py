import simpy

def main():
    env = simpy.Environment()
    env.process(traffic_light(env))
    env.run(until=120)
    print("Simulation complete.")

def traffic_light(env):
    while True:
        print("Light turned Green at t= "+str(env.now))
        yield env.timeout(30)
        print("Light turned Yellow at t="+str(env.now))
        yield env.timeout(5)
        print("Light turned Red at t="+str(env.now))
        yield env.timeout(20)

if __name__ == '__main__':
    main()

