# Motorcycle-dealer-manager-MISD-PTIT
- Thiết kế hệ thống: Các tệp pdf

https://www.canva.com/design/DAFcSgsBSuY/dfenHzkRr1k4s4IQSq9XfQ/edit

https://www.canva.com/design/DAFgzqm7S90/cVCrgREzGYqicni6ew_B_w/edit
- Sơ đồ cơ sở dữ liệu cho hệ thống:
<img src="E:\Thiết kế cơ sở dữ liệu.png"/>
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
        <img src="E:\1.png"/>
        - Xem lịch sử bán hàng của nhân viên
       <img src="E:\2.png"/>
        - Xem các mặt hàng bán ra theo tháng
        <img src="E:\3.png"/>
        - Xem mặt hàng bán chạy
        <img src="E:\4.png"/>
        - Xem lịch sử nhập hàng của nhân viên
        <img src="E:\5.png"/>
      - Xem trực quan dữ liệu
        - Trực quan thu chi
        <img src="E:\6.png"/>
        - Trực quan doanh số của nhân viên theo tháng
        <img src="E:\7.png"/>
        - Trực quan mặt hàng bán chạy theo tháng
        <img src="E:\8.png"/>
        - Trực quan mặt hàng bán chạy
        <img src="E:\9.png"/>
        - Trực quan số lượng đã nhập theo cửa hàng
        <img src="E:\10.png"/>
        - Trực quan lượng hàng đã nhập theo từng nhà cung cấp
        <img src="E:\11.png"/>