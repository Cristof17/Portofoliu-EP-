N = pow(10, 8)
#N =3 
nume = "rot"
hashPrev = 0

file = open('numere.txt', 'w+')

for x in range (0, N):
	sir = nume + str(x)
	if (x == 0):
		hashPrev = len(sir)
	else:
		hashPrev = hashPrev * 31 + ord(sir[x % len(sir)])
	file.write(str(hashPrev) + " ")
