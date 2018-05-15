{% extends 'head.tpl' %}
{% block title %}
    <title>登录页</title>
{% endblock %}
{% block body %}
<body class="cm-login">
    <div class="text-center"
    style="padding:90px 0 30px 0;background:#fff;border-bottom:1px solid #ddd">
      <img src="{{ url_for('static', filename='assets/img/logo-big.svg') }}"
      width="300" height="45">
    </div>
    <div class="col-sm-6 col-md-4 col-lg-3" style="margin:40px auto; float:none;">
   <form method="POST" action="/login">
	<div class="col-xs-12">
          <div class="form-group">
	    <div class="input-group">
	      <div class="input-group-addon"><i class="fa fa-fw fa-user"></i></div>
	      <input type="text" name="username" class="form-control" placeholder="Username">
	    </div>
          </div>
          <div class="form-group">
	    <div class="input-group">
	      <div class="input-group-addon"><i class="fa fa-fw fa-lock"></i></div>
	      <input type="password" name="password" class="form-control" placeholder="Password">
	    </div>
          </div>
        </div>
	<div class="col-xs-6">
          <div class="checkbox"><label><input type="checkbox">记住我</label></div>
	</div><div class="col-xs-6">
          <button type="submit" class="btn btn-block btn-primary">登录</button>
        </div>
      </form>
    </div>
</body>
{% endblock %}
