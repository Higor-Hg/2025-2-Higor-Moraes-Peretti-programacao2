from datetime import datetime, date, time, timedelta

'''
Q1.

Pytz é uma biblioteca do Python que permite calcular fusos horários e
resolver problemas com horários ambíguos no final do horário de verão
O tzdata é um “pacote” de dados do Python que fornece dados de fuso
horário IANA. Ele é principalmente usado pelo módulo “zoneinfo” da
biblioteca padrão, mas também pode ser usado como fonte de dados de fuso
horário para outras bibliotecas de fuso horário.;
'''

#2. Crie um programa que obtenha a data e hora atual usando a classe "datetime";

def data_hora_atual():
  agora = datetime.now()
  return agora


#3. Crie um programa que obtenha a data atual usando a classe "date";

def data_clase_atual():
    hoje = date.today()
    return hoje
 

#4. Crie um programa que crie um objeto "time" representando o horário "14:30:59" e exiba seus atributos;

def data_horario():
    horario = time(14, 30, 59)
    return horario



#5. Crie um programa que formate a data atual no formato "dd/mm/yyyy";

def data_formatada():
  
    data_formatada = date.today().strftime("%d/%m/%Y")
    return data_formatada


'''6. Crie um programa que converta uma string no formato "2023-11-26" para um objeto
"date";'''
def converter_string(data_string):
    
    objeto_datetime = datetime.strptime(data_string, '%Y-%m-%d')
    
    objeto_date = objeto_datetime.date()
    
    return objeto_date

#7. Crie um programa que obtenha o timestamp atual em segundos desde 01/01/1970.
def timestamp_atual():
  
  timestamp = datetime.now().timestamp()
  return timestamp


#8. Crie um programa que adiciona 7 dias à data atual.
def adicionar_dias_data_atual(dias):
  data_atual = date.today()
  nova_data = data_atual + timedelta(days=dias)
  return nova_data



#9. Crie um programa que subtraia 30 dias da data atual.
def subtrair_dias_data_atual(dias):
  
    data_atual = date.today()
    nova_data = data_atual - timedelta(days=dias)
    return nova_data

'''10. Crie uma função que receba duas datas diferentes como parâmetro. A função deve
retornar um valor inteiro que represente a diferença entre essas datas passadas por
parâmetro.'''

def dif_entre_datas(data1, data2):

  diferenca = data2 - data1
  return diferenca.days



#PROGRAMA PRINCIPAL
print("--------------------------------INÍCIO-----------------------------------------------")
#Q2

data_e_hora = data_hora_atual()
print(f"\n\nData e hora atuais: {data_e_hora}")

#Q3
data_atual = data_clase_atual()
print("A data atual é:", data_atual)

#Q4

horario = data_horario()
print ("Horário pré definido:", horario)
print ("Atributos desse Horário(hora):", horario.hour)  
print ("Atributos desse Horário(minuto):", horario.minute)
print ("Atributos desse Horário(segundo):", horario.second)

#Q5
data_frt = data_formatada()
print("Data Atual:", data_frt)

#Q6
data_em_string = "2023-11-26"
data_em_objeto = converter_string(data_em_string)

print(f"String original: {data_em_string}")
print(f"Tipo da string: {type(data_em_string)}")
print("-" * 30)
print(f"Objeto date: {data_em_objeto}")
print(f"Tipo do objeto: {type(data_em_objeto)}")
  
#Q7
timestamp_segundos = timestamp_atual()
print(f"O timestamp atual em segundos é: {timestamp_segundos}")

#Q8
data_futura = adicionar_dias_data_atual(7)
print(f"Data atual: {date.today()}")
print(f"Data daqui a 7 dias: {data_futura}")

#Q9
dias_para_subtrair = 30
data_resultante = subtrair_dias_data_atual(dias_para_subtrair)
print(f"Data atual: {date.today()}")
print(f"Data 30 dias atrás: {data_resultante}")

#Q10
data_inicial = date(2025, 1, 1)
data_final = date(2025, 10, 15)

dias_de_diferenca = dif_entre_datas(data_inicial, data_final)
print(f"A diferença entre as datas é de {dias_de_diferenca} dias.")