// Lấy phần tử form
var form = document.getElementsByTagName("form")[0];

// Lấy các phần tử input và textarea trong form
var inputs = form.getElementsByTagName("input");
var textarea = form.getElementsByTagName("textarea")[0];

// Thêm sự kiện blur cho mỗi input và textarea
for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener("blur", validateInput);
}
textarea.addEventListener("blur", validateInput);

// Hàm kiểm tra giá trị nhập vào của input và textarea
function validateInput(event) {
    // Lấy phần tử input hoặc textarea đang xử lý
    var input = event.target;

    // Lấy giá trị nhập vào của input hoặc textarea
    var value = input.value;

}