# Motorcycle-dealer-manager-MISD-PTIT

https://www.canva.com/design/DAFcSgsBSuY/dfenHzkRr1k4s4IQSq9XfQ/edit

Các bước để có thể sử dụng:
Bước 1: Kích hoạt môi trường ảo
venv\Scripts\activate
Bước 2: Configure database
    - Tạo database: create database motorcycle_manager;
    - Thay đổi các cài đặt tại phần DATABASE trong file setting.py
    - Tạo các bảng trong database: py manage.py migrate
    - Import dữ liệu vào database: Chạy các file trong folder sql
Bước 3: Chạy server
py manage.py runserver
