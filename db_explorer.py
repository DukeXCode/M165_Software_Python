import pymongo
import os


def run():
    connection_string = os.environ.get('MONGO_CONNECTION')
    client = pymongo.MongoClient(connection_string)

    print('\nDB Explorer\n')

    print('DBs:')
    for db in client.list_database_names():
        print(db)

    while True:
        db_input = input('select db: ')
        if db_input in client.list_database_names():
            db = client[db_input]
            break
        print('invalid db')

    print('\nCollections:')
    for collection in db.list_collection_names():
        print(f'- {collection}')

    while True:
        collection_input = input('select collection: ')
        if collection_input in db.list_collection_names():
            collection = db[collection_input]
            break
        print('invalid collection')

    print('\nDocuments:')

    for document in collection.find():
        print(document.get('_id'))

    while True:
        document_input = input('select document: ')
        entry_found = False
        for document in collection.find():
            if str(document.get('_id')) == document_input:
                entry_found = True
                for entry in document:
                    print(f'{entry}: {document.get(entry)}')
        if entry_found:
            break
        else:
            print('invalid document')


while True:
    run()
