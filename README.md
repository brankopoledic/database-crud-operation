# Vector Database CRUD Operations

## Setup Instructions

1. Clone the repository:

   ```sh
   git clone <repository_url>
   cd vector_db_crud
   ```

2. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the tests to ensure everything is set up correctly:

   ```sh
   pytest
   ```

4. To start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```

## Usage

1. **Collection Creation**: Create a new collection/index to store vectorized text documents.
2. **Document Insertion**: Insert a new text document into the collection.
3. **Document Update**: Update an existing text document.
4. **Document Deletion**: Delete a text document from the collection.
5. **Document Retrieval**: Retrieve the top N documents relevant to a given input text.
