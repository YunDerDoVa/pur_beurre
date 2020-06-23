function add_favor(id, url) {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("add_food_alerte").style.display = 'flex';
      setTimeout(function() {
        document.getElementById("add_food_alerte").style.display = 'none';
      }, 5000);

      document.getElementById(id).remove();
    }
  }

  xhttp.open("GET", url, true);
  xhttp.send();

}

function del_favor(id, url) {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("del_food_alerte").style.display = 'flex';
      setTimeout(function() {
        document.getElementById("del_food_alerte").style.display = 'none';
      }, 5000);

      document.getElementById(id).remove();
    }
  }

  xhttp.open("GET", url, true);
  xhttp.send();

}
