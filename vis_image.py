import visdom 
import numpy as np

viz = visdom.Visdom()
assert viz.check_connection()

#单张
viz.image(
    np.random.rand(3, 512, 256),
    opts=dict(title='Random!', caption='How random.'),
)
#多张
viz.images(
    np.random.randn(20, 3, 64, 64),
    opts=dict(title='Random images', caption='How random.')
)