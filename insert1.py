from sindesi1 import get_connection

def insert_game(GameName,year,CompanyName):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO games(GameName,year,CompanyName) values()"
    values = (GameName,year,CompanyName)
    cursor.execute(query, values)
    print("To paixnidi prostethike")
    cursor.close()
    connection.close

GameName= input("dwse onoma paixnidiou: ")
year=int(input("eisagetai etos: "))
CompanyName=input("eiasgetai etairis: ")

insert_game(GameName,year,CompanyName)
