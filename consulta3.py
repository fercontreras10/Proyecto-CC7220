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

SELECT ?canaln (MAX(xsd:integer(?visitas)) AS ?visitasdos) WHERE {
?canales <http://ex.org/a#Youtuber> ?canaln .
?videos <http://ex.org/a#channelTitle> ?canaln .
?videos <http://ex.org/a#view_count> ?visitas .
}
GROUP BY ?canaln 
"""
for r in g.query(query):
    print( r["canaln"] +  " " + r["visitasdos"])
