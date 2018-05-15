{% extends 'base.tpl' %}

{% block title %}
    <title>主页面</title>
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
              <li class="active"  ><a href="#" class="sf-house">主页面</a></li>
              <li class="inactive"><a href="#" class="sf-lock-open">登录页</a></li>
              <li class="inactive"><a href="#" class="sf-layers">查询页</a></li>
              <li class="inactive"><a href="#" class="">功能页2</a></li>
              <li class="inactive"><a href="#" class="">功能页3</a></li>
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
            <h2>欢迎使用本系统!</h2>
          </div>
        </div>
            <button onclick="getJSON()" id="getJson" type="button" class="btn btn-primary btn-lg">获取</button>
        <div class="panel panel-default">
          <div class="panel-heading">Tables with contextual classes</div>
            <div class="panel-body">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>UID</th>
                            <th>姓名</th>
                            <th>性别</th>
                            <th>年龄</th>
                        </tr>
                    </thead>
                    <tbody>
<!-- Data -->
                   </tbody>
                </table>
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
        src="{{ url_for('static', filename='main.js')}}"
    ></script>
</body>
{% endblock %}
