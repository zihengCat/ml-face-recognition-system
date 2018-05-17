import os
import sys
import api

# 使用 API List
i = api.APIList()

# 添加用户
# API 函数：添加一条数据段至用户信息数据库与用户人脸数据库
# user_obj（前端传递） =>
# {
#    "image": img_obj,
#    "name": "",
#    "age": "",
#    "gender": ""
# }
# 接口 => addUser(self, user_obj, img_name = None):
# 注：img_name图片必须存在于 face_core/face_images 下

if __name__ == '__main__':
    # 显示数据
    if(len(sys.argv) < 2):
        print("Error: too few argument")
    elif(sys.argv[1] == "show" and len(sys.argv) == 3):
        i.showUser(sys.argv[2])
    elif(sys.argv[1] == "show" and len(sys.argv) == 2):
        i.showUser("all")
    # 添加数据
    elif(sys.argv[1] == "add" and len(sys.argv) == 3):
        pic_name = sys.argv[2]
        new_user = {
           "image": pic_name,
           "name": "奥巴马同学",
           "age": "56",
           "gender": "男"
        }
        #def addUser(self, user_obj, img_name = None):
        i.addUser(user_obj = new_user, img_name = pic_name)
    # 删除数据
    elif(sys.argv[1] == "delete" and len(sys.argv) == 3):
        i.delUser(userid = sys.argv[2])
    elif(sys.argv[1] == "clean" and len(sys.argv) == 2):
        i.delUser(userid = 'all')
    else:
        print("Error: argument does not fit")

