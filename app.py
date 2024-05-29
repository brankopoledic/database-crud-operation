import faiss
import numpy as np
from fastapi import FastAPI, HTTPException
from typing import List

class VectorDatabase:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []
    
    def create_collection(self):
        self.index = faiss.IndexFlatL2(self.dim)
        self.documents = []

    def insert_document(self, doc_id: int, vector: np.ndarray):
        if doc_id < len(self.documents):
            raise ValueError("Document ID already exists.")
        self.index.add(vector)
        self.documents.append(vector)

    def update_document(self, doc_id: int, new_vector: np.ndarray):
        if doc_id >= len(self.documents):
            raise ValueError("Document ID does not exist.")
        self.documents[doc_id] = new_vector
        self.index.reconstruct(doc_id, new_vector)

    def delete_document(self, doc_id: int):
        if doc_id >= len(self.documents):
            raise ValueError("Document ID does not exist.")
        self.documents.pop(doc_id)
        self.index.remove_ids(np.array([doc_id]))

    def retrieve_documents(self, vector: np.ndarray, n: int):
        D, I = self.index.search(vector, n)
        return I

app = FastAPI()

db = VectorDatabase(dim=300)

@app.post("/create-collection/")
def create_collection():
    db.create_collection()
    return {"message": "Collection created"}

@app.post("/insert-document/")
def insert_document(doc_id: int, vector: List[float]):
    try:
        db.insert_document(doc_id, np.array(vector, dtype=np.float32))
        return {"message": "Document inserted"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/update-document/")
def update_document(doc_id: int, new_vector: List[float]):
    try:
        db.update_document(doc_id, np.array(new_vector, dtype=np.float32))
        return {"message": "Document updated"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/delete-document/{doc_id}")
def delete_document(doc_id: int):
    try:
        db.delete_document(doc_id)
        return {"message": "Document deleted"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/retrieve-documents/")
def retrieve_documents(vector: List[float], n: int):
    indices = db.retrieve_documents(np.array(vector, dtype=np.float32).reshape(1, -1), n)
    return {"indices": indices.tolist()}