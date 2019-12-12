import RPi.GPIO as GPIO
import urllib2
import urllib
from time import sleep
import json
pinTecla = 18
pinLuz = 17
pinEnchufe = 27
GPIO.setwarnings(False)
#configurando pines como salida o entradas
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinTecla,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinLuz,GPIO.OUT)
GPIO.setup(pinEnchufe,GPIO.OUT) 
#inicializo estados de pines
GPIO.output(pinLuz,True)
GPIO.output(pinEnchufe,True)



class StatusClass:
	#CONSTRUCTOR
	def __init__(self):
		self.reles = {'rele1':0}


def traigoEstadoHost(defaultStatus):
	response = urllib2.urlopen('http://prendeme.com.ar/buttonStatus.php')
	response = response.read()
	defaultStatus.reles = json.loads(response) 
	if flagPost:  
		return status.reles
	return defaultStatus.reles	


def actualizoEstadoHost (defaultStatus):            
	try:
		defaultStatus.reles = copiarObjetos(status, defaultStatus)  
		url = 'http://prendeme.com.ar/buttonRasp.php'
		data = urllib.urlencode(defaultStatus.reles)
		request = urllib2.Request(url, data)
		response = urllib2.urlopen(request).read()
		print "intentando enviar el post"
	except:
		print response
	if response=='ok':
		flagPost = False
		return flagPost
	else:
		return flagPost


def actualizoReles ():
		GPIO.output(pinLuz,True)
	else:
		GPIO.output(pinLuz,False)


def apretoTecla(pinTecla):
	global estadoBoton
	if GPIO.input(pinTecla) != estadoBoton:
		sleep(0.25) #espera 200ms
		if GPIO.input(pinTecla) != estadoBoton:
			global status
			global flagPost
			if status.reles['rele1'] == 1:
				status.reles['rele1'] = 0
				GPIO.output(pinLuz,False)
			else:
				status.reles['rele1'] = 1
				GPIO.output(pinLuz,True)
			flagPost = True
			estadoBoton = GPIO.input(pinTecla)
	

def diferentes(hostStatus,auxStatus):
	for indice in hostStatus.reles:
		if hostStatus.reles[indice] != auxStatus.reles[indice]:
			return True
	return False


def copiarObjetos(objetoReferencia, objetoModificar):
	for indice in objetoModificar.reles:
		objetoModificar.reles[indice] = objetoReferencia.reles[indice]
		return objetoModificar.reles




##Declaraciones
auxStatus = StatusClass()
defaultStatus = StatusClass()
status = StatusClass() 
hostStatus = StatusClass() 
flagPost = False 
hostStatus.reles = traigoEstadoHost(defaultStatus) 
status.reles = copiarObjetos(hostStatus,status)
auxStatus.reles = copiarObjetos(hostStatus,auxStatus)
actualizoReles()	
estadoBoton = GPIO.input(pinTecla)
u = 0

#interrupcion
GPIO.add_event_detect(pinTecla, GPIO.BOTH, callback=apretoTecla) 																		

#Programa principal
while True:
	u=u+1
	try:
		if flagPost:
			flagPost = actualizoEstadoHost(defaultStatus)
			pass
		else:
			hostStatus.reles = traigoEstadoHost(defaultStatus)
			if diferentes(hostStatus,auxStatus):			
				status.reles = copiarObjetos(hostStatus,status)
				actualizoReles()
				auxStatus.reles = copiarObjetos(hostStatus,auxStatus)	
	except:
		print "algo fallo en el programa principal"