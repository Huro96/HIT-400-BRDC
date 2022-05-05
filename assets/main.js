
// Add active class to the current button (highlight it)
var header = document.getElementById("grouplist");
var btns = header.getElementsByClassName("items");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
  var current = document.getElementsByClassName("active");
  current[0].className = current[0].className.replace(" active", "");
  this.className += " active";
  });
}

var el = document.getElementById("wrapper");
var toggleButton = document.getElementById("menu-toggle");

toggleButton.onclick = function () {
    el.classList.toggle("toggled");
};
var el = document.getElementById("wrapper");
var toggleButton = document.getElementById("menu-toggle");

toggleButton.onclick = function () {
    el.classList.toggle("toggled");
};

$("#txtarea").on("keyup input",function()
{
    $(this).css('height','auto').css('height',this.scrollHeight+(this.offsetHeight-this.clientHeight));
});
