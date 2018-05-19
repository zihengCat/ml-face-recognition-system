/**
 * Created by zihengCat on 2018-05-17.
 * Client side of dlib Face Detection Web API
 */
//Parameters
const s = document.getElementById('objDetect');
//the API server url
const apiServer = window.location.origin + '/image';
const wsIPPort = '192.168.31.192:8084'

//canvas to grab an image for upload
let imageCanvas = document.getElementById('videoCanvas');
let imageCtx = imageCanvas.getContext("2d");

//Canvas setup
//create a canvas for drawing object boundaries
let drawCanvas = document.createElement('canvas');
//document.body.appendChild(drawCanvas);
let drawCtx = drawCanvas.getContext("2d");

//draw boxes and labels on each detected object
/*
{   'uid': name,
    'locations': {
        'tops': top,
        'right': right,
        'bottom': bottom,
        'left': left
    }
}
*/
function drawBoxes(objects) {
    //clear the previous drawings
    //drawCtx.clearRect(0, 0, drawCanvas.width, drawCanvas.height);
    if(objects !== null &&
       objects.uid === 'noface')
    {
        //var showArea = document.getElementById('showArea');
        //var str = JSON.stringify(objects.info);
        //var str = '';
        //showArea.innerHTML = str;
    }
    else if(objects !== null &&
            objects.uid === 'unknown')
    {
        var showArea = document.getElementById('showArea');
        //var str = JSON.stringify(objects.info);
        var str = '<div class="markdown-body"><table><thead><tr><th>姓名</th><th>性别</th><th>年龄</th></tr></thead><tbody><tr><td>name</td><td>gender</td><td>age</td></tr><tbody></table></div>';
        str = str.replace('name', '陌生人');
        str = str.replace('gender', '');
        str = str.replace('age', '');
        showArea.innerHTML = str;
    }
    else if(objects !== null &&
            objects.uid !== 'noface' &&
            objects.uid !== 'unknown')
    {
        var showArea = document.getElementById('showArea');
        //var str = JSON.stringify(objects.info);
        var str = '<div class="markdown-body"><table><thead><tr><th>姓名</th><th>性别</th><th>年龄</th></tr></thead><tbody><tr><td>name</td><td>gender</td><td>age</td></tr><tbody></table></div>';
        str = str.replace('name', objects.info.name);
        str = str.replace('gender', objects.info.gender);
        str = str.replace('age', objects.info.age);
        showArea.innerHTML = str;
    }
}

//Add file blob to a form and post
function postFile(file) {

    //Set options as form data
    let formdata = new FormData();
    formdata.append("image", file);
    //formdata.append("threshold", scoreThreshold);

    let xhr = new XMLHttpRequest();
    xhr.open('POST', apiServer, true);
    xhr.onload = function () {
        if (this.status === 200) {
            let objects = JSON.parse(this.response);
            console.log(objects);
            //draw the boxes
            drawBoxes(objects);
            //Save and send the next image
            //imageCtx.drawImage(v, 0, 0, v.videoWidth, v.videoHeight, 0, 0, uploadWidth, uploadWidth * (v.videoHeight / v.videoWidth));
            imageCtx.drawImage(v, 0, 0, v.videoWidth, v.videoHeight, 0, 0,
            imageCanvas.width,
            imageCanvas.width * (v.videoHeight / v.videoWidth));
            imageCanvas.toBlob(postFile, 'image/jpeg');
        }
        else {
            console.error(xhr);
        }
    };
    xhr.send(formdata);
}

//Start object detection
function startObjectDetection() {

    console.log("starting object detection");

    v = imageCanvas;
    //Set canvas sizes base don input video
    drawCanvas.width = imageCanvas.width;
    drawCanvas.height = imageCanvas.height;

    /*
    imageCanvas.width = uploadWidth;
    imageCanvas.height = uploadWidth * (v.videoHeight / v.videoWidth);
    */

    //Some styles for the drawcanvas
    drawCtx.lineWidth = 6;
    drawCtx.strokeStyle = "cyan";
    drawCtx.font = "28px Verdana";
    drawCtx.fillStyle = "cyan";

    //Save and send the first image
    imageCtx.drawImage(v, 0, 0, v.videoWidth, v.videoHeight, 0, 0,
                       imageCanvas.width,
                       imageCanvas.width * (v.videoHeight / v.videoWidth));
    imageCanvas.toBlob(postFile, 'image/jpeg');

}

startObjectDetection();
// Show loading notice
var canvas = document.getElementById('videoCanvas');
var ctx = canvas.getContext('2d');
ctx.fillText('Loading...', canvas.width/2-30, canvas.height/3);
// Setup the WebSocket connection and start the player
var client = new WebSocket("ws://" + wsIPPort);
var player = new jsmpeg(client, {canvas:canvas});



//Starting events
/*
//check if metadata is ready - we need the video size
v.onloadedmetadata = () => {
    console.log("video metadata ready");
    gotMetadata = true;
    if (isPlaying)
        startObjectDetection();
};

//see if the video has started playing
v.onplaying = () => {
    console.log("video playing");
    isPlaying = true;
    if (gotMetadata) {
        startObjectDetection();
    }
};
*/
