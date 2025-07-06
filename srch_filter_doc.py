from vector_store import vector_store
from document import doc

#search with similarity
#k=value nedd to shown nomber of th player or option or list
a=vector_sreach=vector_store.similarity_search(
    query="who is the bowler amoung them",
    k=1
)

#print("simil search   :",a)

#serach with similarity score
b=vector_store.similarity_search_with_score(
    query = "Which players in the list represent Chennai Super Kings?",
    k=2

)

#print("score  :",b)

# meta-data filtering
d=vector_store.similarity_search_with_score(
    query="",
    filter={"team": "Chennai Super Kings"}
)

#print(d)