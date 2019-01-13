import visdom 
import numpy as np

viz = visdom.Visdom()

# 2D散点图,分配不同颜色
viz.scatter(
    X=np.random.rand(255, 2),  # 2: 2D
    #随机指定1或者2
    Y=(np.random.rand(255) + 1.5).astype(int),
    opts=dict(
        markersize=10,
        ## 分配两种颜色
        markercolor=np.random.randint(0, 255, (2, 3,)),
    ),
)