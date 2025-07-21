import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chain import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("🧠 Smart AI-Powered CV Matcher + Email Generator")
    url_input = st.text_input("Enter a job post URL:", value="https://careers.nike.com/software-engineer-ii-backend-itc/job/R-52621")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            raw_data = loader.load().pop().page_content
            cleaned_data = clean_text(raw_data)

            portfolio.load_portfolio()
            jobs = llm.extract_jobs(cleaned_data)

            for job in jobs:
                skills = ", ".join(job.get('skills', []))  # ✅ ensure it's a string
                links = portfolio.query_links(skills)

                if links:
                    email = llm.write_mail(job, links)
                    st.markdown(f"### ✉️ Cold Email for: `{job['role']}`")
                    st.code(email, language='markdown')
                    st.markdown(f"🔗 **CV Link:** [{links[0]['role']}]({links[0]['cv_link']})\n\n**Skills Matched:** {links[0]['skills']}")
                else:
                    st.warning("⚠️ No matching CV found for this job.")
        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
