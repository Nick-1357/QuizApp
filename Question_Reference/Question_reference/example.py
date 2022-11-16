#need to change the USER_NAME and PASSWORD for sql connection first



import pandas as pd                         #import these and download them on command line
from sqlalchemy import create_engine        #import these and download them on command line
import csv
from SlideWindow import *
from mySimpleFilter import simpleTextCleaner

#this function will recure the raw text(with html tags) of chapter one as a single string
def chapter1content():
    engine = create_engine("mysql+mysqlconnector://root:Sdz321654@localhost:3306/its") #create_engine("mysql+mysqlconnector://username:password:host:port_number:database_name")
    query = pd.read_sql_query('SELECT * FROM eSPFirst where chapter=1 and meta=\'paragraph\'', engine) #put desired query to convert
    df = pd.DataFrame(query) #convert query into python data structure
    #print(df)

    text_list = df["content"].tolist() # convert into a series (the column containing content)
    print(text_list)
    text = ""
    for te in text_list:
        text = text+" "+te
    #print(text)
    return simpleTextCleaner(text)

#this function will read the extractions.csv from '../keyword_search/extractions.csv', and return a list of [<keyword>,<weight>].
#Now, this function uses a simplest why to delete duplicate.
def kwsFromExtractions():
    kw = []
    w = []
    with open('../keyword_search/extractions.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if(row[1] not in w):
                kw.append([row[1],float(row[4])])           #a very simple duplicate filter
                w.append(row[1])
            line_count += 1
    line_count = 0
    for row in kw:
        line_count += 1
    #print(f'Processed {line_count} lines.')
    return kw

#this function means to find all matching keywords from keyword list, kwsFromExtractions(), within a question, and return the keyword-weight pair.
def kwsfilter(question):
    kw = kwsFromExtractions()
    kw_in = []
    for w in kw:
        if(w[0] in question):
            kw_in.append(w)
    return kw_in

#this function will read the extractions.csv from '../keyword_search/extractions.csv', and return a list of [<keyword>,<weight>].
#Now, this function uses a simplest why to delete duplicate.
def kwsampleQkw():
    kw = []
    w = []
    with open('../keyword_search/question_extractions.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if(row[1] not in w):
                kw.append([row[1],float(row[4])])          #a very simple duplicate filter
                w.append(row[1])
            line_count += 1
    line_count = 0
    for row in kw:
        line_count += 1
    #print(f'Processed {line_count} lines.')
    return kw


def runExample():
    text = chapter1content()
    q = 'The meaning of "negative frequency" in a Fourier series is'
    additionalkw = [["CD",2.0],["signal",0.5]]


    print("\n")
    print("************************************************************************")
    print("*************************Chapter 1 Content******************************")
    print("************************************************************************")
    print(text)

    print("\n")
    print("************************************************************************")
    print("************** Keywords also in extraction.csv *************************")
    print("************************************************************************")

    kws = kwsfilter(q);
    for w in additionalkw:
        kws.append(w);
    print(kws)
    res=calculatePharagraph(kws,text)

    max = 0
    index = 0
    for i in range(len(res)):
        if res[i]>res[index]:
            index = i

    print("\n")
    print("************************************************************************")
    print("************************Sentence_Weight_Res*****************************")
    print("************************************************************************")
    print(res)
    print("The index of the max weight: {}".format(index))

    sentences = text.split(".")
    i = 0

    print("\n")
    print("************************************************************************")
    print("**********Sample_Result,including 3 sentence before and after***********")
    print("************************************************************************")
    for s in sentences:
        if(i<index+3 and i>index-3):
            print("\nIndex:{}".format(i))
            print(s)
        i=i+1

runExample()
    
