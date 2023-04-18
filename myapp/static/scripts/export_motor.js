// Lấy phần tử form
var form = document.getElementsByTagName("form")[0];

// Lấy các phần tử input và select trong form
var inputs = form.getElementsByTagName("input");
var selects = form.getElementsByTagName("select");

// Thêm sự kiện blur cho mỗi input và select
for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener("blur", validateInput);
}
for (var i = 0; i < selects.length; i++) {
    selects[i].addEventListener("blur", validateInput);
}

// Hàm kiểm tra giá trị nhập vào của input và select
function validateInput(event) {
    // Lấy phần tử input hoặc select đang xử lý
    var input = event.target;

    // Lấy giá trị nhập vào của input hoặc select
    var value = input.value;

}