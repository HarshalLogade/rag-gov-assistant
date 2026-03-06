from retriever import search

query = "crop insurance scheme"

results = search(query)

for r in results:
    print(r.page_content)
    print("----")