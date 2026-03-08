import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load env
load_dotenv()

# Debug (optional)
# st.write("ENV:", os.environ)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found. Check your .env file.")
    st.stop()

# Initialize client
client = Groq(api_key=api_key)

# UI
st.set_page_config(page_title="AI Research Assistant", layout="wide")
st.title("🧠 AI Research Assistant")
st.subheader("Generate detailed research reports using AI")

topic = st.text_input("Enter topic:")

if st.button("Generate") and topic:
    with st.spinner("Generating..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant."},
                    {"role": "user", "content": f"Write a detailed report on {topic}"}
                ],
                max_tokens=1500
            )

            output = response.choices[0].message.content

            st.success("Done!")
            st.write(output)

            st.download_button(
                "Download",
                output,
                file_name=topic.replace(" ", "_") + ".txt"
            )

        except Exception as e:
            st.error(f"Error: {e}")
