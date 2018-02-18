# -*- coding: latin-1 -*-

#configuraçãao para Galileo GEN1
#from configuraPCI import *
#configuração para Raspberry
from configuraPCIrasp import *
'''
celsius=0
ph=0
psi1=0
psi2=0
sensor_phmetro=0
'''
def leitura_temperatura():
    rs232.write('3')
    temperatura =int(rs232.read(4))
    celsius = temperatura/22.0
    #print (celsius)
    return celsius

def leitura_pot():	#sensor_phmetro
    rs232.write('1')
    adpot=int(rs232.read(4))
    #print ('Valor lido = {}\n'.format(sensor_phmetro))
    ph = adpot*14.0/1023.0
    return ph

def leitura_pot2():	#sensor_pressao1
    #sensor_pressao1= pinos.analogRead(pino_pot2)
    rs232.write('2')
    sensor_pressao1=int(rs232.read(4))
    psi1 = sensor_pressao1*40.0/1023.0
    return psi1

def leitura_pot3():	#sensor_pressao2
    #sensor_pressao2= pinos.analogRead(pino_pot3)
    rs232.write('3')
    sensor_pressao2=int(rs232.read(4))
    psi2 = sensor_pressao2*40.0/1023.0
    return psi2

def liga_rele1():
    pinos.digitalWrite(pino_rele1, 1)

def desliga_rele1():
    pinos.digitalWrite(pino_rele1, 0)

def liga_rele2():
	pinos.digitalWrite(pino_rele2,1)

def desliga_rele2():
	pinos.digitalWrite(pino_rele2,0)

'''
def move_servo(posicao):
    sg_servo.setAngle(posicao)
    angulo = posicao
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.write("Servo: {}".format(angulo))

def escreve_lcd(texto_linha1, texto_linha2):
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.write(texto_linha1)
    lcd.setCursor(1, 0)
    lcd.write(texto_linha2)
'''
