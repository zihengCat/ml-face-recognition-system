import os
import sys
import face_class as fc

try:
    #face = fc.FaceData(os.path.join(sys.path[0], 'face.data'), 'init')
    # Open data as normal
    face = fc.FaceData(os.path.join(sys.path[0], 'face.data'))
    face.showFace()
except:
    print("FaceData status: faild")

