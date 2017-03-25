function test_demo_initialization_function() {
  document.getElementById("demo_initialization_intro").innerHTML = "javascript works!";
}

function simple_ajax_request(method, url) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, 'http://' + url, true);
  xhr.onload = function() {
    var response = JSON.parse(xhr.responseText);
    document.getElementById("demo_initialization_intro").innerHTML = "Status code: " + (xhr.status).toString() + ". Response message: " + response.status + ".";
  };
  xhr.send();
}
