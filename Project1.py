import hashlib

class Block:
    #กำหนดโครงสร้าง Block
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    #สร้างค่า Hash
    def calculate_hash(self):
        block_header = str(self.transactions) + str(self.previous_hash)
        return hashlib.sha256(block_header.encode()).hexdigest()

class Blockchain:
    #สร้าง Genesis Block
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    #ข้อมูลที่จะถูกนำเข้าไปใส่ใน Genesis Block
    def create_genesis_block(self):
        return Block(["111", "Alice", 5, 30, "โคราช", 235.5, "061-778-6969" ], "0")

    #สร้าง Block ขึ้นมาใหม่
    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)

    #แสดงข้อมูลตาม Block ที่รับเข้ามา
    def display_chain(self, block_index):
        block = self.chain[block_index]
        print("")
        print(f"บล็อคที่: {block_index}")

        print(f"หมายเลข: {block.transactions[0]}")
        print(f"เจ้าของ: {block.transactions[1]}")
        print(f"จำนวนอาคาร: {block.transactions[2]}")
        print(f"จำนวนชั้น: {block.transactions[3]}")
        print(f"สถานที่ตั้ง: {block.transactions[4]}")
        print(f"พื้นที่ใช้สอย: {block.transactions[5]}")
        print(f"เบอร์โทรติดต่อ: {block.transactions[6]}")

        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print("")

    #แสดงข้อมูล Block ที่มีอยู่ทั้งหมด
    def display_all_chain(self):
        for i, block in enumerate(self.chain):
            print("********")
            print(f"บล็อคที่: {i}")

            print(f"หมายเลข: {block.transactions[0]}")
            print(f"เจ้าของ: {block.transactions[1]}")
            print(f"จำนวนอาคาร: {block.transactions[2]}")
            print(f"จำนวนชั้น: {block.transactions[3]}")
            print(f"สถานที่ตั้ง: {block.transactions[4]}")
            print(f"พื้นที่ใช้สอย: {block.transactions[5]}")
            print(f"เบอร์โทรติดต่อ: {block.transactions[6]}")

            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("")

    #เพิ่ม Data (Transaction) เข้าไปใน Block
    def add_transaction(self):
        transactions = []
        print("---------------------------------------")
        id = input("ใส่ข้อมูลหมายเลขคอนโดมิเนียม: ")
        transactions.append(id)
        owner = input("ใส่ข้อมูลชื่อเจ้าของ: ")
        transactions.append(owner)
        building = int(input("ใส่จำนวนอาคาร: "))
        transactions.append(building)
        floor = int(input("ใส่จำนวนชั้น: "))
        transactions.append(floor)
        location = input("ใส่สถานที่ตั้ง: ")
        transactions.append(location)
        area = float(input("ใส่พื้นที่ใช้สอยทั้งหมด (ตร.ม.) : "))
        transactions.append(area)
        phone = input("ใส่เบอร์โทรติดต่อ:")
        transactions.append(phone)
        print("---------------------------------------")
        self.add_block(transactions)
    
    #แก้ไข Data (Transaction) ใน Block ที่เลือก
    def edit_transaction(self, block_index, new_id, new_owner, new_building, new_floor, new_location, new_area, new_phone):
        block = self.chain[block_index]
        block.transactions[0] = new_id
        block.transactions[1] = new_owner
        block.transactions[2] = new_building
        block.transactions[3] = new_floor
        block.transactions[4] = new_location
        block.transactions[5] = new_area
        block.transactions[6] = new_phone
        block.hash = block.calculate_hash()
    
    #เช็คว่าค่า Hash มีการเปลี่ยนแปลงหรือไม่
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

blockchain = Blockchain()

while True:
    #แสดงฟังก์ชันต่างๆของระบบ
    print("======================================================")
    print("เลือกฟังก์ชั่นที่จะใช้งาน")
    print("1. เพิ่มข้อมูล")
    print("2. แสดงข้อมูลในคอนโดแบบเลือก Block")
    print("3. แสดงข้อมูลทั้งหมดในระบบ")
    print("4. แก้ไขข้อมูลของคอนโด")
    print("5. ตรวจสอบการว่ามีการแก้ไขข้อมูลหรือไม่")
    print("6. ออกจากโปรแกรม")
    print("======================================================")

    choice = int(input("กรุณาใส่หมายเลขฟังก์ชันที่ต้องการใช้งาน: "))

    if choice == 1:
        blockchain.add_transaction()

    elif choice == 2:
        block_index = int(input("Block ของคอนโดที่ต้องการให้แสดง: "))
        blockchain.display_chain(block_index)
        print("")

    elif choice == 3:
        blockchain.display_all_chain()

    elif choice == 4:
        block_index = int(input("ใส่หมายเลข Block ของคอนโดที่ต้องการแก้ไข: "))
        new_id = input("ใส่หมายเลขคอนโดใหม่: ")
        new_owner = input("ใส่เจ้าของใหม่: ")
        new_building = input("ใส่จำนวนอาคารใหม่: ")
        new_floor = input("ใส่จำนวนชั้นใหม่: ")
        new_location = input("ใส่สถานที่ตั้งใหม่: ")
        new_area = input("ใส่พื้นที่ใช้สอยใหม่ (ตร.ม.): ")
        new_phone = input("ใส่เบอร์โทรศัพท์ใหม่: ")
        print("")
        blockchain.edit_transaction(block_index, new_id, new_owner, new_building, new_floor, new_location, new_area, new_phone)

    elif choice == 5:
        if blockchain.is_valid():
            print("")
            print("ไม่มีการเปลี่ยนแปลงข้อมูล")
            print("")
        else:
            print("")
            print("ตรวจพบการเปลี่ยนแปลงข้อมูล !!!")
            print("")

    elif choice == 6:
        break

    else:
        print("ใส่หมายเลขผิดพลาด")