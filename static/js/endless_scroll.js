$(document).ready(function () {
    $('.card-body').hide();
    quotes_size = $(".card-body").length;
    x=3;
    $('.card-body:lt('+x+')').show();
    $('#load-more').click(function () {
        x = (x+5 <= quotes_size) ? x+5 : quotes_size;
        $('.card-body:lt('+x+')').show();
        if (x == quotes_size){
            $('#load-more').hide()
        }
    });
});

// 
// $(document).ready(function() {
//     original_text = $("#addcmt").text()
//     $("#addcmt").click(function() {
//         $(".commentarea").toggle();
//         if ($("#addcmt").text() == "Add additional comment") {
//             $("#addcmt").text("Remove comment");
//         }
//         else {
//             $("#addcmt").text("Add additional comment");
//         }
//     });
// });
