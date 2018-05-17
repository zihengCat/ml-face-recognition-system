function getData() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/get/register", true);
    xmlhttp.onreadystatechange = function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var data = JSON.parse(xmlhttp.responseText);
            var d = document.getElementsByClassName('table');
            d = d[0].tBodies[0];
            d.innerHTML = "";
            for(var k in data) {
                d.innerHTML += json_to_node(k, data[k]);
            }
        }
    }
    xmlhttp.send();
}
function getXXX() {
    alert("该功能还未完成...");
}
function json_to_node(key, obj) {
/*
{ 'uid': {
    'name': 'ziheng',
    'age': '20',
    'gender': '男',
    'image': 'addr'
   },
   ...
}
*/
    var str = '<tr>' +
              '<th>' + key + '</th>' +
              '<th>' + obj['name'] + '</th>' +
              '<th>' + obj['gender'] + '</th>' +
              '<th>' + obj['age'] + '</th>' +
              '</tr>';
    return str;
}

