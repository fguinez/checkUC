num=input('Inserte número de alumno: ')
#18628834-mecepeda
num = num[:7]
num = num[::-1]
i = 0
sum = 0

while i < 7:
    sum += int(num[i]) * (i + 2)
    i += 1

verificador = 11 - (sum % 11)
if verificador == 10:
    verificador = 'J'

print(verificador)

