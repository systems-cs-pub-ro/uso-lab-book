$(function() {
    var toggleCaptionVisibility = function(idx, elem) {
        //var tocCaption = this.innerText.split("\n")[0];
        var tocCaption = elem.innerText.split("\n")[0];

        var visibleCaption = sessionStorage.getItem("visibleCaption");
        if (visibleCaption) {
            //var isVisible = $(this).children("ul").is(":visible");
            var isVisible = $(elem).children("ul").is(":visible");
            if (((!isVisible) && (visibleCaption === tocCaption)) ||
                (isVisible && (visibleCaption !== tocCaption))) {

                $(elem).children("ul").toggle();
            }
        }
    };

    if (sessionStorage.getItem("visibleCaption")) {
        $(".sidebar-group").each(toggleCaptionVisibility);
    }

    $(".sidebar-group .caption-text a").click(function(event) {
        event.preventDefault();
    });

    $(".sidebar-group").click(function() {
        $(this).children("ul").toggle();

        var tocCaption = this.innerText.split("\n")[0];
        sessionStorage.setItem("visibleCaption", tocCaption);

        $(".sidebar-group").each(toggleCaptionVisibility);
    });
});