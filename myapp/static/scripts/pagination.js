$(document).ready(function () {
    var keyword = $('.form-control').val();
    console.log(keyword);
    if (keyword) {
        var href = $(".page-link").attr("href");
        $(".page-link").attr("href", href + `&keyword=` + keyword);
    }
});
