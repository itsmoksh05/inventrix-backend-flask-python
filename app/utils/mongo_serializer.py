def serialize_docs(cursor):
    return [
        {**doc, "_id": str(doc["_id"])}
        for doc in cursor
    ]

def serialize_doc(cursor):
    if cursor and "_id" in cursor:
        cursor["_id"] = str(cursor["_id"])

    return cursor