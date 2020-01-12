// document.getElementById('search_btn').onclick = function()
// {
//     var searchText = document.getElementById('txt_field').value;
//     searchRequest(searchText);
// };

// function searchRequest(searchText) {
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//             if (this.readyState == 4 && this.status == 200) {
//              var result = JSON.parse(this.responseText);
//             }
//           };
//         var url = 'IP:port/search?query='+ searchText; 
//         xhttp.open("GET", url, true);
//         xhttp.send();
//     }