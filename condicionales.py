#variable
#claficaciones 20-17 ->A ...
nota = int(input("imgrese una nota"))
if nota >= 1 and nota <=10:
   calificacion = "D" 
elif nota>=11 and nota <=13:
  calificacion = "C" 
elif nota <= 14 and nota <= 17: 
 calificacion = "B"
elif nota >= 18 and nota <=20:
  calificacion = "A"
else:
   print("ingrse una nota valida-> entre 1 y 20")

print("le corresponde una calificacion:" , calificacion)