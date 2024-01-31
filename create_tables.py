from connection import postgres_conn
cursor = postgres_conn.cursor()

def create_tables():

    cursor.execute("""CREATE TABLE region(
                   region_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE address(
                   address_id SERIAL NOT NULL PRIMARY KEY,
                   address VARCHAR(60) NOT NULL,
                   district VARCHAR(60) NOT NULL,
                   region_id INT NOT NULL REFERENCES region(region_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE manufacturer(
                   manufacturer_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(60) NOT NULL,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE customer(
                   customer_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   phone VARCHAR(20) NOT NULL,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE staff(
                   staff_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   email VARCHAR(30) NOT NULL,
                   phone VARCHAR(20) NOT NULL,
                   start_work_at TIME NOT NULL,
                   end_work_at TIME NOT NULL,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")
    

    cursor.execute("""CREATE TABLE filial(
                   filial_id SERIAL NOT NULL PRIMARY KEY,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   weekend_day INT NOT NULL,
                   work_start TIME NOT NULL,
                   work_finish TIME NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE staff_filial(
                   filial_id INT NOT NULL REFERENCES filial(filial_id),
                   staff_id INT NOT NULL REFERENCES staff(staff_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE medicine(
                   medicine_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(60) NOT NULL,
                   description TEXT NOT NULL,
                   price NUMERIC(8,2) NOT NULL,
                   quantity INT NOT NULL,
                   manufacturer_id INT NOT NULL REFERENCES manufacturer(manufacturer_id),
                   realise_date DATE NOT NULL,
                   finish_date DATE NOT NULL,
                   filial_id INT NOT NULL REFERENCES filial(filial_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE receipt(
                   receipt_id SERIAL NOT NULL PRIMARY KEY,
                   customer_id INT NOT NULL REFERENCES customer(customer_id),
                   medicine_id INT NOT NULL REFERENCES medicine(medicine_id),
                   receipt TEXT NOT NULL,
                   staff_id INT NOT NULL REFERENCES staff(staff_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    postgres_conn.commit()
    print("CREATE TABLE")
