// Lấy phần tử form
var form = document.getElementsByTagName("form")[0];

// Lấy các phần tử input trong form
var inputs = form.getElementsByTagName("input");

// Thêm sự kiện blur cho mỗi input
for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener("blur", validateInput);
}

// Hàm kiểm tra giá trị nhập vào của input
function validateInput(event) {
    // Lấy phần tử input đang xử lý
    var input = event.target;

    // Lấy giá trị nhập vào của input
    var value = input.value;

}