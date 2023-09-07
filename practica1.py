import csv
#-------------------------------------------------------------------
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def obtener_fecha(self):
        return f"{self.dia}/{self.mes}/{self.año}"
    
    def cambiar_fecha(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
#--------------------------------------------------------------------
mi_fecha_de_nacimiento = Fecha(21,9,2004)    
print("Dia:", mi_fecha_de_nacimiento.dia)
print("Mes:", mi_fecha_de_nacimiento.mes)  
print("Año:", mi_fecha_de_nacimiento.año)  
print("Fecha:", mi_fecha_de_nacimiento.obtener_fecha())

mi_fecha_de_nacimiento.cambiar_fecha(4,9,2023)

print("El dia de hoy cae:", mi_fecha_de_nacimiento.obtener_fecha())
#--------------------------------------------------------------------
fechas_de_nacimiento = []
with open('datos.csv', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)

    for fila in lector_csv:
        fecha_de_nacimiento = fila['Fecha de nacimiento'].split('/')
        dia, mes, año = map(int, fecha_de_nacimiento)
        fecha_objeto = Fecha(dia,mes,año)

        fechas_de_nacimiento.append(fecha_objeto)
#-----------------------------------------------------------------------

for fecha in fechas_de_nacimiento:
    print('Fecha de nacimiento:', fecha.obtener_fecha())

    

                  
