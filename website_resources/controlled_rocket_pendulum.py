import numpy as np
import cv2

from InvertedPendulum import InvertedPendulum

from scipy.integrate import solve_ivp

import matplotlib.pyplot as plt 
import matplotlib.animation as animation 


def u(t):
    duration = 1.6
    t1 = 3.
    t2 = t1 + duration

    motor_acc = 30.0

    if(t > t1 and t < t2):
        return motor_acc
    else:
        return 0.

# Pendulum and cart system. The motors on the cart turned at fixed time. In other words
# The motors are actuated to deliver forward x force from t=t1 to t=t2.
# Y : [ theta, theta_dot, phi]


def func3(t, y):
    g = 9.8  # Gravitational Acceleration
    L = 1.5  # Length of pendulum

    m = 1.0  # mass of pend (kg)

    theta_ddot = -g/L * np.cos(y[0]) + np.sin(y[2])*u(t)

    damping_theta = - 1*y[1]

    phi_dot = 0

    return [y[1], theta_ddot + damping_theta, phi_dot]


# Both cart and the pendulum can move.
if __name__ == "__main__":

    sol = solve_ivp(func3, [0, 20], [np.pi/2 - 0.1, 0.,
                    np.pi/2],   t_eval=np.linspace(0, 20, 300))

    syst = InvertedPendulum()

    for i, t in enumerate(sol.t):
        rendered = syst.step([sol.y[0, i], sol.y[1, i], sol.y[2, i]], t)
        cv2.imshow('im', rendered)
        cv2.moveWindow('im', 100, 100)

        if cv2.waitKey(30) == ord('q'):
            break

