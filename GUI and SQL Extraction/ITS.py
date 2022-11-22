import mysql.connector

myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Brokenvessels27",
    port="3306",
    database="b'its'"
)


def query_Sql(a):
    cursor.execute(a)
    users = cursor.fetchall()
    for user in users:
        return user[0], user[4]


cursor = myDb.cursor()


def querySql(prompt):
    match prompt:
        case "Chapter 1":
            sql_select_query1 = "select * from questions where status = 'publish'  and category = 'Chapter1' LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query1)
            attempted(question)
            return question

        case "Chapter 2":
            sql_select_query2 = "select * from questions where status = 'publish'  and category = 'Chapter2' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query2)
            attempted(question)
            return question

        case "Chapter 3":
            sql_select_query3 = "select * from questions where status = 'publish'  and category = 'Chapter3' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query3)
            attempted(question)
            return question

        case "Chapter 4":
            sql_select_query4 = "select * from questions where status = 'publish'  and category = 'Chapter4' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query4)
            attempted(question)
            return question

        case "Chapter 5":
            sql_select_query5 = "select * from questions where status = 'publish'  and category = 'Chapter5' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query5)
            attempted(question)
            return question

        case "Chapter 6":
            sql_select_query6 = "select * from questions where status = 'publish'  and category = 'Chapter6' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query6)
            attempted(question)
            return question

        case "Chapter 7":
            sql_select_query7 = "select * from questions where status = 'publish'  and category = 'Chapter7' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query7)
            attempted(question)
            return question

        case "Chapter 8":
            sql_select_query8 = "select * from questions where status = 'publish'  and category LIKE 'Chapter8%' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query8)
            attempted(question)
            return question

        case "Chapter 9":
            sql_select_query9 = "select * from questions where status = 'publish'  and category LIKE 'Chapter9%' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query9)
            attempted(question)
            return question

        case "Chapter 10":
            sql_select_query10 = "select * from questions where status = 'publish'  and category LIKE 'Chapter10%' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query10)
            attempted(question)
            return question

        case "Chapter 11":
            sql_select_query11 = "select * from questions where status = 'publish'  and category LIKE 'Chapter11%' ORDER by RAND() LIMIT 1"
            (question_id, question) = query_Sql(sql_select_query11)
            attempted(question)
            return question

        case "Chapter 12":
            sql_select_query12 = "select * from questions where status = 'publish'  and category LIKE 'Chapter12%' ORDER by RAND() LIMIT 1"
            question = query_Sql(sql_select_query12)
            attempted(question)
            return question
        case _:
            print("Selection invalid")


def addUser(username, password):
    username = username
    password = password
    createUser = "INSERT INTO User (userID, password) VALUES('" + username + "'," + password + ");"
    query_Sql(createUser)


def attempted(username, question_id):
    username = username
    question_ID = question_id
    attempted_question = "INSERT INTO Attempted_Question (userID, questionID) VALUES('" + username + "'," + question_ID + ");"
    query_Sql(attempted_question)
