import face_recognition
import numpy as np
import pickle
# 数据结构: 键值对 =>
# {
#  "id_1": np.ndarray,
#  "id_2": np.ndarray,
#  "id_3": np.ndarray,
#   ...
#  "id_N": np.ndarray
# }
class FaceData():
    # 构造函数：初始化
    def __init__(self, path, flag = None):
        # 存盘指示器（析构函数通过该值判断是否要重新保存数据）
        # 0 => 操作不改变数据（查询）
        # 1 => 操作改变了数据（增删）
        self.counter = 0
        # 数据路径
        self.face_data_path = path
        # 初始化（清空）
        if(flag == "init"):
            self.face_data = { }
            self.counter = 1
        # 初始化（正常启动）
        else:
            try:
                f = open(self.face_data_path, 'rb')
                self.face_data = pickle.load(f)
                f.close()
            except:
                f.close()
                raise "Error: open file failed or unknow format"
    # 析构函数：通过指示器判断是否要重新保存数据
    def __del__(self):
        if(self.counter == 1):
            self.__updateFace()
        else:
            pass
    # API函数：人脸识别
    # 可优化项：图片
    def recognizeFace(self, unknown_img_path):
        unknown_image = face_recognition.load_image_file(unknown_img_path)
        # 列表（List）
        unknown_encoding = face_recognition.face_encodings(unknown_image)
        if(len(unknown_encoding) != 1):
            raise "Error: recognize face image does not fit"
        self.__checkFaceEncoding(unknown_encoding[0])

    # API函数：查询人脸数据
    def showFace(self, img_id = None):
        if(img_id == None):
            print(self.face_data);
        else:
            print(self.face_data[img_id]);
    # API函数：添加人脸数据
    def addFace(self, img_id, img_path):
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)[0]
        add_data = {
            img_id: encoding
        }
        self.face_data.update(add_data)
        self.counter = 1
    # API函数：删除人脸数据
    def delFace(self, img_id):
        face_data.pop(img_id)
        self.counter = 1
    # API函数：清空人脸数据
    def cleanFace(self, flag = None):
        self.face_data = { }
        self.counter = 1

    # 内部函数：人脸比对
    # 计算两个特征矩阵的欧几里得距离 d
    # 当 d < 0.6 时, 认为是同一个人
    def __checkFaceEncoding(self, enc):
        for k in self.face_data:
            d = np.linalg.norm(self.face_data[k] - enc)
            if(d < 0.6):
                print("Found: %s" % k)
                return
        print("Not Found")

    # 内部函数：存盘
    def __updateFace(self):
        f = open(self.face_data_path, 'wb')
        pickle.dump(self.face_data, f)
        f.close()

