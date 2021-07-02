import random
import time

#Se define la clase principal de del pokemon, la cual va a contener El nombre del pokemon sus puntos de vida

class Pokemon(object):#Las clases siempre van con mayusculas
	def __init__(self,nombre):#cuando se pone init los valores que se inician aqui de manera definida son los que toma la clase si necesidad de colocarlos en la clase
		self.nombre=nombre
		self.hp=100
		
		
#Clase Fuego	
	
class Fuego(Pokemon): #Recuerdas que cuando se declara una clase se ponen en los parentecis los parametros que se va a utilizar, en este casos como el obejto del que se van a heredar son de Pokemon se colacan de ahi mismo que es nombre y así.
	def __init__(self,nombre):#Se coloca el valor nombre porque es la variable que usamos de la clase padre
		super(Fuego,self).__init__(nombre)#Llama el __init__ de la clase padre y mandamos pedir los parametros que queremos, en este caso mandamos llamr el nombre de la clase padre
		
		
	def Llamarada(self):
		return random.randint(0,13)# Se importa la librería random y dentro de random existe una función randint que es para dar un numero ale
	
	def Bola(self):
		return random.randint(0,11)
		
	
		
#Clase planta			
		
class Planta(Pokemon):
	def __init__(self,nombre):
		super(Planta,self).__init__(nombre)
		
		
	def Latigo(self):
		return random.randint(0,13) # Se importa la librería random y dentro de random existe una función randint que es para dar un numero ale
	
	def Polenizacion(self):
		return random.randint(0,11)
	
	
#Definicon de la doble clase

class FP(Fuego,Planta):#Se Colocan las dos Clases de las cuales se va heredar, Fuego y Planta en este caso como solo necesitamos el nombre del pokemo este cacha y pide a fuego y planta 
	def __init__(self,nombre):
		super(FP,self).__init__(nombre)
	def Destello(self):
		return random.randint(0,17)
		

########## Código Principal #############

	valor=0
	m=0
	c=0
while(1):
	print(" ")
	print("     Ahora solo tienes estos pokemons ")
	print(" ")
	print('1. Charmander, 2. Chicorita, 3. ChicoFlama')
	print(" ")
	valor=input(' Selecciona la Pokebola ')
	print(" ")
	valor=int(valor)



	if valor == 1:
		print("Charmander preparado para el ataque")
		v2=input(' Selecciona un 1. Llamarada 2. Bola de Fuego ')
		print(" ")
		v2=int(v2)
		if v2 == 1:
			c=Fuego("Charmander").Llamarada()
			print("Llamarada con valor de", c)
			print(" ")
		elif v2 == 2:
			c=Fuego("Charmander").Bola()
			print("Bola con valor de", c)
			print(" ")
		else:
			print("NO ESCOGISTE NINGUN ATAQUE Valido")
			print(" ")
			
	elif valor ==2:
		print("Chicorita preparado para el ataque")
		print(" ")
		v2=input(' Selecciona un 1. Latigo 2. Polenizacion ')
		print(" ")
		v2=int(v2)
		if v2 == 1:
			c=Planta("Chicorita").Latigo()
			print("Latigo con valor de", c)
			print(" ")
		elif v2 == 2:
			c=Planta("Chicorita").Polenizacion()
			print("Polenizacion de", c)
			print(" ")
		else:
			print("NO ESCOGISTE NINGUN ATAQUE Valido")
			print(" ")
			
	elif valor ==3:
		print("Chicoflama preparado para el ataque")
		print(" ")
		v2=input(' Selecciona un 1. Llamara 2. Bola de Fuego, 3. Latigo 4. Polenizacion 5.Destello ')
		print(" ")
		v2=int(v2)
		if v2 == 1:
			c=FP("ChicoFlama").Llamarada()
			print("Llamarada con valor de", c)
			print(" ")
		elif v2 == 2:
			c=FP("ChicoFlama").Bola()
			print("Bola de Fuego de", c)
			print(" ")
		
		elif v2 == 3:
			c=FP("Chicoflama").Latigo()
			print("Latigo con valor de", c)
			print(" ")
		elif v2 == 4:
			c=FP("ChicoFlama").Polenizacion()
			print("Polenizacion de", c)
			print(" ")
		
		elif v2 == 5:
			c=FP("Chicoflama").Destello()
			print("Destello de", c)
			print(" ")
			
			
		else:
			print("NO ESCOGISTE NINGUN ATAQUE Valido")
	print(" ")
	print("     Tu contrincante tiene va a seleccionar su jugada ")
	print('1. Pyro, 2. Plantita, 3. Pyroplantita')
	print(" ")
	b=random.randint(1,3)

	b=int(valor)
	time.sleep(3)

	if b == 1:
		print("Pyro preparado para el ataque")
		print(' Tipos de ataques 1. Llamara 2. Bola de Fuego ')
		v22=random.randint(1,2)
		time.sleep(1)
		if v22 == 1:
			m=Fuego("Pyro").Llamarada()
			print("Llamarada con valor de", m)
		elif v22 == 2:
			m=Fuego("Pyro").Bola()
			print("Bola con valor de", m)
		else:
			print("NO ESCOGISTE NINGUN ATAQUE Valido")
		print(" ")		
	elif b ==2:
		print("Plantita preparado para el ataque")
		print(' Tipos de ataques 1. Latigo 2. Polenizacion ')
		v22=random.randint(1,2)
		time.sleep(1)
		if v22 == 1:
			m=Planta("Plantita").Latigo()
			print("Latigo con valor de", m)
		elif v22 == 2:
			m=Planta("Plantita").Polenizacion()
			print("Polenizacion de", m)
		else:
			print("NO ESCOGISTE NINGUN ATAQUE Valido")
		print(" ")	
	elif b ==3:
		print("Pyroplantita preparado para el ataque")
		print(' Tipos de ataques1. Llamara 2. Bola de Fuego, 3. Latigo 4. Polenizacion 5.Destello ')
		v22=random.randint(1,5)
		time.sleep(1)
		v22=int(v22)
		if v22 == 1:
			m=FP("Pyroplantita").Llamarada()
			print("Llamarada con valor de", m)
		elif v22 == 2:
			m=FP("Pyroplantita").Bola()
			print("Bola de Fuego de", m)
		
		elif v22 == 3:
			m=FP("Pyroplantita").Latigo()
			print("Latigo con valor de", m)
		elif v22 == 4:
			m=FP("Pyroplantita").Polenizacion()
			print("Polenizacion de", m)
		
		elif v22 == 5:
			m=FP("Pyroplantita").Destello()
			print("Destello de", m)
			
			
		else:
			print("NO ESCOGISTE NINGUN ATAQUE Valido")
		print(" ")
			
	time.sleep(1)

	if c<m:
		print("Gano la Maquina")
		print(" ")
	else:
		print("Ganaste")
	print("")