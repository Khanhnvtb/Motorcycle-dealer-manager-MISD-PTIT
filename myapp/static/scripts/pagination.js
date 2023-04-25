$(document).ready(function () {
    var keyword = "{{keyword}}";
    if (keyword) {
        var href = $(".page-link").attr("href");
        $(".page-link").attr("href", href + `&keyword=` + keyword);
    }
});
