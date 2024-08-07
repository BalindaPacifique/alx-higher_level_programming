// File: 102-script.js
$(document).ready(function() {
    $("#btn_translate").click(function() {
        let langCode = $("#language_code").val();
        $.get("https://www.fourtonfish.com/hellosalut/hello/?lang=" + langCode, function(data) {
            $("#hello").text(data.hello);
        });
    });
});
