from connection import postgres_conn

cursor = postgres_conn.cursor()

def insert_tables():

    regions = ["tashkent", "samarqand","jizzax","namangan"]
    for i in regions:
        cursor.execute(f"INSERT INTO region(name) VALUES('{i}')")


    addresses = [
        ("140 qorabogsoy","qorobog",1),
        ("123 oybek","6/4",2),
        ("543 ilgor","3/4",3),
        ("10 istiqlol","2/2",4),]
    for i,j,k in addresses:
        cursor.execute(f"INSERT INTO address(address,district,region_id) VALUES('{i}','{j}',{k})")


    manufacturers = [
        ("arzon pharm",1),
        ("shayana pharm",2),
        ("medicine",3),
        ("new pharm",4)
    ]
    for i,j in manufacturers:
        cursor.execute(f"INSERT INTO manufacturer(name,address_id) VALUES('{i}',{j})")



    customers = [
        ("ahmad","jalolov","+998-93-474-32-34",1),
        ("obid","qodirov","+998-50-445-34-34",2),
        ("asil","kamilov","+998-90-656-56-34",3),
        ("javlon","abduqodirov","+998-78-233-75-34",4)
    ]
    for i,j,k,l in customers:
        cursor.execute(f"INSERT INTO customer(first_name,last_name,phone,address_id) VALUES('{i}', '{j}','{k}',{l})")



    cursor.execute("INSERT INTO staff(first_name,last_name,email,phone,start_work_at,end_work_at,address_id) VALUES('sodiq','ortiqov','sodiqortiqov@gmail.com','+998-94-918-34-25','08:00:00','14:00:00',1)")

    cursor.execute("INSERT INTO staff(first_name,last_name,email,phone,start_work_at,end_work_at,address_id) VALUES('alisher','hasanov','alisher1242@gmail.com','+998-91-004-70-08','14:00:00','20:00:00',2)")




    cursor.execute("INSERT INTO filial(address_id,weekend_day,work_start,work_finish) VALUES(1,7,'9:00:00','20:00:00')")

    cursor.execute("INSERT INTO filial(address_id,weekend_day,work_start,work_finish) VALUES(2,6,'8:00:00','20:00:00')")




    cursor.execute("INSERT INTO staff_filial(filial_id,staff_id) VALUES(2,1)")

    cursor.execute("INSERT INTO staff_filial(filial_id,staff_id) VALUES(1,2)")



    
    
    cursor.execute("INSERT INTO medicine(name,description,price,quantity,manufacturer_id,realise_date,finish_date,filial_id) VALUES('paratsetamol','tomoq ogrigi uchun foydalaniladi', 34000,50,3,'9-9-2023','1-1-2024',2)")

    cursor.execute("INSERT INTO medicine(name,description,price,quantity,manufacturer_id,realise_date,finish_date,filial_id) VALUES('sitramon','bosh ogrigi uchun qollaniladi', 50000,30,1,'17-9-2023','28-1-2024',2)")



    cursor.execute("INSERT INTO receipt(customer_id,medicine_id,receipt,staff_id) VALUES(2,1,'3 maxal bittadan ovaqattdan keyin',1)")

    cursor.execute("INSERT INTO receipt(customer_id,medicine_id,receipt,staff_id) VALUES(1,2,'2 maxal bittadan ovaqat bilan  1 hafta',2)")

    postgres_conn.commit()
    print("INSERT 0 1")

