import visdom 
import numpy as np

viz = visdom.Visdom()

#3D 散点图
viz.scatter(
    X=np.random.rand(100, 3),   # 3: 3D
    Y=(np.random.rand(100) + 1.5).astype(int),
    opts=dict(
        legend=['Men', 'Women'],
        markersize=5,
    )
)