import face_core.face_class as fc
import json
import os
import sys

class AppWebAPIList():
    def __init__(self):
        self.facedata = fc.FaceData()
        self.maindata = [
        { 'uid': '1',
          'name': 'ziheng',
          'age': '20',
          'gender': '男',
          'image': 'addr'
        },
         {'uid': '2',
          'name': 'zihengCat',
          'age': '18',
          'gender': '女',
          'image': 'addr'
        }]
    def getRegisterInfo(self, obj = None):
        if(obj == None):
            return json.dumps(self.maindata)
        else:
            return json.dumps({ })

    def faceRecognition(self, img):
        r = ""
        #p = os.path.join(sys.path[0], 'face_location_temp/' + img_name)
        r = json.dumps(self.facedata.recognizeFace(unknown_img_obj = img))
        return r

if __name__ == '__main__':
    pass

