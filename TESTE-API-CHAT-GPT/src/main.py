from datetime import datetime
from os import getenv 
import dotenv
import openai

dotenv.load_dotenv() 

def request_openai(prompt:str) -> str:
	openai.api_key = getenv('KEY_GPT')
	response = openai.Completion.create(
		model='text-davinci-003',
		prompt= prompt,
		temperature= 0.7,
		max_tokens= 100,
		n=1, 
		stop=None 
	)
	return response['choices'][0]['text'].strip()	

def connect_db()-> pyodbc.Cursor:
	server = getenv('SERVER')
	database = getenv('DATABASE')
	username = getenv('USERNAME')
	password = getenv('PASSWORD')
	driver = getenv('DRIVER')

	conn = pyodbc.connect(f'DRIVER={driver};Server={server};Database={database};User ID={username};Password={password}')
	cursor = conn.cursor()
	return cursor

def inserir_question(cursor: pyodbc.Cursor, date_time_question: datetime.datetime, text_question: str) -> None:
    sql = "INSERT INTO question (date_time_question, text_question) VALUES (?, ?)"
    cursor.execute(sql, (date_time_question, text_question))

def inserir_answer(cursor: pyodbc.Cursor, id_question: int, date_time_answer: datetime.datetime, text_answer: str) -> None:
    sql = "INSERT INTO answer (id_question, date_time_answer, text_answer) VALUES (?, ?, ?)"
    cursor.execute(sql, (id_question, date_time_answer, text_answer))

if __name__ == '__main__':

	prompt = input('What is your question?\n\n')
	time_question = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

	answer = request_openai(prompt)

	print(f'\n{time_question} \n{answer}\n')	