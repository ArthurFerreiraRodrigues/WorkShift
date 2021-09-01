import calendar

year = int(input("Digite o Ano : "))
monthStart = int(input("Digite o Mês de Início : "))
monthFinish = int(input("Digite o Mês de Término : "))
totalTime = monthFinish - monthStart

name = input("Nome do(s) Monitor(es) (Ex: Arthur,Ferreira) : ").split(",")
quant = len(name)

# Initialize a tridimensional matrix -> [IdexOfName[DaysInTimeWindow[Day,month,year]]]
work_shift = [[[0 for k in range(3)] for j in range(
    31*totalTime)] for i in range(quant)]

distDays = input(
    "\nDias da Semana a Serem Distribuídos \n(Ex : 0,2,6 - Onde 0 é Segunda e 6 é Domingo) : ").split(",")
distDays = list(map(int, distDays))


inCharge = 0  # In charge of this especific day
totalWorkLoad = [0 for i in range(quant)]  # Quantity of days registered / Name
for month in range(monthStart, monthFinish):
    # for weekday->0,2,3 = Monday, Wednesday, Thursday
    for day in range(1, calendar.monthlen(year, month)+1):
        weekday = calendar.weekday(year, month, day)
        if(weekday in distDays):
            work_shift[inCharge][totalWorkLoad[inCharge]][0] = day
            work_shift[inCharge][totalWorkLoad[inCharge]][1] = month
            work_shift[inCharge][totalWorkLoad[inCharge]][2] = year
            totalWorkLoad[inCharge] += 1
            inCharge += 1
            if(inCharge == quant):
                inCharge = 0

print(work_shift)
