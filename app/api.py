import os
import sys
import random
import json
import face_core.face_class as fc
# API 列表
# 为 Flask Web 框架提供封装的 API 支持
class APIList():
    def __init__(self):
        # 启动人脸数据库（内存）
        self.facedata = fc.FaceData()
        # 启动用户数据库（SQL）
        # SQL 待实现，先用 JSON 替代
        f = open(os.path.join(sys.path[0], 'user_data/users.json'), 'rt')
        self.maindata = json.load(f)
        f.close()
    # API 函数：取得注册用户
    def getRegisterInfo(self, uid = None):
        if(obj == None):
            return json.dumps(self.maindata)
        else:
            return json.dumps({ })
    # API 函数：前端获取到人脸图片交后台程序处理
    # 参数：二进制图片（Blob）
    # 返回：识别结果数据（JSON）
    def faceRecognition(self, img):
        r = self.facedata.recognizeFace(unknown_img_obj = img)
        print(r)
        return json.dumps(r)
#except:
#print("Erroe: in faceRecognition")
#finally:
#return json.dumps(r)
    # API 函数：添加一条数据至用户数据库与人脸数据库
    def addUser(self, u_obj):
        l = [
{ 'uid': '1',
  'name': 'ziheng',
  'age': '20',
  'gender': '男',
  'image': 'blob'
}]
    # 内部函数：随机生成 UID
    # UID：人脸数据库与用户数据库的关联键
    def __random_uid(self):
        seed  = "1234567890"
        seed += "abcdefghijklmnopqrstuvwxyz"
        seed += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        seed += "!@#$%^&*()_+=-"
        sa = [ ]
        salt = ''
        for i in range(8):
            sa.append(random.choice(seed))
            salt = ''.join(sa)
        return salt
# 测试
if __name__ == '__main__':
    pass

