import pyodbc 

'''
dados_conexao = (
    "Driver={SQL Server};"
    "Server=200.141.72.206,7027.database.windows.net;"
    "Database=teste_desenvolvedor;"
)
# <server>.database.windows.net
# 200.141.72.206,7027
conn = pyodbc.connect(dados_conexao)

print('SUCESSO!')   
'''

######################################


import pyodbc 


server = 'tcp:200.141.72.206,7027.database.windows.net'
database = 'teste_desenvolvedor'
username = 'teste_desenvolvedor_usr'
password = '@123A'
driver = '{ODBC Driver 17 for SQL Server}'
# Devart ODBC Driver for SQLAzure



#';UID=' + username
#Port=myport;

data_conn = f'DRIVER={driver};Server={server};Database={database};User ID={username};Password={password}'

cnxn = pyodbc.connect(data_conn)
cursor = cnxn.cursor()

data = '2023-06-07 10:00:00'
r = 'Qual é a capital do Brasil?'

cursor.execute(f"INSERT INTO EMP (date_time_question, text_question) VALUES ({data},{r})") 



# cursor.execute("SELECT * FROM EMP") 
# row = cursor.fetchone() 
# while row:
#     print (row) 
#     row = cursor.fetchone()


