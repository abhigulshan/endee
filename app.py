import streamlit as st
from difflib import get_close_matches

st.set_page_config(page_title="AI Assistant", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Programming Assistant")

# ✅ Knowledge base
qa_data = {
    "what is java": "Java is a high-level, object-oriented programming language used to build applications.",
    "what is node js": "Node.js is a runtime environment that allows JavaScript to run on the server side.",
    "what is api": "API stands for Application Programming Interface, used for communication between systems.",
    "what is abstraction": "Abstraction means hiding implementation details and showing only essential features.",
    "what is encapsulation": "Encapsulation means wrapping data and methods into a single unit.",
    "what is inheritance": "Inheritance allows one class to acquire properties of another class.",
    "what is polymorphism": "Polymorphism allows methods to behave differently based on input."
}

query = st.text_input("💬 Ask your question")

if st.button("Get Answer") and query:

    query_lower = query.lower()

    # 🔥 Direct keyword match
    found = False
    for q in qa_data:
        if q in query_lower:
            st.success("💡 Answer")
            st.write(qa_data[q])
            found = True
            break

    # 🔥 Fuzzy match (smart matching)
    if not found:
        matches = get_close_matches(query_lower, qa_data.keys(), n=1, cutoff=0.5)

        if matches:
            st.success("💡 Answer")
            st.write(qa_data[matches[0]])
        else:
            st.error("❌ Sorry, I don’t know this yet. Try programming-related questions.")