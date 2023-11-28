# IMPORTANDO BIBLIOTECAS NECESSÁRIAS 
from playsound import playsound

# MÓDULO UTILIZADO PARA REGULAR O TEMPO
import time 

# SEQUÊNCIAS DE ESCAPE PARA LIMPAR E ATUALIZAR O TERMINAL
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# CRIANDO A FUNÇÃO ALARM()
def alarm(seconds):
    # TEMPO ATÉ TOCAR O EFEITO SONORO DO ALARME
    time_elapsed = 0 

    # LIMPA O TERMINAL
    print(CLEAR)

    # LOOP PARA DECORRER O TEMPO
    while time_elapsed < seconds:
        # DEFINIR TEMPO DE ESPERA PARA NÃO EXECUTAR IMEDIATAMENTE
        time.sleep(1)
        # CONTADOR
        time_elapsed += 1

        # MOSTRAR MINUTOS E SEGUNDOS RESTANTES PARA SOAR O ALARME
        time_left = seconds - time_elapsed 
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # IMPRIMIR A IMFORMAÇÃO NA TELA EM CONTAGEM REGRESSIVA
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
        
        # 02d FORMATAÇÃO PARA O ESTILO "00:00"

    # REPRODUZIR EFEITO SONORO 
    playsound("src/sound/alarm.mp3")

# ENTRADA DO USUÁRIO - DEFINIÇÃO DO TEMPO PARA TOCAR O ALARME
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))

# TEMPO TOTAL
total_seconds = minutes * 60 + seconds

# CHAMANDO A FUNÇÃO ALARM()
alarm(total_seconds)