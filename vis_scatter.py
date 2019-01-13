import visdom 
import numpy as np

viz = visdom.Visdom()

#画出随机的散点图
import time
Y = np.random.rand(100)
old_scatter = viz.scatter(
    X=np.random.rand(100, 2),
    Y=(Y[Y > 0] + 1.5).astype(int),
    opts=dict(
        legend=['Didnt', 'Update'],
        xtickmin=-50,
        xtickmax=50,
        xtickstep=50,
        ytickmin=-50,
        ytickmax=50,
        ytickstep=20,
        markersymbol='cross-thin-open',
    ),
)

time.sleep(5)

#对窗口进行更新,包括标注,坐标,样式等
viz.update_window_opts(
    win=old_scatter,
    opts=dict(
        legend=['Apples', 'Pears'],
        xtickmin=0,
        xtickmax=1,
        xtickstep=0.5,
        ytickmin=0,
        ytickmax=1,
        ytickstep=0.5,
        markersymbol='cross-thin-open',
    ),
)
