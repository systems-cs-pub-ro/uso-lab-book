$( document ).ready(function() {
    $(".sidebar-group").click(function() {
        $(this).children("ul").toggle();
    });
});
