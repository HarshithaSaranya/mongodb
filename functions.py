print("hello")
import pymongo
import pprint
client = pymongo.MongoClient()
production2 = client.production2
person_collection = production2.person_collection

def create_document():
    names=["Ajeeth","Priyanka","pavitra","vignesh","sathya"]
    ages=[10,13,15,12,10]
    weights=[20,15,16,30,23]

    docs=[]
    for name,age,weight in zip(names,ages,weights):
        doc={"name":name,"age":age,"weight":weight}
        docs.append(doc)
    person_collection.insert_many(docs)
printer=pprint.PrettyPrinter()   

def find_all_people():
    people=person_collection.find() 
    for person in people:
        printer.pprint(person)

def find_par():
    par= person_collection.find_one({"name":"vaishna"})
    printer.pprint(par)

def count_all_people():
    count=person_collection.count_documents(filter={})
    print("no of people",count)

