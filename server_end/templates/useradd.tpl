{% extends 'base.tpl' %}

{% block title %}
    <title>添加用户</title>
{% endblock %}

{% block head %}
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">
  <link rel="stylesheet" type="text/css"
        href="{{ url_for('static', filename='assets/css/bootstrap-clearmin.min.css')}}"
  >
  <link rel="stylesheet" type="text/css"
        href="{{ url_for('static', filename='assets/css/font-awesome.min.css')}}"
  >
  <link rel="stylesheet" type="text/css"
        href="{{ url_for('static', filename='assets/css/roboto.css')}}"
  >
  <link rel="stylesheet" type="text/css"
        href="{{ url_for('static', filename='assets/css/material-design.css')}}"
  >
  <link rel="stylesheet" type="text/css"
        href="{{ url_for('static', filename='assets/css/small-n-flat.css')}}"
  >
</head>
{% endblock %}
{% block body %}
<body class="cm-no-transition cm-1-navbar">
    <div id="cm-menu">
      <nav class="cm-navbar cm-navbar-primary">
        <div class="cm-flex"><h1>LOGO</h1></div>
        <div class="btn btn-primary md-menu-white" data-toggle="cm-menu"></div>
      </nav>
      <div id="cm-menu-content">
        <div id="cm-menu-items-wrapper">
          <div id="cm-menu-scroller">
            <ul class="cm-menu-items">
              <li class="inactive"><a href="/welcome" class="sf-house">欢迎页面</a></li>
              <li class="inactive"><a href="/dashboard" class="sf-dashboard">数据中心</a></li>
              <li class="inactive"><a href="/registers" class="sf-user-id">注册用户</a></li>
              <li class="inactive"><a href="/records" class="sf-notepad">门禁记录</a></li>
              <li class="active"><a href="/useradd" class="sf-handshake">访客添加</a></li>
              <li class="inactive"><a href="/systool" class="sf-wrench-screwdriver">系统工具</a></li>
              <li class="inactive"><a href="/video" class="sf-webcam">Demo演示</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
	<header id="cm-header">
      <nav class="cm-navbar cm-navbar-primary">
        <div class="btn btn-primary md-menu-white hidden-md hidden-lg" data-toggle="cm-menu"></div>
        <div class="cm-flex"><h1>AI门禁后台管理系统</h1></div>
      </nav>
    </header>
	<div id="global">
      <div class="container-fluid">
        <div class="panel panel-default">
          <div class="panel-body">
            <h2>欢迎使用AI门禁后台管理系统</h2>
          </div>
        </div>
		<div class="panel panel-default">
            <div class="panel-heading">访客添加</div>
                <div class="panel-body" style="min-height: 214px;">
                    <form class="form-horizontal" action="/put/user" method="POST" enctype="multipart/form-data">
                        <div class="form-group">
                            <label class="col-sm-2 control-label">姓名</label>
                                <div class="col-sm-10">
                                    <input type="text" class="form-control" name="uname" placeholder="Username">
                                </div>
                        </div>
                        <div class="form-group">
                            <label class="col-sm-2 control-label">性别</label>
                                <div class="col-sm-10">
                                    <select name="gender" class="form-control">
                                      <option value="male">男</option>
                                      <option value="female">女</option>
                                    </select>
                                </div>
                        </div>
                        <div class="form-group">
                            <label class="col-sm-2 control-label">年龄</label>
                                <div class="col-sm-10">
                                    <input name="age" type="text" class="form-control" placeholder="Age">
                                </div>
                        </div>
                        <div class="form-group">
                            <label class="col-sm-2 control-label">人脸图像</label>
                                <div class="col-sm-10">
                                    <input name="image" type="file" class="form-control">
                                </div>
                        </div>
                        <div class="form-group" style="margin-bottom:0">
                            <div class="col-sm-offset-2 col-sm-10">
                                <button type="submit" class="btn-lg btn-primary">提交</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
    </div>
        <footer class="cm-footer"><span class="pull-right">&copy; ACME Inc.</span></footer>
    </div>

<!-- Scripts -->
    <script src="{{ url_for('static', filename='assets/js/lib/jquery-2.1.3.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/jquery.mousewheel.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/jquery.cookie.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/fastclick.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/bootstrap.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/clearmin.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='video.js')}}"
    ></script>
</body>
{% endblock %}
