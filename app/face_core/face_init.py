import os
import sys
import face_class as fc

try:
    # clean faces data
    face = fc.FaceData(os.path.join(sys.path[0], 'face.data'), 'init')
except:
    print("FaceData status: faild")

