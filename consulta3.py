filename = r"C:\Users\Deme\Desktop\U\watos\xd.ttl" 
import rdflib
g = rdflib.Graph()
result = g.parse(filename, format='ttl')
print(result)
#Query que retorna el video con mayor cantidad de visitas para cada canal que esté en los top 1000.
query = """
PREFIX : <http://ex.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?canaln ?videon (MAX(xsd:integer(?visitas)) AS ?visitat) WHERE {
?canales <http://ex.org/a#Youtuber> ?canaln .
?videos <http://ex.org/a#channelTitle> ?canaln .
?videos <http://ex.org/a#view_count> ?visitas .
?videos <http://ex.org/a#title> ?videon .
}
GROUP BY ?canaln
ORDER BY DESC(?visitat)
"""
#g.query(query)
for r in g.query(query):
    print( r["canaln"] + " " + r["videon"] + " " + r["visitat"])