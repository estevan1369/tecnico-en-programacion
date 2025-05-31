#ejercicio 1
# pe=(input("ingrese el nombre del producto:", ))
# pr=(float(input("ingrese el presio:", )))        #solicita datos
# ca=(int(input("ingrese la cantidad a comprar:", )))
# tup=(pe , pr)
# lis=[tup , ca]
# diccionario={
#     "producto":lis    #diccionario con lista como valor

# }
# costo_total=pr * ca     #calcula el costo total
# print(f"nombre:{pe}")
# print(f"presio unitario:{pr}")
# print(f"cantidad comprada:{ca}")
# print(f"costo total:{costo_total}")

#ejercicio 2
# nombre=(input("ingrese el nombre del producto:", ))
# costo=(float(input("ingrese el costo:", )))   #ingreso de datos para el producto 1
# cantidad=(int(input("ingrese la cantidad:", )))

# nombre1=(input("ingrese el nombre del producto:", ))
# costo1=(float(input("ingrese el costo:", )))   #ingreso de datos para el producto 2
# cantidad1=(int(input("ingrese la cantidad:", )))

# nombre2=(input("ingrese el nombre del producto:", ))
# costo2=(float(input("ingrese el costo:", )))   #ingreso de datos para el producto 3
# cantidad2=(int(input("ingrese la cantidad:", )))

# producto=[(nombre,costo),cantidad]
# producto1=[(nombre1,costo1),cantidad1]   #crear tupla para cada producto
# producto2=[(nombre2,costo2),cantidad2]

# factura={
#     "producto6":producto,
#     "producto5":producto1,   #guardamos en el diccionario
#     "producto7":producto2
# }

# total1=costo*cantidad
# total2=costo1*cantidad1     #calcular total de todo
# total3=costo2*cantidad2

# costo_total=total1+total2+total3  #coste total de la factura

# print(f"{nombre}:{costo}*{cantidad}:{total1}")
# print(f"{nombre1}:{costo1}*{cantidad1}:{total2}")   #factura
# print(f"{nombre2}:{costo2}*{cantidad2}:{total3}")
# print(f"total general:{costo_total}")

# ejercicio 3

# estudiante=(input("ingresar el nombre del estudiante:", ))
# mat_1=(input("nimbre de la primera materia:", ))
# not_1=(float(input(ingrese la primera nota, )))   #ingreso de notas 
# not_2=(float(input(ingrese la segunda nota, )))

# mat_2=(input("nimbre de la primera materia:", ))
# not_3=(float(input(ingrese la primera nota, )))
# not_4=(float(input(ingrese la segunda nota, )))

# mat_3=(input("nimbre de la primera materia:", ))
# not_5=(float(input(ingrese la primera nota, )))
# not_6=(float(input(ingrese la segunda nota, )))

# asig_1=(mat_1, not_1, not_2//2)
# asig_2=(mat_2, not_3, not_4//2)    #promedio de las notas 
# asig_3=(mat_3, not_5, not_6//2)

# agrupacion_1=[asig_1, not_1, not_2]
# agrupacion_2=[asig_2, not_3, not_4]     #agrupacion 
# agrupacion_3=[asig_3, not_5, not_6]

# registro={
#     "nombre": estudiante,
#     "mat_1": agrupacion_1,
#     "mat_2": agrupacion_2,
#     "mat_3": agrupacion_3
# }

# promedio_final= not_1 + not_2 + not_3 + not_4 + not_5 + not_6//6

# print(f"el estudiante {estudiante} en la materiade {mat_1} tuvo las siguientes calificaciones {not_1} y {not_2}, en la materia {mat_2} tuvo las siguientes calificaciones {not_3} y {not_4} y en la materia de {mat_3} tuvo las siguientes calificaciones {not_5} y { not_6} con un promedioo de {prpomedio_final}")