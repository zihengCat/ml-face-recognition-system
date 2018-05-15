<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>Signin Template for Bootstrap</title>
    <!-- Bootstrap core CSS -->
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
     <!-- Custom styles for this template -->
     <link href="{{ url_for('static', filename='signin.css') }}" rel="stylesheet">
  </head>
  <body>
    <div class="container">

      <form action="/login" method="POST" class="form-signin">
        <h2 class="form-signin-heading">登录页</h2>
        <label for="inputEmail" class="sr-only">账号</label>
        <input name="username" type="text" id="inputEmail" class="form-control" placeholder="Account" required autofocus>
        <label for="inputPassword" class="sr-only">密码</label>
        <input name="password" type="password" id="inputPassword" class="form-control" placeholder="Password" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> 记住我
          </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">登录</button>
      </form>
    </div> <!-- /container -->
  </body>
</html>
