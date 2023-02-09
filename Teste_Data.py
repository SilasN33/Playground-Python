from datetime import time, datetime, timedelta

#Datas
def adicionaData():
  today = datetime.now()
  dia_atual = today - timedelta(days=180)

  while True:
    dia_atual = dia_atual + timedelta(days=30)
    yield  dia_atual.strftime("%Y/%m")

gera_data = adicionaData()
datas = []
for i in range(6):
  data = next(gera_data)
  datas.append(data)


mes1 = datas[0] #6 meses - data atual
mes2 = datas[1]
mes3 = datas[2]
mes4 = datas[3]
mes5 = datas[4]
mes6 = datas[5] #Atual

# Meses
m1_conversao = datetime.strptime(mes1,"%Y/%m")
m1 = m1_conversao.month
m2_conversao = datetime.strptime(mes2,"%Y/%m")
m2 = m2_conversao.month
m3_conversao = datetime.strptime(mes3,"%Y/%m")
m3 = m3_conversao.month
m4_conversao = datetime.strptime(mes4,"%Y/%m")
m4 = m4_conversao.month
m5_conversao = datetime.strptime(mes5,"%Y/%m")
m5 = m5_conversao.month
m6_conversao = datetime.strptime(mes6,"%Y/%m")
m6 = m6_conversao.month

#Laço para iterar com a relação do nome dos meses no cabeçalho da tabela
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

nomes_meses = []
for m in [m1, m2, m3, m4, m5, m6]:
    if m >= 1 and m <= 12:
        nomes_meses.append(meses[m-1])
    else:
        nomes_meses.append("Mês inválido")

#Atribuindo novamente os valores de M para que seja usado na table

m1 = nomes_meses[0]
m2 = nomes_meses[1]
m3 = nomes_meses[2]
m4 = nomes_meses[3]
m5 = nomes_meses[4]
m6 = nomes_meses[5]  

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)



