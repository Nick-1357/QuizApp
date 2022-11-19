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
        return(user[4])


cursor = myDb.cursor()


def querySql(prompt):
    match prompt:
        case "Chapter 1":
            sql_select_query1 = "select * from questions where status = 'publish'  and category = 'Chapter1' LIMIT 1"
            return query_Sql(sql_select_query1)

        case "Chapter 2":
            sql_select_query2 = "select * from questions where status = 'publish'  and category = 'Chapter2' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query2)
        case "Chapter 3":
            sql_select_query3 = "select * from questions where status = 'publish'  and category = 'Chapter3' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query3)
        case "Chapter 4":
            sql_select_query4 = "select * from questions where status = 'publish'  and category = 'Chapter4' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query4)
        case "Chapter 5":
            sql_select_query5 = "select * from questions where status = 'publish'  and category = 'Chapter5' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query5)
        case "Chapter 6":
            sql_select_query6 = "select * from questions where status = 'publish'  and category = 'Chapter6' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query6)
        case "Chapter 7":
            sql_select_query7 = "select * from questions where status = 'publish'  and category = 'Chapter7' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query7)
        case "Chapter 8":
            sql_select_query8 = "select * from questions where status = 'publish'  and category LIKE 'Chapter8%' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query8)
        case "Chapter 9":
            sql_select_query9 = "select * from questions where status = 'publish'  and category LIKE 'Chapter9%' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query9)
        case "Chapter 10":
            sql_select_query10 = "select * from questions where status = 'publish'  and category LIKE 'Chapter10%' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query10)
        case "Chapter 11":
            sql_select_query11 = "select * from questions where status = 'publish'  and category LIKE 'Chapter11%' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query11)
        case "Chapter 12":
            sql_select_query12 = "select * from questions where status = 'publish'  and category LIKE 'Chapter12%' ORDER by RAND() LIMIT 1"
            return query_Sql(sql_select_query12)
        case _:
            print("Selection invalid")