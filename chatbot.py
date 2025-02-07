

pip install langchain

pip install -U langchain-community

!pip install unstructured
!pip install unstructured[local-inference]
!pip install unstructured[docs]

from langchain.document_loaders import UnstructuredURLLoader

urls = ["https://brainlox.com/courses/category/technical"]


loader = UnstructuredURLLoader(urls=urls)
documents = loader.load()

for doc in documents:
    print(doc.page_content)

!pip install faiss-cpu

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


texts = [doc.page_content for doc in documents if doc.page_content]  


faiss_index = FAISS.from_texts(texts, embedding_model)


faiss_index.save_local("vectorstore_index")
print("Embeddings created and stored in FAISS!")

pip install flask flask-restful



from flask import Flask, request, jsonify
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import numpy as np

app = Flask(__name__)


faiss_index = FAISS.load_local("vectorstore_index", embedding_model, allow_dangerous_deserialization=True)

@app.route("/query", methods=["POST"])
def query_index():
    data = request.json
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query cannot be empty."}), 400


    query_embedding = embedding_model.embed_documents([user_query])
    query_embedding = np.array(query_embedding).astype('float32')


    distances, indices = faiss_index.search(query_embedding, k=1)

    if indices[0][0] != -1:
        closest_match = faiss_index.texts[indices[0][0]]
        return jsonify({"closest_match": closest_match})
    else:
        return jsonify({"message": "No match  has been found."})

if __name__ == "__main__":
    app.run(debug=True)

