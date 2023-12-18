import pandas as pd
import pymongo
import json

uri = "mongodb+srv://susheela:<pavan629>@cluster0.twh81ir.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = (r"C:\\Machine_Learning_Application\\Machine-Learning-Application\\Data\\train.csv")

DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ == "__main__":
    #Read the data from the CSV file into a pandas dataframe
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns of our Data: {df.shape}")

    #Convert the DataFrame to a list of dictionaries (Json records)
    joson_records = json.loads(df.to_json(orient="records"))
    print(joson_records[0])

    #Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)

    #Access the desired database  and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

    #Insert the json record into collection
    collection.insert_many(joson_records)

    #Close the MongoDB connection
    client.close()
