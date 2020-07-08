#-- coding: utf-8--
def convertir_integer(valor):
  numero_int= int (valor)
  return numero_int


respuesta="si" #flag
while respuesta!="no":
   print (''' 
CALCULADORA BASICA ----->
1) SUMAR
2) RESTAR
3) MULTIPLICAR
4) DIVIDIR
5) SALIR*''')
   opcion=convertir_integer(input("Ingrese el numero de su opcion: "))
  #  opcion=convertir_integer(opcion) # int para convertir str a int
   if opcion>0 and opcion<5:
      primer_numero=int (input("Ingrese un Numero: "))
      segundo_numero=int (input("Ingrese otro Numero: "))
      if opcion == 1:
         suma=primer_numero+segundo_numero
         print("SUMA: ", suma)
      elif opcion == 2:
         resta=primer_numero-segundo_numero
         print("RESTA: ", resta)
      elif opcion == 3:
         multiplicacion=primer_numero*segundo_numero
         print("MULTIPLICACION: ", multiplicacion)
      elif opcion == 4:
         if segundo_numero==0:
            print("ERROR")# un valor no puede dividirse para cero
         else:
            division = primer_numero/segundo_numero
            print("DIVISION", division)
   elif opcion == 5:
      print("HASTA LUEGO!")
      respuesta="no" #flag de salida del while
