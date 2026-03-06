import json
from langchain_core.documents import Document

def load_schemes():

    with open("schemes.json", "r", encoding="utf-8") as f:
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