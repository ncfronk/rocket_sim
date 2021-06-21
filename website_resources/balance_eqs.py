# this is a simple kinimatics balance set

#start with energy going up
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

import engines as eng

#maximum_mass = eng.estes_d12_3.max_lift_weight
maximum_mass = (eng.estes_d12_3.max_lift_weight)

    land_dur = rocket_sample.land_engine.thrust_duration #s
    land_m = rocket_sample.current_mass
    land_avg_thrust = rocket_sample.land_engine.total_impulse/land_dur
    land_f = land_avg_thrust/land_m #

