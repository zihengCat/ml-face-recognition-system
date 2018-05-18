import os
import sys
import random
import json
import face_core.face_class as fc
# API 列表
# 为 Flask Web 框架与 CLI 命令行工具提供封装的 API 支持
# 用户主数据格式 =>
#{
#    "uid": {
#        "name": "吕子恒",
#        "age": "20",
#        "gender": "男"
#    },
#    ...
#}
class APIList():
    def __init__(self):
        # 启动人脸数据库（内存）
        self.facedata = fc.FaceData()
        # 启动用户数据库（SQL）
        ## SQL 待实现，先用 JSON 替代
        # 数据库地址
        self.datapath = os.path.join(sys.path[0], 'user_data/users.json')
        # 存盘指示器
        self.saver = 0
        # 用户信息数据库
        f = open(self.datapath, 'rt')
        self.maindata = json.load(f)
        f.close()
    # API析构函数：数据落盘
    def dataSaver(self):
        if(self.saver == 1):
            f = open(self.datapath, 'wt')
            json.dump(self.maindata, f)
            f.close()
            # 通知人脸数据库也执行存盘操作
            self.facedata.dataClose()
            print("Data saved OK")
        else:
            print("in users database: Nothing to do")

    # API 函数：取得注册用户信息
    # 参数：用户UID
    # 返回：目标用户信息（不指定UID则获取全部用户信息）
    def getRegisterInfo(self, uid = None):
        if(uid == None):
            return json.dumps(self.maindata)
        else:
            return json.dumps(self.maindata[uid])

    # API 函数：前端获取到人脸图片交后台程序处理
    # 参数：二进制图片（Blob）
    # 返回：识别结果数据（JSON）
    def faceRecognition(self, img_obj):
        r = { }
        r = self.facedata.recognizeFace(unknown_img_obj = img_obj)
        #print(r)
        try:
            if(r['uid'] != 'unknown' and r['uid'] != 'noface'):
                u = r
                u_info = self.maindata[r['uid']]
                u.update({'info': u_info})
                return json.dumps(u)
            else:
                return json.dumps(r)
        except:
            return json.dumps(r)

    # API 函数：读取本地人脸图片交后台程序处理
    # 参数：本地图片路径（String）
    # 返回：识别结果数据（JSON）
    def cliFaceRecognition(self, img_path):
        r = { }
        # 读取本地图片
        r = self.facedata.recognizeFace(unknown_img_path = img_path)
        #print(r)
        try:
            if(r['uid'] != 'unknown' and r['uid'] != 'noface'):
                u = r
                u_info = self.maindata[r['uid']]
                u.update({'info': u_info})
                # 问好
                if(True):
                    name = u_info['name']
                    ext = '先生' if (u_info['gender'] == '男') else '女士'
                    words = '很高兴遇见你，'
                    words = words + name + ext
                    cmd = 'ssh ziheng@10.211.55.14 ' + "'say " + words + "'"
                    print(cmd)
                    os.system(cmd)
                return json.dumps(r)
            elif(r['uid'] == 'unknown'):
                if(True):
                    words = '您好，本系统目前还不认识您，您可以尝试录入信息'
                    cmd = 'ssh ziheng@10.211.55.14 ' + "'say " + words + "'"
                    print(cmd)
                    os.system(cmd)
            return json.dumps(r)
        except:
            return json.dumps(r)

    # API 函数：添加一条数据至用户数据库与人脸数据库
    # 参数：user_obj
    # 返回：无
    # user_obj（可由Web前端传递） =>
    # {
    #    "image": img_obj,
    #    "name": "",
    #    "age": "",
    #    "gender": ""
    # }
    def addUser(self, user_obj, img_name = None):
        uid = self.__random_uid();
        new_user = {
            uid: {
                'name':    user_obj['name'],
                'age':     user_obj['age'],
                'gender':  user_obj['gender']
            }
        }
        # 加入新数据至用户信息数据库
        self.maindata.update(new_user)
        self.saver = 1
        # 加入新数据至用户人脸数据库
        if(img_name != None):
            # CLI命令行接口
            p = os.path.join(sys.path[0], 'face_core/face_images/' + img_name)
            self.facedata.addFace(uid, img_path = p)
        else:
            # Web前端接口
            self.facedata.addFace(uid, img_obj= user_obj['image'])
        # 数据落盘
        self.dataSaver()
        # 正常返回
        return 0

    def delUser(self, userid):
        if(userid == "all"):
            # 清空数据
            self.maindata = { }
        else:
            # 删除目标数据
            self.maindata.pop(userid)
        # 通知人脸数据库执行相同操作
        self.facedata.delFace(uid = userid)
        # 设置存盘指示器
        self.saver = 1
        # 数据存盘
        self.dataSaver()

    # API 函数：显示数据至终端
    def showUser(self, uid = "all"):
        if(uid == "all"):
            print(self.maindata)
        else:
            print(self.maindata[uid])

    def __random_uid(self):
        seed  = "1234567890"
        seed += "abcdefghijklmnopqrstuvwxyz"
        seed += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # 不使用特殊字符
        #seed += "!@#$%^&*()_+=-"
        sa = [ ]
        salt = ''
        for i in range(8):
            sa.append(random.choice(seed))
            salt = ''.join(sa)
        return salt

