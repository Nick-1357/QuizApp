import pandas as pd
from sqlalchemy import create_engine
import csv
from SlideWindow import *
#import py_mysql_connector #import these and download them on command line

def chapter1content():
    engine = create_engine("mysql+mysqlconnector://root:Sdz321654@localhost:3306/its") #create_engine("mysql+mysqlconnector://username:password:host:port_number:database_name")
    query = pd.read_sql_query('SELECT * FROM eSPFirst WHERE chapter = 1', engine) #put desired query to convert
    df = pd.DataFrame(query) #convert query into python data structure
    print(df)

    text_list = df["content"].tolist() # convert into a series (the column containing content)
    print(text_list)
    text = ""
    for te in text_list:
        text = text+" "+te
    print(text)
    return text

def kwsFromExtractions():
    kw = []
    with open('../keyword_search/extractions.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if([row[1],row[4]] not in kw):
                kw.append([row[1],float(row[4])])          #simple duplicate filter
            line_count += 1
        #print(f'Processed {line_count} lines.')
    line_count = 0
    for row in kw:
        #print(row)
        line_count += 1
    print(f'Processed {line_count} lines.')
    return kw

def kwsfilter(question):
    kw = kwsFromExtractions()
    kw_in = []
    for w in kw:
        if(w[0] in question):
            kw_in.append(w)
    return kw_in

def kwsampleQkw():
    kw = []
    with open('../keyword_search/question_extractions.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if([row[1],row[4]] not in kw):
                kw.append([row[1],float(row[4])])          #simple duplicate filter
            line_count += 1
        #print(f'Processed {line_count} lines.')
    line_count = 0
    for row in kw:
        #print(row)
        line_count += 1
    print(f'Processed {line_count} lines.')
    return kw

#print(kwsampleQkw())
#print(kwsfilter("step signal concentration system"))

text = chapter1content()

res=calculatePharagraph(kwsampleQkw(),text)

max = 0
index = 0
for i in range(len(res)):
    if res[i]>res[index]:
        index = i
#print(res)
print(index)
sentences = text.split(".")
i = 0
print("***********************Sample_Result****************************")
for s in sentences:
    if(i<index+3 and i>index-3):
        print(s)
    #else:
    #    print(s)
    #print(" ")
    i=i+1





    
