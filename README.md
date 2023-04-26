# Motorcycle-dealer-manager-MISD-PTIT
- Thiết kế hệ thống: Các tệp pdf

https://www.canva.com/design/DAFcSgsBSuY/dfenHzkRr1k4s4IQSq9XfQ/edit

https://www.canva.com/design/DAFgzqm7S90/cVCrgREzGYqicni6ew_B_w/edit
- Sơ đồ cơ sở dữ liệu cho hệ thống:
<img src="image/Thiết kế cơ sở dữ liệu.png" alt="Alt text" title="Optional title">
- Các bước để có thể sử dụng:

Bước 1: Cài đặt python

Bước 2: Cài đặt các thư viện trong file requiments.txt

Bước 3: Cấu hình cơ sở dữ liệu

    - Tạo cơ sở dữ liệu: create database motorcycle_manager;
    - Thay đổi các cài đặt tại phần DATABASE trong tệp setting.py
    - Tạo các bảng trong database: py manage.py migrate
    - Nhập dữ liệu vào cơ sở dữ liệu: Nhập các tệp trong thư mục database hoặc chạy tệp import_data.py
Bước 3: Chạy server

py manage.py runserver

- Các chức năng trong có hệ thống
  - Các chức năng của admin
      - Quản lý nhân viên
    <img src="E:\Untitled.png"/>
      - Xem báo cáo thống kê
        - Xem thống kê thu chi theo tháng
        <img src="image/1.png" alt="Alt text" title="Optional title">
        - Xem lịch sử bán hàng của nhân viên
        <img src="image/2.png" alt="Alt text" title="Optional title">
        - Xem các mặt hàng bán ra theo tháng
        <img src="image/3.png" alt="Alt text" title="Optional title">
        - Xem mặt hàng bán chạy
        <img src="image/4.png" alt="Alt text" title="Optional title">
        - Xem lịch sử nhập hàng của nhân viên
        <img src="image/5.png" alt="Alt text" title="Optional title">
      - Xem trực quan dữ liệu
        - Trực quan thu chi
        <img src="image/6.png" alt="Alt text" title="Optional title">
        - Trực quan doanh số của nhân viên theo tháng
        <img src="image/7.png" alt="Alt text" title="Optional title">
        - Trực quan mặt hàng bán chạy theo tháng
        <img src="image/8.png" alt="Alt text" title="Optional title">
        - Trực quan mặt hàng bán chạy
        <img src="image/9.png" alt="Alt text" title="Optional title">
        - Trực quan số lượng đã nhập theo cửa hàng
        <img src="image/10.png" alt="Alt text" title="Optional title">
        - Trực quan lượng hàng đã nhập theo từng nhà cung cấp
        <img src="image/11.png" alt="Alt text" title="Optional title">
