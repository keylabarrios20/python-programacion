peso=float(input("ingrese su peso en kg: /n"))
altura= float(input("ingrese su altura en m: /n"))

indice=float(peso/altura**2)

if indice<18.5:
 print("peso bajo")

 if 18.5<=indice and indice<25:
  print("peso normal")

 if 25<=indice and indice<30:
  print("sobrepeso")

 if 30<=indice and indice<40:
  print("obesidad")

 else:
   print("obesidad morbida")
