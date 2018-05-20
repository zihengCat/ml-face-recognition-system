# Machine Learning based Face Recognition System

A draft machine learning based Face Recognition System works for 2018 Hackathon ArcSoft（虹软）task.

# System Requirements

The draft system was tested on following system requirement:

- dlib
- Python 3.5 + (Not Support Python2)
- Node.js (Optional)

The draft system server side works fine on Linux and macOS, but didn't test on Windows.

# Usage

Please make sure your system requirements has no problem. Do as following.

- clone the source using `git clone`.
- `cd` to project `app` directory
- install all dependences using `pip3 install -r requirement.txt`
- run `python3 app.py` to start the system

# Architecture

The project achieved a high availability and develop friendly Face Recognition System based on `dlib` machine learning library and python `flask` micro web framework. Back-end server using the core face recognition modular to analysis specific image infomations, something like that, does the image contains faces, what location landmarks on the face, what is the distance of two images...etc. Look at examples.

[example1][example_1]

[example2][example_2]

[example3][example_3]

[example4][example_4]

[example5][example_5]

The problem is to processing video streams(both converting and analysising), I chieve that in a creative way. Using WebRTC to catch streams from a target IP addres(using Web Socket `ws://`). And converting every frame on the video stream by using HTML5 Canvas API. Then sending every frame captured to back-end server, server analysised and returned JSON to show the results.

[arch1][arch_1]

After achieved core face recognition modular and video stream processing modular, I started building an AI based Access Control System by using two core modulars. The Access Control System could recognize faces on **Memory based Face key-value Database** quickly, effectively and correctly.

The main user info database using `Mariadb` to achieve both high availability and scalability.

The system also added a **Incremental Log Module** which also could be used in data analysising services.

The front end managment system is developed based on `Bootstrap`, also added some useful plug-ins. Benefited by responsive website design, the whole client could run cross-platform,  mobile or desktop.

# Demo

The following example shows that the system works fine.

![demo1][demo_1]

# License

[MIT](./LICENSE)

[example_1]: ./dev_docs/doc_images/example_1.png
[example_2]: ./dev_docs/doc_images/example_2.png
[example_3]: ./dev_docs/doc_images/example_3.png
[example_4]: ./dev_docs/doc_images/example_4.png
[example_5]: ./dev_docs/doc_images/example_5.png
[arch_1]: ./dev_docs/doc_images/arch_1.png
[demo_1]: ./dev_docs/doc_images/demo_1.png

