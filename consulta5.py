filename = r"C:\Users\Deme\Desktop\U\watos\xd.ttl" 
import rdflib
g = rdflib.Graph()
result = g.parse(filename, format='ttl')
print(result)
#Query que retorna cuantos videos por categoría que tengan más dislikes que likes.
query = """
PREFIX : <http://ex.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?cat (COUNT(DISTINCT ?videos) AS ?count) WHERE {
?canales <http://ex.org/a#Youtuber> ?canaln .
?videos <http://ex.org/a#channelTitle> ?canaln  . 
?videos <http://ex.org/a#likes> ?likes .
?videos <http://ex.org/a#dislikes> ?dislikes .
?canales <http://ex.org/a#category> ?cat .
FILTER (xsd:integer(?dislikes) >= xsd:integer(?likes))
}
GROUP BY ?cat
ORDER BY DESC(?count)
"""

for r in g.query(query):
    print( r["cat"] + " " +r["count"])