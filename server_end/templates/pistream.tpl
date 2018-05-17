<!DOCTYPE html>
<html>
<head>
	<title>Demo - Raspberry Pi Streaming Recognition</title>
	<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
	<link rel="stylesheet" href="/static/bootstrap/css/bootstrap.min.css">
	<style type="text/css">
		body {
			text-align: center;
			/* margin-top: 10%; */
		}
		#videoCanvas {
			/* Always stretch the canvas to 640x480, regardless of its
			internal size. */
            /*
			width: 640px;
			height: 480px;
            */
		}
	</style>
</head>
<body>

<!--
-->

<div class="container">
<!-- -->
    <div class="jumbotron">
        <h1>虹软任务 - 基于AI智慧人脸门禁系统<h1>
        <h1>Demo演示（树莓派串流）<h1>
    </div>
<!-- -->
<div class="row">
  <div class="col-md-2"></div>
  <div class="col-md-8">
<!-- -->
<div class="panel panel-primary">
	<div class="panel-heading">
	  <h1 class="panel-title">识别结果</h1>
	</div>
	<div id="showArea" class="panel-body">
    <!-- 识别结果展示区 -->
	</div>
</div>
<!-- -->
  <div class="col-md-2"></div>
</div>
<!-- -->
</div>

<!-- The Canvas size specified here is the "initial" internal resolution. jsmpeg will
    change this internal resolution to whatever the source provides. The size the
    canvas is displayed on the website is dictated by the CSS style.
-->
	<canvas id="videoCanvas" width="640" height="480">
        <!-- if User Browser doesn't support Canvas -->
		<p>
			Please use a browser that supports the Canvas Element, like
			<a href="http://www.google.com/chrome">Chrome</a>,
			<a href="http://www.mozilla.com/firefox/">Firefox</a>,
			<a href="http://www.apple.com/safari/">Safari</a>
            or Internet Explorer 10
		</p>
	</canvas>
	<script type="text/javascript" src="/static/jsmpg.js"></script>
	<script type="text/javascript" src="/static/adapter-latest.js"></script>
	<script type="text/javascript" src="/static/pistream.js"></script>
    </script>
</body>
</html>
