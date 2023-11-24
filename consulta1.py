filename = r"C:\Users\Deme\Desktop\U\watos\xd.ttl" 
import rdflib
g = rdflib.Graph()
result = g.parse(filename, format='ttl')
print(result)
#Query que retorna cuantos videos trending tiene cada canal y su rank.
query = """
PREFIX : <http://ex.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?canal ?rank (COUNT(DISTINCT ?video) AS ?count) WHERE {
?video <http://ex.org/a#channelTitle> ?canal .
?id <http://ex.org/a#Youtuber> ?canal .
?id <http://ex.org/a#rank> ?rank .
}
GROUP BY ?canal 
ORDER BY DESC(?count)
"""
for r in g.query(query):
    print(r["canal"] + " " + r["rank"] + " " + r["count"])
