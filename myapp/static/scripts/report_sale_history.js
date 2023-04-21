// Lấy phần tử bảng
var table = document.getElementsByTagName("table")[0];

// Lấy các hàng trong bảng
var rows = table.getElementsByTagName("tr");

// Thêm sự kiện click cho mỗi hàng
for (var i = 1; i < rows.length; i++) {
    // Lấy các phần tử liên kết trong hàng
    var links = rows[i].getElementsByTagName("a");

    // Duyệt qua các liên kết
    for (var j = 0; j < links.length; j++) {
        // Thêm sự kiện click cho liên kết
        links[j].addEventListener("click", function (event) {
            // Ngăn chặn hành động mặc định của liên kết
            event.preventDefault();

            // Lấy đường dẫn của liên kết
            var href = this.getAttribute("href");

            // Hiển thị thông báo xác nhận
            var confirm = window.confirm("Bạn có muốn xem chi tiết " + this.textContent + "?");

            // Nếu người dùng đồng ý, chuyển hướng đến đường dẫn của liên kết
            if (confirm) {
                window.location.href = href;
            }
        });
    }
}