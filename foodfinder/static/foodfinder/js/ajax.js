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

function add_favor_from_details(url) {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("add_food_alerte").style.display = 'flex';
      setTimeout(function() {
        document.getElementById("add_food_alerte").style.display = 'none';
      }, 5000);

      document.getElementById("save_button").href = 'javascript:void(0);';
      document.getElementById("save_button").enabled = false;
      document.getElementById("save_button").innerHTML = 'Ajouté aux favoris';
    }
  }

  xhttp.open("GET", url, true);
  xhttp.send();

}
