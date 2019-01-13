import visdom
import numpy as np 
import math

viz = visdom.Visdom()

# boxplot
X = np.random.rand(100, 2)
X[:, 1] += 2
viz.boxplot(
    X=X,
    opts=dict(legend=['Men', 'Women'])
)

# stemplot
Y = np.linspace(0, 2 * math.pi, 70)
X = np.column_stack((np.sin(Y), np.cos(Y)))
viz.stem(
    X=X,
    Y=Y,
    opts=dict(legend=['Sine', 'Cosine'])
)

# quiver plot
X = np.arange(0, 2.1, .2)
Y = np.arange(0, 2.1, .2)
X = np.broadcast_to(np.expand_dims(X, axis=1), (len(X), len(X)))
Y = np.broadcast_to(np.expand_dims(Y, axis=0), (len(Y), len(Y)))
U = np.multiply(np.cos(X), Y)
V = np.multiply(np.sin(X), Y)
viz.quiver(
    X=U,
    Y=V,
    opts=dict(normalize=0.9),
)