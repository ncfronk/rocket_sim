
import numpy as np
import matplotlib.pyplot as plt
from engines import *

#Simulation goals
#1 make 1d simulation 
#   hope to get general idea of problem and start making design decisions
#2 make 3 dof sim
#   rocket can move in x, y, and rotate about cg
#3 expand to 9 dof
#   

estes_b4_2 = estes_rocket_def(name="B4-2",total_impulse=5.0,time_delay=2.0,max_lift_weight=0.113,total_mass=0.0198,propellant_mass=0.00833,thrust_duration=1.1)
estes_c6_3 = estes_rocket_def(name="C4-3",total_impulse=10.0,time_delay=3.0,max_lift_weight=0.113,total_mass=0.0258,propellant_mass=0.01248,thrust_duration=1.6)

estes_d12_4 = estes_rocket_def(name="D12-0",total_impulse=20.0,time_delay=4,max_lift_weight=0.396,total_mass=(0.043),propellant_mass=0.02493,thrust_duration=1.6)

ejected_mass = 0.107 #kg

rocket_body = body_properties(width=0.005,heigth=0.060,cg=0.030,cp=0.010,mass=0.3)

rocket_sample = rocket(launch_engine=estes_d12_4,land_engine=estes_c6_3,body_properties=rocket_body)
 

#Faero = 
#xdot = (fthrust + fgrav)/mass 
# is altitude
def eq( v0, x0, g, f, t):
    a_t = (g+f)
    x = v0*t + a_t*t*t/2.0 + x0
    v = v0 + a_t*t
    return [x, v]

def run(h, t_end, t_l, v_l, x_l, g, f):
    t0 = t_l[-1]
    v0 = v_l[-1]
    x0 = x_l[-1]

    t = 0
    while t <= t_end:
        x_t, v_t = eq(v0,x0,g,f,t)

        t_l.append(t + t0)
        v_l.append(v_t)
        x_l.append(x_t)

        t = t + h
        if x_t < 0:
            break
    #print("run finished with t, x, v : ", ta[-1], x[-1], v[-1])


    return  t_l,v_l,x_l

def plot(t):
    #variables
    g = -9.8 #m/s


    boost_dur = rocket_sample.launch_engine.thrust_duration #1.0 #seconds
    boost_m = rocket_sample.current_mass #kg
    avg_thrust = (rocket_sample.launch_engine.total_impulse/boost_dur) #N== kg m/s^2
    boost_f = avg_thrust/(boost_m)  #80.0 #m/s^2


    land_ig = 9.25 #s  time of second ignition
    #

    t, h = 0.0, 0.02
    ta, x, v = [0], [0], [0]
    #ta_s, x_s, v_s = [], [], []

    #1.boost 
    print("boost stage at t = 0")
    
    print("boost : ", boost_f)
    ta,v,x = run(h, boost_dur, ta, v, x, g, boost_f)
    print("t,v,x : ", ta[-1],v[-1],x[-1])
    
    v_max = np.max(v)
    ## now subtract mass of motor\

    rocket_sample.current_mass = rocket_sample.current_mass - (rocket_sample.launch_engine.total_mass + ejected_mass) ## this is a point where we could lose more masss, will explain in 1 sec

    #2.coast
    
    b_end = ta[-1]
    print("second burn started  at : ", b_end)
    ta,v,x = run(h, land_ig-boost_dur, ta, v, x, g, 0)

    
    land_dur = rocket_sample.land_engine.thrust_duration #s
    land_m = rocket_sample.current_mass
    land_avg_thrust = rocket_sample.land_engine.total_impulse/land_dur
    land_f = land_avg_thrust/land_m #
    #land_m = 0.2 #kg

    #3.secondary
    print("boost : ", land_f)
    l_start = ta[-1]
    print("second burn started  at : ", l_start)
    ta,v,x = run(h, land_dur, ta, v, x, g, land_f)

    #4. coast to land 
    l_end = ta[-1]
    print("run till ground at : ", l_end)
    ta,v,x = run(h, 1000, ta, v, x, g, 0)

    stop = ta[-1]


    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(ta,x, '--')
    plt.xlabel('t(s)')
    plt.ylabel('x(m)')

    plt.axvline(b_end)
    plt.axvline(l_start)
    plt.axvline(l_end)
    plt.axvline(stop)
    
    

    plt.subplot(2,1,2)
    plt.plot(ta,v, '--')
    plt.xlabel('t(s)')
    plt.ylabel('v(m/s)')
    plt.show()

plot(5.0)