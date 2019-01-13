import visdom
import os.path
import getpass
import numpy as np
from six.moves import urllib
from sys import platform as _platform


viz = visdom.Visdom()

try:
    # # video demo: download video from http://media.w3.org/2010/05/sintel/trailer.ogv
    # video_url = 'http://media.w3.org/2010/05/sintel/trailer.ogv'
    # # linux
    # if _platform == "linux" or _platform == "linux2":
    #     videofile = '/home/%s/trailer.ogv' % getpass.getuser()
    # # MAC OS X
    # elif _platform == "darwin":
    #     videofile = '/Users/%s/Desktop/trailer.ogv' % getpass.getuser()
    # # download video
    # urllib.request.urlretrieve(video_url, videofile)
    
    videofile = '/Users/%s/Desktop/trailer.ogv' % getpass.getuser()
    if os.path.isfile(videofile):
        viz.video(videofile=videofile)
except ImportError:
    print('Skipped video example')


