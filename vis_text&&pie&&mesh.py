import visdom
import numpy as np 

viz = visdom.Visdom()

# text window with Callbacks
txt = 'This is a write demo notepad. Type below. Delete clears text:<br>'
callback_text_window = viz.text(txt)

# pie chart
X = np.asarray([19, 26, 55])
viz.pie(
X=X,
opts=dict(legend=['Residential', 'Non-Residential', 'Utility'])
)

# mesh plot
x = [0, 0, 1, 1, 0, 0, 1, 1]
y = [0, 1, 1, 0, 0, 1, 1, 0]
z = [0, 0, 0, 0, 1, 1, 1, 1]
X = np.c_[x, y, z]
i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6]
Y = np.c_[i, j, k]
viz.mesh(X=X, Y=Y, opts=dict(opacity=0.5))