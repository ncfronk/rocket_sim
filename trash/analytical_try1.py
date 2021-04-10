import numpy as np
import matplotlib as mp
import scipy as sp





time = 1.1
acceleration = 5.19
initialVelocity = -25


displacement = initialVelocity*time + 0.5*acceleration*time*time
print("Here is displacement: " + str(displacement))