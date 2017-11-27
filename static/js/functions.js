$(document).ready(function () {
    $("#sendCSV").click(function () {
        $(this).addClass("loading")
        $("#upload_form").submit()
    });
    $("#id_csvFile").change(function () {
        if ($(this).val() !== "") {
            $("#sendCSV").removeClass("disabled")
        }
    });
});

function dismiss(element) {
    element.delay(200).fadeOut()
}
