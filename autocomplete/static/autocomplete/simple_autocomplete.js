function simple_autocomplete(field_id, datalist, name) {

  //console.log(field_id);
  //console.log(datalist);
  //console.log(name);

  var field = document.getElementById(field_id);

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      json = JSON.parse(this.responseText);

      datalist.inenrHTML = '';

      for (var i = 0; i < json.names.length; i++) {
        var name = json.names[i];
        var option = document.createElement('option');
        option.innerText = name;
        datalist.appendChild(option);
      }
    }
  };
  xhttp.open("GET", field.parentNode.dataset[field.dataset['urlname']] + '?name=' + name, true);
  xhttp.send();

}

function init_simple_autocomplete() {
  var fields = document.getElementsByClassName('mug-simple-autocomplete');

  for (var i = 0; i < fields.length; i++) {
    var field = fields[i];
    field.addEventListener("keypress", function(){
      var name = field.value;
      simple_autocomplete(field.id, field.list, name);
    });
  }

}

init_simple_autocomplete();
