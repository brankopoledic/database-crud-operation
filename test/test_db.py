import pytest
import numpy as np
from main import VectorDatabase

def test_create_collection():
    db = VectorDatabase(dim=3)
    db.create_collection()
    assert len(db.documents) == 0

def test_insert_document():
    db = VectorDatabase(dim=3)
    db.create_collection()
    vector = np.array([[0.1, 0.2, 0.3]], dtype=np.float32)
    db.insert_document(0, vector)
    assert len(db.documents) == 1

def test_update_document():
    db = VectorDatabase(dim=3)
    db.create_collection()
    vector = np.array([[0.1, 0.2, 0.3]], dtype=np.float32)
    db.insert_document(0, vector)
    new_vector = np.array([[0.4, 0.5, 0.6]], dtype=np.float32)
    db.update_document(0, new_vector)
    assert np.array_equal(db.documents[0], new_vector)

def test_delete_document():
    db = VectorDatabase(dim=3)
    db.create_collection()
    vector = np.array([[0.1, 0.2, 0.3]], dtype=np.float32)
    db.insert_document(0, vector)
    db.delete_document(0)
    assert len(db.documents) == 0

def test_retrieve_documents():
    db = VectorDatabase(dim=3)
    db.create_collection()
    vector1 = np.array([[0.1, 0.2, 0.3]], dtype=np.float32)
    vector2 = np.array([[0.4, 0.5, 0.6]], dtype=np.float32)
    db.insert_document(0, vector1)
    db.insert_document(1, vector2)
    retrieved = db.retrieve_documents(vector1, 1)
    assert retrieved[0][0] == 0