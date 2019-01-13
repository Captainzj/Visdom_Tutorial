from visdom import Visdom
import numpy as np

viz = Visdom()

try:
    import matplotlib.pyplot as plt
    plt.plot([1, 23, 2, 10, 4])
    plt.ylabel('some numbers')
    viz.matplot(plt)
except BaseException as err:
    print('Skipped matplotlib example')
    print('Error message: ', err)