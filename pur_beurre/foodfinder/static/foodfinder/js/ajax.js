function add_favor(url) {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("add_food_alerte").style.display = 'flex';
    }
    setTimeout(function() {
      document.getElementById("add_food_alerte").style.display = 'none';
    }, 5000)
  };

  xhttp.open("GET", url, true);
  xhttp.send();

}
