import os
import sys
import face_class as fc

#face = fc.FaceData('./face.data', "init")
#face.addFace("obama", './tests/obama_default.jpg')
#face.addFace("obama1", './tests/obama_default.jpg')
#face.addFace("obama2", './tests/obama_t1.jpg')

face = fc.FaceData(os.path.join(sys.path[0], 'face.data'))
#face.addFace("obama2", './tests/obama_default.jpg')
#face.showFace()
face.recognizeFace(os.path.join(sys.path[0], 'tests/obama_t1.jpg'))

