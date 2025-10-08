from datetime import datetime, date, time;
import locale
#Objeto do tipo datetime

hoje = datetime.now()
data_formatada = hoje.strftime("%d/%m/%Y")  #produz 28/11/2024
hora_formatada = hoje.strftime("%H:%M:%S")  #produz 15:20:59
print("\nData formatada:", data_formatada)
print("Hora formatada:", hora_formatada)
print(f"\nFormato de data de retornado pela função 'now'.\nDia de hoje: !!{hoje}!!\n")

formato = "%d/%m/%Y %H:%M:%S"
data_hora_formatada = hoje.strftime(formato)
print("Data e hora formatadas:", data_hora_formatada)  #produz 28/11/2024 15:20:59

# Definindo a localização para o Brasil - pt_BR.UTF-8
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
hoje = datetime.now()

data_formatada = hoje.strftime("%x")
hora_formatada = hoje.strftime("%X")
print("Data formatada: ", data_formatada)
print("Hora formatada:", hora_formatada)

