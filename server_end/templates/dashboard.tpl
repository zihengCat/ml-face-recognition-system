{% extends 'base.tpl' %}

{% block title %}
    <title>数据中心</title>
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

  <link rel="stylesheet" type="text/css"
        href="{{ url_for('static', filename='assets/css/font-awesome.min.css')}}"
  >
  <link rel="stylesheet" type="text/css"
        href="{{ url_for('static', filename='assets/css/c3.min.css')}}"
  >
</head>
{% endblock %}
{% block body %}
<body class="cm-no-transition cm-1-navbar">
<!-- CM Menu -->
    <div id="cm-menu">
      <nav class="cm-navbar cm-navbar-primary">
        <div class="cm-flex"><h1>LOGO</h1></div>
        <div class="btn btn-primary md-menu-white" data-toggle="cm-menu"></div>
      </nav>
      <div id="cm-menu-content">
        <div id="cm-menu-items-wrapper">
          <div id="cm-menu-scroller">
            <ul class="cm-menu-items">
              <li class="inactive"><a href="#" class="sf-house">欢迎页面</a></li>
              <li class="active"><a href="#" class="sf-dashboard">数据中心</a></li>
              <li class="inactive"><a href="#" class="sf-layers">注册用户</a></li>
              <li class="inactive"><a href="#" class="sf-layers">门禁记录</a></li>
              <li class="inactive"><a href="#" class="sf-layers">访客添加</a></li>
              <li class="inactive"><a href="#" class="sf-lock-open">登录页面</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
<!-- CM Header -->
	<header id="cm-header">
            <nav class="cm-navbar cm-navbar-primary">
                <div class="btn btn-primary md-menu-white hidden-md hidden-lg" data-toggle="cm-menu"></div>
                <div class="cm-flex">
                    <h1>Home</h1>
                    <form id="cm-search" action="index.html" method="get" class="">
                        <input type="search" name="q" autocomplete="off" placeholder="搜索...">
                    </form>
                </div>
                <div class="pull-right">
                    <div id="cm-search-btn" class="btn btn-primary md-search-white" data-toggle="cm-search"></div>
                </div>
                <div class="dropdown pull-right">
                    <button class="btn btn-primary md-notifications-white" data-toggle="dropdown" aria-expanded="false"> <span class="label label-danger">3</span></button>
                    <div class="popover cm-popover bottom" style="left: -210px;">
                        <div class="arrow" style="left: 235px;"></div>
                        <div class="popover-content">
                            <div class="list-group">
                                <a href="#" class="list-group-item">
                                    <h4 class="list-group-item-heading text-overflow">
                                        <i class="fa fa-fw fa-envelope"></i>消息
                                    </h4>
                                    <p class="list-group-item-text text-overflow">这是一条动态消息。</p>
                                </a>
                                <a href="#" class="list-group-item">
                                    <h4 class="list-group-item-heading">
                                        <i class="fa fa-fw fa-envelope"></i>消息
                                    </h4>
                                    <p class="list-group-item-text">这是一条动态消息。</p>
                                </a>
                                <a href="#" class="list-group-item">
                                    <h4 class="list-group-item-heading">
                                        <i class="fa fa-fw fa-warning"></i>警告
                                    </h4>
                                    <p class="list-group-item-text">这是一条警告信息。</p>
                                </a>
                            </div>
                            <div style="padding:10px"><a class="btn btn-success btn-block" href="#">显示更多</a></div>
                        </div>
                    </div>
                </div>
                <div class="dropdown pull-right">
                    <button class="btn btn-primary md-account-circle-white" data-toggle="dropdown" aria-expanded="false"></button>
                    <ul class="dropdown-menu">
                        <li class="disabled text-center">
                            <a style="cursor:default;"><strong>Admin</strong></a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#"><i class="fa fa-fw fa-user"></i>主页</a>
                        </li>
                        <li>
                            <a href="#"><i class="fa fa-fw fa-cog"></i>设置</a>
                        </li>
                        <li>
                            <a href="#"><i class="fa fa-fw fa-sign-out"></i>登出</a>
                        </li>
                    </ul>
                </div>
            </nav>
        </header>
<!-- CM Global -->
	<div id="global">
      <div class="container-fluid">
        <div class="panel panel-default">
          <div class="panel-body">
            <h2>欢迎使用门禁后台管理系统</h2>
            <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis.</p>
          </div>
        </div>
<!-- CM Dashboard -->
                <div class="row">
                    <div class="col-sm-4">
                        <div class="panel panel-default">
                            <div class="panel-heading">CPU负载</div>
                            <div class="panel-body">
                                <div id="d1-c1" style="height:150px"></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-4">
                        <div class="panel panel-default">
                            <div class="panel-heading">内存压力</div>
                            <div class="panel-body">
                                <div id="d1-c2" style="height:150px"></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-4">
                        <div class="panel panel-default">
                            <div class="panel-heading">网络IO</div>
                            <div class="panel-body">
                                <div id="d1-c3" style="height:150px"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel panel-default">
                    <div class="panel-heading">门禁记录 - Bars</div>
                    <div class="panel-body">
                        <div id="d1-c5" style="height:320px"></div>
                    </div>
                </div>
                <div class="panel panel-default">
                    <div class="panel-heading">门禁记录 - Splines</div>
                    <div class="panel-body">
                        <div id="d1-c4" style="height:320px"></div>
                    </div>
                </div>
                <div class="alert alert-info shadowed" role="alert"> <i class="fa fa-fw fa-info-circle"></i> 由 C3.js 绘图库提供强力支持 <a href="http://c3js.org/">http://c3js.org/</a> </div>

<!-- CM Footer -->
      <footer class="cm-footer"><span class="pull-right">&copy; A Company Inc.</span></footer>
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
        src="{{ url_for('static', filename='assets/js/lib/d3.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/lib/c3.min.js')}}"
    ></script>
    <script
        src="{{ url_for('static', filename='demo/dashboard.js')}}"
    ></script>
</body>
{% endblock %}
