import json
import os
from pathlib import Path
from langchain_core.documents import Document

def load_schemes():
    # Get the absolute path to the data folder
    current_dir = Path(__file__).resolve().parent.parent
    schemes_path = current_dir / "data" / "schemes.json"
    
    print(f"📂 Loading schemes from: {schemes_path}")
    
    with open(schemes_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    schemes = data["schemes"]

    docs = []

    for key, scheme in schemes.items():
        text = f"""
        Scheme Name: {scheme['name']}
        Description: {scheme['description']}
        Eligibility: {scheme['eligibility']}
        Benefit: {scheme['benefit']}
        Category: {scheme['category']}
        Crops: {scheme['params']['crops']}
        State: {scheme['params']['state']}
        Required Documents: {', '.join(scheme['docs'])}
        Apply Link: {scheme['url']}
        """

        docs.append(
            Document(
                page_content=text,
                metadata={
                    "id": scheme["id"],
                    "name": scheme["name"],
                    "category": scheme["category"]
                }
            )
        )

    return docs