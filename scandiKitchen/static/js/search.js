$(document).ready(function() {

    $("#searchForm").submit(function(e){
        e.preventDefault();
        var search_word = $("#txt_field").val()

        window.location = `${window.location.origin}/search/${search_word}`
        

    
    });
})


