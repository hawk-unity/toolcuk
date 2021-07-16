import os
author="hawk ofcx"
print("""
_______________________
1- nmap ile hafif port tara
2- nmap ile servis versiyon bilgisini al
3- sqlmap ile dbs çek
_______________________
""")
vur = input("Lütfen yapacağınızı seçiniz -> ")
if vur == "1" :
   vur2 = input("ip veya link girin => ") 
   os.system("nmap " + vur2)
if vur == "2" : 
   vur3 = input("ip adresi => ")
   os.system("sudo nmap -sS -sV " + vur3)
if vur == "3":
   vur4 = input("açıklı url => ")
   os.system("sqlmap "+vur4 + "--dbs")
else : 
  print("hatalı fonksiyon ab")
