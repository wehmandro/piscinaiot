# -*- coding: latin-1 -*-

#PARA USAR EM GALILEO GEN1
#from configuraPCI import *
#from sensores import *

#PARA USAR EM Raspberry
from configuraPCIrasp import *
from sensoresrasp import *


import db_sqlite
'''
lcd.setCursor(0, 0)
lcd.write("teste Galileo")
texto1=""
texto2=""
dados = [ "", "", "", ""]
'''
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/botoes")
def botoes():
    return render_template("botoes.html")

@app.route("/sensores")
def sensores():

    celsius=leitura_temperatura()
    print ('Valor lido AN temp na principal = {}\n'.format(celsius))# - Funcionando
    '''
    ph=leitura_pot()
    #ph = ("{:.1f}".format(leitura_pot()))
    print ('valor do PH: {}\n'.format(ph))
    psi1=leitura_pot2()
    #psi1 = ("{:.1f}".format(leitura_pot2()))
    print 'Valor lido Pressao 1 = ',psi1,'\n'
    psi2=leitura_pot3()
    #psi2 =("{:.1f}".format(leitura_pot3()))
    print 'Valor lido Pressao 2 = ',psi2,'\n'
    '''
    ph=7.8
    psi1=32.2
    psi2=24.5
    valores1 = [celsius, ph , psi1 , psi2]
    lista1 = ["Temperatura", "PH", "psi", "psi"]
    #texto1 = ("Temp: {}      ".format(celsius))
    #texto2=("pH: {}      ".format(ph))
    #escreve_lcd(texto1, texto2)
    return render_template("sensores.html", valores1=valores1, lista1=lista1)

@app.route("/web")
def web():
    temperatura_opw = piracicaba.temperatura()
    pressao_opw = piracicaba.pressao()
    humidade_opw = piracicaba.humidade()
    vento_opw = piracicaba.vento_speed()
    valores2 = [temperatura_opw, pressao_opw, humidade_opw, vento_opw]
    lista2 = ["Temperatura", "Pressao", "Humidade", "Ventos"]
    return render_template("web.html", valores2=valores2, lista2=lista2)

@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/servo/<val_servo>")
def servo(val_servo):
    temp = int(val_servo)
    if temp > 180 :
        val_servo = 180
        temp = 180
    elif temp < 0 :
        val_servo = 180
        temp = 180
    else:
        print "val_servo: ", val_servo

    if temp <= 180 :
        posicao = int(val_servo)
        move_servo(posicao)
        angulo = posicao
        print "valor: ", val_servo
        print "pos: ", posicao
        print "ang: ", angulo
        texto2=("Servo: {}".format(angulo))
	#escreve_lcd(texto1, texto2)
    return render_template("servo.html", val_servo=val_servo)

@app.route("/led/<val_led>")
def led(val_led):
    status = int(val_led)

    if status == 1:
		liga_led()
		texto2="Led Ligado      "
		escreve_lcd(texto1, texto2)
    else:
		desliga_led()
		texto2 = "Led Desligado   "
		escreve_lcd(texto1, texto2)
    return ('OK', 200)

@app.route("/rele/<val_rele>")
def rele(val_rele):
    status = int(val_rele)

    if status == 1:
       liga_rele()
       texto2="Rele Ligado     "
       escreve_lcd(texto1, texto2)
    else:
		desliga_rele()
		texto2="Rele Desligado  "
		escreve_lcd(texto1, texto2)
    return ('OK', 200)


@app.route('/graficos')
def graficos():
    valores = db_sqlite.retorna_dados_sensores()
    return render_template('graficos.html', valores=valores)


@app.route('/update_potenciometro')
def update_potenciometro():
    data[0] = ("{:.1f}".format(leitura_temperatura())) #temperatura
    data[1] = ("{:.1f}".format(leitura_pot()))			#ph
    data[2] = ("{:.1f}".format(leitura_pot2()))		#motor1
    data[3] = ("{:.1f}".format(leitura_pot3()))		#motor2

    #texto1=("pH: {}      ".format(dados[1]))
    #texto2=("M1:{} psi   ".format(dados[2]))
    #escreve_lcd(texto1, texto2)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
