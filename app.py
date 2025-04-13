import streamlit as st
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


st.set_page_config(page_title="Polite Email Rewriter", page_icon="🤐")

st.title("🧼 Passive-Aggressive Email Rewriter")
st.caption("Turn rude messages into polite emails powered by AI")

rude_input = st.text_area("✍️ Enter the rude message here:")

if st.button("Rewrite It ✨"):
    if rude_input.strip() == "":
        st.warning("Please enter a message to rewrite.")
    else:
        with st.spinner("Rewriting politely..."):
            prompt = f"""Rewrite the following rude or blunt sentence into a professional, polite, and workplace-appropriate message:

Rude: "{rude_input}"
Polite:"""

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=100
            )

            polite_output = response["choices"][0]["message"]["content"].strip()
            st.success("Here's your polite message:")
            st.write(polite_output)
