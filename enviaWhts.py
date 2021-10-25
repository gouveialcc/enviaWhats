# BIBLIOTECAS USADAS PARA ENVIO DE MENSAGEM WHATSAPP
from datetime import datetime
import pywhatkit
import keyboard
import time

# FUNCAO ENVIA MENSAGEM WHATSAPP
def envMensagem():
    mensagem = ('Se você recebeu esta mensagem, o meu código está funcionando!')
    # NUMERO DEVE CONTER O SEGUINTE FORMATO: '+5511912345678'
    contatos = ['+5511912345678', 'NUMERO_2', 'NUMERO_3']
    x = 0
    
    # ENQUANTO TIVER CONTATO ENVIA MENSAGEM
    while x <= 2:
        pywhatkit.sendwhatmsg(contatos[x], mensagem, datetime.now().hour, datetime.now().minute + 2, wait_time=10)
        time.sleep(30)
        keyboard.press_and_release('ctrl + w')
        x = x+1

# EXECUTA A FUNÇÃO ACIMA
envMensagem()