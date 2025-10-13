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

def convert_frase():
    conversao = 

#8. Crie um programa que adiciona 7 dias à data atual.

#9. Crie um programa que subtraia 30 dias da data atual.

'''10. Crie uma função que receba duas datas diferentes como parâmetro. A função deve
retornar um valor inteiro que represente a diferença entre essas datas passadas por
parâmetro.'''


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

  

