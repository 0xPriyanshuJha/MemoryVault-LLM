import streamlit as st
from mem0 import Memory
from openai import OpenAI

st.title("Mem0AI")
st.caption("LLM App with personalized memory layer")
open_api_key = st.text_input("OpenAI API Key", type="password")
if open_api_key:
    client =OpenAI(api_key = open_api_key)
    config = {
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "host": "localhost",
                "port": 6333,
            }
        },
    }
    memory = Memory.from_config(config)

user_id = st.text_input("Enter your Username")
prompt = st.text_input("Ask GPT")

if st.button('Chat with LLM'):
    with st.spinner('Searching...'):
        relevant_memories = memory.search(query=prompt, user_id = user_id)
        context = "Relevant past information: \n" + "\n".join([f"-{mem['text']}" for mem in relevant_memories])
        full_prompt = f"{context}\nHuman: {prompt}\nAI:"

        response = client.chat.completions.create(
            model="gpt-4",
            message=[
                {"role": "system", "content": "You are a helplful assistant with access to past conversations."},
                {"role": "user", "content": full_prompt}
            ]
        )

        answer = response.choices[0].message.content
        st.write("Answer: ", answer)
        memory.add(answer, user_id = user_id)
        
st.sidebar.title("Memory Info")
if st.sidebar.button("View Memory Info"):
    memories = memory.get_all(user_id = user_id)
    if memories:
        st.sidebar.write(f"You are viewing memory for user **{user_id}**")
        for mem in memories:
            st.sidebar.write(f"-{mem['text']}")
        else:
            st.sidebar.info("No learning history found for this user ID.")