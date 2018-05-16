'use strict';

document.getElementsByTagName('button')[0].onclick = playVideo;
var video = document.getElementById('webcam');
var constraints = window.constraints = {
  audio: false,
  video: true
};

function playVideo() {
    navigator.mediaDevices.getUserMedia(constraints, onSuccess, onError);
}

function onSuccess(stream) {
    var videoTracks = stream.getVideoTracks();
    video.srcObject = stream;
    video.autoplay = true;
    //or video.play();
}
function onError(e) {
    console.error(e);
}

