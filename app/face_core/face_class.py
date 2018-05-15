import os
import sys
import pickle
import numpy as np
import PIL as pil
import face_recognition
# 内部数据结构: 键值对 =>
# {
#  "id_1": np.ndarray,
#  "id_2": np.ndarray,
#  "id_3": np.ndarray,
#   ...
#  "id_N": np.ndarray
# }
class FaceData():
    # 构造函数：初始化
    def __init__(self, path = './face_core/face.data', flag = None):
        # 存盘指示器（析构函数通过该值判断是否要重新保存数据）
        # 0 => 操作不改变数据（查询）
        # 1 => 操作改变了数据（增删）
        self.counter = 0
        # 数据路径
        self.face_data_path = os.path.join(sys.path[0], path)
        # 初始化（清空）
        if(flag == "init"):
            self.face_data = { }
            self.counter = 1
        # 初始化（正常启动）
        else:
            try:
                # 人脸数据库（二进制存取）
                f = open(self.face_data_path, 'rb')
                self.face_data = pickle.load(f)
                f.close()
            except:
                f.close()
                raise "Error: open face.data failed or unknown format"
    # 析构函数：通过指示器判断是否要重新保存数据
    def __del__(self):
        if(self.counter == 1):
            self.__updateFace()
        else:
            pass
    # API 函数：人脸识别
    # 参数：图片路径或图片二进制数据
    # 返回：人脸数据库中目标UID与目标人脸框（前端显示）
    def recognizeFace(self, unknown_img_path = None, unknown_img_obj = None):
        unknown_image = None
        # 不同参数 => 不同处理方式
        if(unknown_img_path != None and unknown_img_obj == None):
            unknown_image = face_recognition.load_image_file(unknown_img_path)
        elif(unknown_img_path == None and unknown_img_obj != None):
            unknown_image = pil.Image.open(unknown_img_obj)
            # 'RGB' (8-bit RGB, 3 channels) or 'L' (black and white)
            unknown_image = unknown_image.convert('RGB')
            unknown_image = np.array(unknown_image)
        else:
            raise "Error: face_class -> recognizeFace"
        # 返回数据格式 => 列表（List）
        unknown_encoding = face_recognition.face_encodings(unknown_image)
        # 设置单一人脸识别限制
        if(len(unknown_encoding) == 1):
            # 核查目标人脸是否在数据库中（注册用户 or 陌生人）
            face_name = self.__checkFaceEncoding(unknown_encoding[0])
            if(face_name != None):
                face_locations = face_recognition.face_locations(unknown_image)
                for ((top, right, bottom, left), name) in zip(face_locations, face_name):
                    return  {
                        'uid': name,
                        'locations': {
                            'tops': top,
                            'right': right,
                            'bottom': bottom,
                            'left': left
                        }
                    }
    # API 函数：查询人脸数据库中的注册信息
    # 参数：UID
    # 返回：
    def showFace(self, uid = None):
        if(uid == None):
            print(self.face_data);
        else:
            print(self.face_data[uid]);
    # API 函数：添加人脸数据
    def addFace(self, uid, img_path):
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)[0]
        add_data = {
            img_id: encoding
        }
        # 加入新数据
        self.face_data.update(add_data)
        # 设触发器（保存数据）
        self.counter = 1
    # API 函数：删除人脸数据
    def delFace(self, uid):
        # 删除已有数据
        face_data.pop(uid)
        # 设触发器（保存数据）
        self.counter = 1
    # API函数：清空人脸数据
    #def cleanFace(self, flag = None):
    #    self.face_data = { }
    #    self.counter = 1

    # 内部函数：人脸比对
    # 计算两个特征矩阵的欧几里得距离 d
    # 当 d < 0.6 时, 认为是同一个人
    # 返回 None 说明不匹配（陌生人）
    def __checkFaceEncoding(self, enc):
        # 时间复杂度 O(n)
        for k in self.face_data:
            d = np.linalg.norm(self.face_data[k] - enc)
            if(d < 0.6):
                return k
        return None
    # 内部函数：数据落盘
    def __updateFace(self):
        f = open(self.face_data_path, 'wb')
        pickle.dump(self.face_data, f)
        f.close()

