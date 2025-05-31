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
nombre=(input("ingrese el nombre del producto:", ))
costo=(float(input("ingrese el costo:", )))   #ingreso de datos parael producto 1
cantidad=(int(input("ingrese la cantidad:", )))

nombre1=(input("ingrese el nombre del producto:", ))
costo1=(float(input("ingrese el costo:", )))   #ingreso de datos parael producto 2
cantidad1=(int(input("ingrese la cantidad:", )))

nombre2=(input("ingrese el nombre del producto:", ))
costo2=(float(input("ingrese el costo:", )))   #ingreso de datos parael producto 3
cantidad2=(int(input("ingrese la cantidad:", )))

producto=[(nombre,costo),cantidad]
producto1=[(nombre1,costo1),cantidad1]   #crear tupla para cada producto
producto2=[(nombre2,costo2),cantidad2]

factura={
    "producto6":producto,
    "producto5":producto1,   #guardamos en el diccionario
    "producto7":producto2
}

total1=costo*cantidad
total2=costo1*cantidad1     #calcular total de todo
total3=costo2*cantidad2

costo_total=total1+total2+total3  #coste total de la factura

print(f"{nombre}:{costo}*{cantidad}:{total1}")
print(f"{nombre1}:{costo1}*{cantidad1}:{total2}")
print(f"{nombre2}:{costo2}*{cantidad2}:{total3}")
print(f"total general:{costo_total}")