// File: 103-script.js
$(document).ready(function() {
    function fetchHello() {
        let langCode = $("#language_code").val();
        $.get("https://www.fourtonfish.com/hellosalut/hello/?lang=" + langCode, function(data) {
            $("#hello").text(data.hello);
        });
    }

    $("#btn_translate").click(fetchHello);

    $("#language_code").keypress(function(event) {
        if (event.which === 13) {
            fetchHello();
        }
    });
});
