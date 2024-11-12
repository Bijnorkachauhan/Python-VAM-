from pymongo import MongoClient

#to create the mongo do client
client = MongoClient("mongodb://localhost:27017/")

#to create new database in client
myDb = client["tododb"]

#to create new collection in database
myCol = myDb["dailyTask"]

# #to insert the task in tododatabase
# myTask = {"taskName":input("Enter Task Name: "), "taskDesc":input("Enter Task Description: "), "taskDate":input("Enter Task Date: "), "taskStatus":0}

# #to execute the insert in collection
# myCol.insert_one(myTask)


#to pass the delete task from collection
# myDeleteTask = {"taskDate":"11 nov 2024"}
# #to pass the delete task to collecttion
# myCol.delete_one(myDeleteTask)

#create new collection for event
eventList = myDb["eventList"]

#Add new event in eventList
# event = [{"eventName":"Talent Hunt","eventDate":"13 Nov 2024","venue":"ITS"},{"eventName":"VAM","eventDate":"14 Nov 2024","venue":"ITS"}]
# #add event into eventlist
# eventList.insert_many(event)

#to get the list of event
allEvent = eventList.find()
for event in allEvent:
    print(event)
    
#update the event in eventList
updatevent = {"eventDate":"14 Nov 2024"}
eventList.update_one({"eventName":"Talent Hunt"},{"$set":updatevent})
updatevent = {"eventDate":"16 NOV 2024"}
eventList.update_many({"venue":"ITS"},{"$set":updatevent})
              