import visdom 
import numpy as np

viz = visdom.Visdom()

## 通过update='new'添加新散点
import time
win = viz.scatter(
    X=np.random.rand(255, 2),
    opts=dict(
        markersize=5,
        markercolor=np.random.randint(0, 255, (255, 3,)),
    ),
)

# 判断窗口是否存在
assert viz.win_exists(win), 'Created window marked as not existing'
time.sleep(2)

# 向散点图中加入新的描述
viz.scatter(
    X=np.random.rand(255),
    Y=np.random.rand(255),
    win=win,
    name='new_trace',
    update='new'
)