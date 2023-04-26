import json
import mysql.connector
# Tên các file JSON cần import
json_files = ['motor.json',
              'store.json', 'supplier.json', 'user.json','delivery_invoice.json', 'delivery_motor.json','deliveryreceipt.json',  'expense.json',
               'import_invoice.json', 'import_motor.json','importreceipt.json', ]
# Kết nối tới MySQL
try: 
    cnx = mysql.connector.connect(user='root', password='phuy2712',
                                host='127.0.0.1', port=3306, database='motorcycle_manager')
    
    cursor = cnx.cursor()
    print("Connected to MySQL")
    for file_name in json_files:
    # Đọc dữ liệu từ file JSON
        with open('./database/' + file_name) as f:
            data = json.load(f)

        # Tên bảng tương ứng với file JSON
        table_name = 'myapp_' + file_name.split('.')[0]

        # Tạo danh sách các trường trong bảng
        fields = list(data[0].keys())

        # Tạo danh sách các giá trị để chèn vào bảng
        values_list = []
        for record in data:
            values = []
            for field in fields:
                values.append(record[field])
            values_list.append(tuple(values))

            # Tạo truy vấn SQL REPLACE
            placeholders = ', '.join(['%s'] * len(fields))
            sql = 'REPLACE INTO {} ({}) VALUES ({})'.format(table_name, ', '.join(fields), placeholders)

            # Thực thi truy vấn REPLACE
            cursor.executemany(sql, values_list)
            cnx.commit()
        print(file_name)
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    print("Failed to connect to MySQL: {}".format(err))



# Duyệt qua từng file JSON và thực hiện import


# Đóng kết nối MySQL
