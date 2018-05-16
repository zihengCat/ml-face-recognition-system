import json
import flask as f
import api

# Create App
app = f.Flask(__name__)
# Using API List
i = api.APIList()

# RESTful APIs

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
    try:
        # get the image
        image_file = f.request.files['image']
        #print(image_file)
        return i.faceRecognition(image_file)
    except:
        print('Error: in POST /image')

## Get Register Info
@app.route('/get/register', methods = ['GET', 'POST'])
def do_get_register():
    return i.getRegisterInfo()

# Pages Router

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
            return f.render_template('main.tpl')
        elif f.request.form['username'] == 'user' and f.request.form['password'] == 'user':
            return f.render_template('user.tpl', name = f.request.form['username'])
        else:
            return f.render_template('login.tpl')

@app.route('/video')
def do_video():
    return f.Response(open('./templates/video.html').read(), mimetype="text/html")

@app.route('/u/<username>')
def username(username):
    return f.render_template('user.tpl', name=username)


if __name__ == '__main__':
    #print(app.url_map)
    app.run(host='0.0.0.0', port='2333', debug=True)

