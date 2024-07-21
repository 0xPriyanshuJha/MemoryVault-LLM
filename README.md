## LLM App with Memory (MemoryVault-LLM)
This Streamlit application functions as an AI-powered chatbot, utilizing OpenAI's GPT-4o model with a memory retention feature. It allows users to converse with the AI, maintaining context over multiple interactions for a seamless conversational experience.
### Features

- Utilizes OpenAI's GPT-4o model for generating responses.
- Implements persistent memory using Mem0 and the Qdrant vector store.
- Allows users to view their conversation history.
- Provides a user-friendly interface through Streamlit.

### How to get Started?

1. Clone the GitHub repository
```bash
git clone https://github.com/0xPriyanshuJha/MemoryVault-LLM.git
```

2. Install the required dependencies:

```bash
pip install streamlit, mem0, openai
```

3. Ensure Qdrant is running:
The app expects Qdrant to be running on localhost:6333. Adjust the configuration in the code as per your requirement.

```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

4. Run the Streamlit App
```bash
streamlit run llm.py
```
