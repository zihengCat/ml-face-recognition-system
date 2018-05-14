import flask as f
app = f.Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if f.request.method == 'GET':
        return f.render_template('login.tpl')
    if f.request.method == 'POST':
        if f.request.form['username'] == 'admin' and f.request.form['password'] == 'admin':
            return f.render_template('user.tpl', name = f.request.form['username'])
        else:
            return '<h1>登录失败：用户名或密码错误</h1>'


@app.route('/u/<username>')
def username(username):
    return f.render_template('user.tpl', name=username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2333', debug=True)

