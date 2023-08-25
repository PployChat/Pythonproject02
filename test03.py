#รับค่า ป้อนทางแป้นพิมพ์ ใช้ input() เป็น string

#ตัวแปร variable เป็น identifler มีหน้าที่เก็บข้อมูลในโปรแกรม ข้อมูลที่เก็บอยู่ใน RAM
#identifler คือ ชื่อที่ dev.ตั้งชื่อมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn =  input('ป้อนปีเกิด :') #สิ่งที่ต้องป้อนทั้งหมดถือเป็น String
print('--------------------------')
stdAge = 2023 - int (stdYearBorn) #ต้องแปลง String เป็น number -> int(),float()
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
print(f"คุณเกิดปี {stdYearBorn} อายุ {stdAge}")
print('--------------------------')
print("ยินดีต้อนรับ" ,std_id, "ชื่อ" ,std_name,)#ใช้ ,
print("คุณเกิดปี" ,stdYearBorn, "อายุ" ,stdAge,)
print('--------------------------')
print("ยินดีต้อนรับ"+' '+str(std_id)+' '+"ชื่อ"+' '+str(std_name))#ใช้ +
print("คุณเกิดปี"+' '+str(stdYearBorn)+' '+"อายุ"+' '+str(stdAge))#ใช้
print('--------------------------')
print("ยินดีต้อนรับ {} ชื่อ {} ".format(std_id,std_name))#ใช้ เมธอด format
print("คุณเกิดปี {} อายุ {} ".format(stdYearBorn,stdAge))
print('--------------------------')
print("ยินดีต้อนรับ %s ชื่อ %s" %(std_id,std_name))#ใช้ %
print("คุณเกิดปี %s อายุ %s" %(stdYearBorn,stdAge))
