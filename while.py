#control de notas WHILE
cantidad = 0
suma = 0
aprobado = 0
desaprobado = 0
nota_mayor = 0
nota = int(input("ingrse notas"))
while nota!= -1:
  if nota<0 or nota >20:
     print("nota no valida")
  else:
        cantidad = cantidad +1 #contador 
        suma = suma+nota #acumulador
        if nota>=11:
         aprobado = aprobado + 1 #incrementar el numero de aprobados 
        else:
           desaprobado = desaprobado +1
        if nota>nota_mayor:
           nota_mayor = nota
  nota = float(input("ingrese un nota -1 para TERMINAR")) 

print ("\n =========RESULTADO=========")
print ("estudiantes resgistrado: ", cantidad)
print ("aprobados: ", aprobado )
print ("desaprobados: ", desaprobado )
print ("la nota mayor es : ", nota_mayor)