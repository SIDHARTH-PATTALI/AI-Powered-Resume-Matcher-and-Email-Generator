import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="C:/Users/asus/ai_my_Project_2/cv_links.csv"):   ##cvlinkcontaincsv
        self.file_path = file_path
        self.data = pd.read_csv(file_path, encoding='ISO-8859-1')
        self.chroma_client = chromadb.PersistentClient(path="vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if self.collection.count() == 0:
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Skills Included"]],
                    metadatas=[{
                        "cv_link": row["CV_Link"],
                        "role": row["Role"],
                        "skills": row["Skills Included"]
                    }],
                    ids=[str(uuid.uuid4())]
                )
            print("✅ Portfolio loaded into ChromaDB")
        else:
            print("⚠️ Portfolio already loaded")

    def query_links(self, skills):
        if isinstance(skills, list):
            skills = ", ".join(skills)
        results = self.collection.query(query_texts=[skills], n_results=1)
        metadatas = results.get('metadatas', [])
        # Ensure it's not a list of lists
        if metadatas and isinstance(metadatas[0], list):
            return metadatas[0]
        return metadatas

