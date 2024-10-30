usuario = {"nombre": "Luis", "apellido":"Fandiño", "edad": 22}
print(usuario["nombre"]) #imprime la variable que uno indique

usuario["profesion"] = "desarrollador de software"
print(usuario)
listaClaves = usuario.keys()
del usuario["apellido"]
print(listaClaves)

usuario.values()
usuario.update({"ciudad": "Madrid"})
print(usuario)