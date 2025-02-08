
# Custom Chatbot Project


This repository contains a custom chatbot project using vector-based search and FAISS indexing.

## Project Structure   
```plaintext
custom_chatbot/
├── vectorstore_index     # Directory containing chatbot index files
│   ├── index.faiss       # FAISS index for efficient vector-based search
│   └── index.pkl         # Pickled data for chatbot processing
├── README.md             # Project documentation
├── chatbot.py            # Main chatbot script
└── url.txt               # List of URLs or resources used by the chatbot 

```
 


## Features

- **Vector-based Search**: Fast and efficient retrieval using FAISS.
- **Modular Design**: Easy to extend with additional functionalities.
- **Lightweight**: Minimal dependencies for fast execution.






##  How to use 

1. Clone this repository 

```plaintext 
git clone https://github.com/sonali1326/custom_chatbot.git
cd custom_chatbot
``` 

2. Run the chatbot 

```plaintext  
python chatbot.py
```
## Folder and File Explanation 

- **vectorstore_index**: Contains FAISS and pickle index files for chatbot operations.
- **chatbot.py**: The main script for running the chatbot.
- **url.txt**: Stores relevant URLs or text resources used in the project.

## Future Improvements 

- Integrate advanced NLP models for better responses..
- Build a front-end interface for user interactions.
- Optimize FAISS index storage for faster retrieval.