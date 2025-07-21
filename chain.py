import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### INSTRUCTION:
            The scraped text is from a careers page.
            Extract job postings and return JSON with these keys: `role`, `experience`, `skills`, `description`.

            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke({"page_data": cleaned_text})

        try:
            parser = JsonOutputParser()
            result = parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("🧠 Failed to parse job details.")

        return result if isinstance(result, list) else [result]

    def write_mail(self, job, links):
        if not links:
            return "❌ No matching CV found."

        first_match = links[0]
        if not isinstance(first_match, dict):
            return f"❌ Invalid metadata format: {first_match}"

        prompt_email = PromptTemplate.from_template(
            """
            ### JOB ROLE CONTEXT:
            {job_role}

            ### YOUR AVAILABLE SKILLS (from CV):
            {cv_skills}

            ### INSTRUCTION:
            You are Sidharth Pattali, applying for the above role.
            Write a cold email to HR. Be formal, concise, and highlight ONLY these skills .
            
            ### Job description that give on the website:(only for takeing company name)
            {job_description}
            

            Mention your CV is attached.

            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        response = chain_email.invoke({
            "job_role": job.get('role', 'Unknown Role'),
            "job_description": job.get('description', 'No Description'),
            "cv_skills": first_match.get("skills", "Python")  # fallback
        })
        return response.content