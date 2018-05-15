function getJSON() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/get/register", true);
    xmlhttp.onreadystatechange = function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = JSON.parse(xmlhttp.responseText);
            var d = document.getElementsByClassName('table');
            d = d[0].tBodies[0];
            d.innerHTML = "";
            for(var i = 0; i < data.length; i++) {
                d.innerHTML += json2el(data[i]);
            }
        }
    }
    xmlhttp.send();
}

function json2el(obj) {
/*
[{ 'uid': '1',
  'name': 'ziheng',
  'age': '20',
  'gender': '男'
  'image': 'addr'
}, ...]
*/
    var str = '<tr>' +
              '<th>' + obj['uid'] + '</th>' +
              '<th>' + obj['name'] + '</th>' +
              '<th>' + obj['gender'] + '</th>' +
              '<th>' + obj['age'] + '</th>' +
              '</tr>';
    return str;
}

