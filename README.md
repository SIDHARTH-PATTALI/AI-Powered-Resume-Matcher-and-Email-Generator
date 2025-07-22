# AI-Powered-Resume-Matcher-and-Email-Generator


This project is an AI-powered assistant that automates job applications. It takes a **job URL**, scrapes the job description, matches it with your best-fitting CV, and generates a **tailored cold email** to apply — all in seconds.

## 🚀 Features

- 🔎 Scrapes job description from any job posting URL.
- 🧠 Uses semantic similarity to match the job with your most relevant CV.
- 📧 Auto-generates a professional cold email using your real CV skills .
- 🧾 Outputs selected CV link and email in Streamlit.

--

## 💻 Technologies Used

| Tool                   | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| **LangChain**          | Framework to build the LLM pipeline and manage prompt chaining          |
| **ChromaDB**           | Vector store to store and retrieve CVs based on semantic similarity     |
| **ChatGroq (LLaMA 3)** | Hosted LLM used to generate high-quality application emails             |
| **Streamlit**          | Frontend interface to upload CVs, paste job URLs, and view results      |
| **WebBaseLoader**      | Loads and parses job descriptions from web URLs                         |
| **Pandas**             | Reads and processes the CSV of your CVs                                 |
---

## 📄 Input Format: CV Skills Table

This project uses a CSV file (e.g., `cv_data.csv`) that contains your available CVs and their associated skills.

### ✅ Sample `cv_data.csv` Format

```csv
cv_link,role,Skills Included
https://.../Datascience_sidharth_cv1.pdf,Data Science,"Python, SQL, Numpy, Pandas"
https://.../DataEngineering_sidharth_cv1.pdf,Data Engineering,"Python, SQL, Airflow, Spark"
https://.../AI_ML_sidharth_cv1.pdf,AI_ML,"LangChain, LLMs, Python, Transformers, Tensorflow"
https://.../Data_Analytics_sidharth_cv1.pdf,Data Analytics,"Python, SQL, Power BI, Excel"
https://.../Fullstack_sidharth_cv1.pdf,Full Stack,"HTML, CSS, Java, Python, AWS, MySQL, MongoDB"
