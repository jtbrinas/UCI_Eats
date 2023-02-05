let serverUrl = "http://127.0.0.1:5000/"


function getRatings(ab) {
    fetch("http://127.0.0.1:5000/receiveFormData" + ab).then(res => res.json()).then(response => {
        console.log(response);
        for(var i in response) {
            document.getElementById(i).innerHTML = response[i].toFixed(2);
        }
    })
}

function callBackend() {
    fetch("http://127.0.0.1:5000/").then(res => res.json()).then(response => {
        console.log(response);
        document.getElementById('food_name').innerHTML = response.food_items[0];
        document.getElementById('food_rating').innerHTML = response.food_items[1];
    })      

}

function callBackend2() {
    fetch("http://127.0.0.1:5000/receiveFormData").then(res => res.json()).then(response => {
        console.log(response);
        document.getElementById('food_name').innerHTML = response.item3;
    })      

}
