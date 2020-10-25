
import numpy as np
import matplotlib.pyplot as plt

#Simulation goals
#1 make 1d simulation 
#   hope to get general idea of problem and start making design decisions
#2 make 3 dof sim
#   rocket can move in x, y, and rotate about cg
#3 expand to 9 dof
#   

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


    boost_dur = 1.0 #seconds
    boost_f = 80.0 #m/s^2
    #boost_m = 0.2 #kg

    land_ig = 15 #s  time of second ignition
    land_dur = 1.0 #s
    land_f = 80.0 #
    #land_m = 0.2 #kg

    t, h = 0.0, 0.02
    ta, x, v = [0], [0], [0]
    #ta_s, x_s, v_s = [], [], []

    #1.boost 
    print("boost stage at t = 0")
    ta,v,x = run(h, boost_dur, ta, v, x, g, boost_f)
    print("t,v,x : ", ta[-1],v[-1],x[-1])
    

    #2.coast
    
    b_end = ta[-1]
    print("second burn started  at : ", b_end)
    ta,v,x = run(h, land_ig-boost_dur, ta, v, x, g, 0)

    #3.secondary
    l_start = ta[-1]
    print("second burn started  at : ", l_start)
    ta,v,x = run(h, land_dur, ta, v, x, g, land_f)

    #4.land 
    l_end = ta[-1]
    print("run till ground at : ", l_end)
    ta,v,x = run(h, land_dur, ta, v, x, g, 0)

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