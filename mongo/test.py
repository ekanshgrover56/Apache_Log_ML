from MongoGrabber import Mongo_Grabber

pipeline = [
    {
        "$group": {
            "_id": {
                "uri": "$uri",
                "server_ip": "$server_ip",
                "category":"$category"
            }
        }
    },
    {
        "$match": {
            "_id.category": {
               "$in" : ["good", "attack"]

            }
        }
    }
]

master = {}
dbconnector = Mongo_Grabber(Mongo ACCOUNT)
#dbconnector.mongo_authenticated('http_bank')
#print(dbconnector.mongo_authenticate())

#print(dbconnector.mongo_connection)
i = 1
print(dbconnector.get_data(pipeline,'http_bank'))

print(i)
