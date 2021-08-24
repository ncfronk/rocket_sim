import os
import numpy as np
import matplotlib.pyplot as plt
import imageio

y = np.random.randint(30, 40, size=(40))
filenames = []
for i in y:
    # plot the line chart
    plt.plot(y[:i])
    plt.ylim(20,50)
    
    # create file name and append it to a list
    filename = f'{i}.png'
    filenames.append(filename)
    
    # save frame
    plt.savefig(filename)
    plt.close()
# build gif
with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        
# Remove files
for filename in set(filenames):
    os.remove(filename)