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
          <img src="image/12.png" alt="Alt text" title="Optional title">
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
        - Xem hệ thống khuyến nghị
            - Dự đoán sản phẩm
              <img src="image/13.png" alt="Alt text" title="Optional title">
            - Dự đoán nhà cung cấp
              <img src="image/14.png" alt="Alt text" title="Optional title">
    - Các chức năng của nhân viên bán hàng
        - Quản lý cửa hàng
          <img src="image/15.png" alt="Alt text" title="Optional title">
        - Quản lý chi phí
          <img src="image/16.png" alt="Alt text" title="Optional title">
        - Quản lý hóa đơn xuất hàng
          <img src="image/17.png" alt="Alt text" title="Optional title">
        - Xem báo cáo thống kê
            - Báo cáo mặt hàng đã bán theo tháng(giống với admin)
            - Báo cáo mặt hàng bán chạy(giống với admin)
            - Xem lịch sử bán hàng
              <img src="image/18.png" alt="Alt text" title="Optional title">
        - Xem trực quan hóa
            - Trực quan mặt hàng đã bán theo tháng(giống admin)
            - Trực quan mặt hàng bán chạy(giống admin)
            - Trực quan số lượng hàng đã bán cho từng cửa hàng(giống admin)
            - Trực quan kpi
              <img src="image/19.png" alt="Alt text" title="Optional title">
    - Các chức năng của nhân viên kho
        - Quản lý xe
          <img src="image/20.png" alt="Alt text" title="Optional title">
        - Quản lý nhà cung cấp
          <img src="image/21.png" alt="Alt text" title="Optional title">
        - Quản lý hóa đơn nhập hàng
          <img src="image/22.png" alt="Alt text" title="Optional title">
        - Xem báo cáo thống kê
            - Xem lịch sử nhập hàng
              <img src="image/23.png" alt="Alt text" title="Optional title">
        - Xem trực quan hóa
            - Trực quan số lượng hàng đã nhập của từng nhà cung cấp(giống admin)