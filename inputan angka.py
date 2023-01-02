''' sebuah program yang dapat membaca input angka 1-4 lalu mencetak 
penulisan angka tersebut. Misalkan dibaca 1, maka output berupa tulisan “satu”, demikian untuk angka lainnya. Jika angka yang dimasukkan tidak berada di antara 1-4 
maka akan muncul tulisan bahwa angka yang dimasukkan salah. 
2'''

print("masukkan angka 1 sampai 4")

pilihan = input("angka : ")

if pilihan == "1":
	print("satu")
elif pilihan == "2":
	print("dua")
elif pilihan == "3":
	print("tiga")
elif pilihan == "4":
	print("empat")
else:
	print("masukkan angka yang benar")
	
	
	