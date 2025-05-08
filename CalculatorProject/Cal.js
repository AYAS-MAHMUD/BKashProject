
const display = document.getElementById("display");

function appendtodisplay(input){
    display.value +=input;
}
function clearvalue(){
    display.value = ""
}
function calculate(){
    display.value = eval(display.value)
}