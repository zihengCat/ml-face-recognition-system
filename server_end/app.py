import json
import flask as f
import api

# Create App
app = f.Flask(__name__)

# Using API List
i = api.APIList()

####################
### RESTful APIs ###
####################

## For CORS
@app.after_request
def do_after_request(response):
    #response.headers.add('Access-Control-Allow-Origin', '*')
    #response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    #response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

## Face Recognition
@app.route('/image', methods = ['POST'])
def do_image():
    # get the image
    image_file = f.request.files['image']
    #print(image_file)
    return i.faceRecognition(image_file)

## Get Register Info
@app.route('/get/register', methods = ['GET', 'POST'])
def do_get_register():
    return i.getRegisterInfo()

## Add a new User to database
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
@app.route('/put/user', methods = ['POST'])
def do_put_user():
    obj = {
        # 人脸图片（二进制图片数据）
        "image":  f.request.files['image'],
        # 姓名
        "name":   f.request.form['uname'],
        # 年龄
        "age":    f.request.form['age'],
        # 性别
        "gender": "男" if(f.request.form['gender'] == 'male') else "女"
    }
    if(i.addUser(obj) == 0):
        return f.Response('{"status":"ok"}', mimetype="text/json")
    else:
        return f.Response('{"status":"fail"}', mimetype="text/json")

####################
### Pages Router ###
####################

## Index Page
@app.route('/', methods=['GET'])
def do_index():
    return f.redirect(f.url_for('do_login'))

## Login Page
@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if f.request.method == 'GET':
        return f.render_template('login.tpl')
    if f.request.method == 'POST':
        if f.request.form['username'] == 'admin' and f.request.form['password'] == 'admin':
            return f.redirect('/welcome')
        elif f.request.form['username'] == 'user' and f.request.form['password'] == 'user':
            return f.render_template('user.tpl', name = f.request.form['username'])
        else:
            return f.render_template('login.tpl')

## Welcome Page
@app.route('/welcome', methods=['GET', 'POST'])
def do_welcome():
    return f.render_template('welcome.tpl')

## Dashboard Page
@app.route('/dashboard', methods=['GET', 'POST'])
def do_dashboard():
    return f.render_template('dashboard.tpl')

## Registers Page
@app.route('/registers', methods=['GET', 'POST'])
def do_registers():
    return f.render_template('registers.tpl')


## Useradd Page
@app.route('/useradd', methods=['GET', 'POST'])
def do_useradd():
    return f.render_template('useradd.tpl')


@app.route('/video')
def do_video():
    return f.Response(open('./templates/video.html').read(), mimetype="text/html")

@app.route('/pistream')
def do_pistream():
    return f.render_template('pistream.tpl', ip_port='192.168.1.103:8084')


@app.route('/u/<username>')
def username(username):
    return f.render_template('user.tpl', name=username)


if __name__ == '__main__':
    #print(app.url_map)
    app.run(host='0.0.0.0', port='2333', debug=True)

