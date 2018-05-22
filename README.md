# 基于机器学习的智慧人脸门禁系统

这是一枚草案性质的基于机器学习的智慧人脸门禁系统。为2018年Hackathon虹软任务编写。

# 系统要求

本系统的依赖项如下所示：

- dlib
- Python 3.5 + (不支持Python2)
- Node.js (可选的)

本系统服务端程序在Linux与macOS上测试通过，但不保证在Windows系统上也能正常工作。

# 使用说明

在保证系统要求达到的前提下，按如下步骤进行：

1. 拷贝项目源码库使用`git clone`
2. `cd` 进入项目主目录`app` 目录下
3. 使用`pip3 install -r requirement.txt`安装全部项目依赖
4. `python3 app.py`启动项目

# 系统架构

项目借助`dlib`机器学习库与`flask`框架，实现出了一个高可用，开发友好的智能人脸识别系统。后端服务端使用核心人脸识别模块分析场景中的人脸信息，如：图片是否包含人脸，人脸特征点提取，人脸特征向量的提取与比对。具体见下图：

![example1][example_1]

![example2][example_2]

![example3][example_3]

![example4][example_4]

另一核心技术问题是，如何从视频流中提取人脸信息（包括视频流转化序列帧与序列帧传输分析）。本项目使用`WebRTC`捕捉来自目标地址的视频流（使用Web Socket`ws://`）。浏览器端使用`HTML5 Canvas API`捕捉并转换视频流中的每一帧，`XHR`发往后端服务器，服务器分析后返回包含分析结果的JSON。

![arch1][arch_1]

在实现人脸识别模块与视频处理模块后，就可以搭建基于AI的智慧人脸门禁系统了。门禁系统使用**内存键值对**数据库存储人脸信息，这保证了系统人脸识别的效率与速度。

用户信息数据库采用传统关系型数据库`Mariadb`存储，与内存中的人脸数据库使用`UID`进行关联，具备高灵活性与可扩展性。

系统还实现了一个**增量式日志模块**，该模块可以准确记录下用户/访客/陌生人通过门禁的具体信息，也为数据分析服务提供数据支持。

系统前端管理界面使用`Bootstrap`搭建，加入了很多好用的前端插件。得益于响应式的网页设计，整个客户端具备可移植性，管理人员在手机端或桌面端均可使用后台管理系统。

![example5][example_5]

![example6][example_6]

# 演示

下图展示了，本系统可正常识别出摄像头视频流中的人脸信息，并处理。

![demo1][demo_1]

# 许可协议

[MIT](./LICENSE)

[example_1]: ./dev_docs/doc_images/example_1.png
[example_2]: ./dev_docs/doc_images/example_2.png
[example_3]: ./dev_docs/doc_images/example_3.png
[example_4]: ./dev_docs/doc_images/example_4.png
[arch_1]:    ./dev_docs/doc_images/arch_1.png
[demo_1]:    ./dev_docs/doc_images/demo_1.png
[example_5]: ./dev_docs/doc_images/example_5.png
[example_6]: ./dev_docs/doc_images/example_6.png

