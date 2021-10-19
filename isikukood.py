ik=""
while len(ik)!=11 or ik.isdigit()!=True:
	try:
	    ik=input("Введите личный код:")
	except ValueError:
	    print("Не правильный введите еще раз!!!")
print("Анализ личного кода:".center(50,"-"))
print("Первый символ:")
ik_list=list(ik)
if int (ik_list[0]) not in [1,2,3,4,5,6]:
    print(ik_list[0],"- не правильно!")
else:
	print(ik_list[0],"- правильно!")
	kuu=ik_list[3]+ik_list[4]
	kuu=int(kuu)
	if kuu>0 and kuu<13:
		print(ik_list[3],ik_list[4],"- правильный месяц!")
		paev=int(ik_list[5]+ik_list[6])
		if int(ik_list[0])==1 or int(ik_list[0])==2:
			aasta=int("18"+ik_list[1]+ik_list[2])
		elif int(ik_list[0])==3 or int(ik_list[0])==4:
			aasta=int("19"+ik_list[1]+ik_list[2])
		elif int(ik_list[0])==5 or int(ik_list[0])==6:
			aasta=int("20"+ik_list[1]+ik_list[2])

		if kuu in [1,3,5,7,8,10,12] and paev>0 and paev<32:
			print(ik_list[5],ik_list[6],"- правильный день!")
		elif (kuu in [4,6,9,11] and paev>0 and paev<31) or (kuu ==2 and paev>0 and paev<29):
			print(ik_list[5],ik_list[6],"- правильный день")
		elif aasta % 4==0 and kuu ==2 and paev>0 and paev<30:
			print(ik_list[5],ik_list[6],"- правильно! 29 фев.")
		else:
			print(ik_list[5],ik_list[6],"Правильный день!")
	else:
		print(ik_list[3],ik_list[4],"правильный месяц!")

Summa=0
for i in range(1,11):
	if i==10:
		i=1
	Summa+=i*int(ik_list[i-1])
print("Summa", Summa)
jaak=Summa//11
if jaak==10:
	Summa=0
	for i in range(3,13):
		if i<9:
			Summa+=i*int(ik_list[i-1])
		else:
			Summa+=(i-8)*int(ik_list[i-1])
	jaak=Summa//11
jaak=Summa-jaak*11
print("Kontroolnumbr:", jaak)
if jaak==(ik_list[10]):
	print("Isisukood on õige!!!!")
else:
	print("Isisukood on vale!!!!")
	print("Isisukood on vale!!!!")
