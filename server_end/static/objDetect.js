/**
 * Created by zihengCat on 2018-05-17.
 * Client side of dlib Face Detection Web API
 */
//Parameters
const s = document.getElementById('objDetect');
const sourceVideo = s.getAttribute("data-source");  //the source video to use
const uploadWidth = s.getAttribute("data-uploadWidth") || 640; //the width of the upload file
const mirror = s.getAttribute("data-mirror") || false; //mirror the boundary boxes
const scoreThreshold = s.getAttribute("data-scoreThreshold") || 0.5;
//the API server url
const apiServer = s.getAttribute("data-apiServer") ||
                    window.location.origin + '/image';

//Video element selector
v = document.getElementById(sourceVideo);

//for starting events
let isPlaying = false,
    gotMetadata = false;

//Canvas setup

//create a canvas to grab an image for upload
let imageCanvas = document.createElement('canvas');
let imageCtx = imageCanvas.getContext("2d");

//create a canvas for drawing object boundaries
let drawCanvas = document.createElement('canvas');
document.body.appendChild(drawCanvas);
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
    drawCtx.clearRect(0, 0, drawCanvas.width, drawCanvas.height);

    if(objects !== null &&
       objects.uid !== 'unknown' &&
       objects.uid !== 'noface')
    {
        //filter out objects that contain a class_name and then draw boxes and labels on each
        let object = objects;
        //console.log(object);
        // flip the x axis if local video is mirrored
        /*
        if (mirror) {
            x = drawCanvas.width - (x + width)
        }
        */

        drawCtx.fillText(object.info.name,
                         object.locations.bottom + 100,
                         object.locations.tops);

        drawCtx.strokeRect(object.locations.bottom + 80,
                           object.locations.tops + 20,
                           100,
                           100)
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
            imageCtx.drawImage(v, 0, 0, v.videoWidth, v.videoHeight, 0, 0, uploadWidth, uploadWidth * (v.videoHeight / v.videoWidth));
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

    //Set canvas sizes base don input video
    drawCanvas.width = v.videoWidth;
    drawCanvas.height = v.videoHeight;

    imageCanvas.width = uploadWidth;
    imageCanvas.height = uploadWidth * (v.videoHeight / v.videoWidth);

    //Some styles for the drawcanvas
    drawCtx.lineWidth = 6;
    drawCtx.strokeStyle = "cyan";
    drawCtx.font = "28px Verdana";
    drawCtx.fillStyle = "cyan";

    //Save and send the first image
    imageCtx.drawImage(v, 0, 0, v.videoWidth, v.videoHeight, 0, 0, uploadWidth, uploadWidth * (v.videoHeight / v.videoWidth));
    imageCanvas.toBlob(postFile, 'image/jpeg');

}

//Starting events

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

