filename = r"C:\Users\Deme\Desktop\U\watos\xd.ttl" 
import rdflib
g = rdflib.Graph()
result = g.parse(filename, format='ttl')
print(result)
#Query que retorna todos los canales que no tienen un video en los videos trending.
query = """
PREFIX : <http://ex.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?canaln WHERE {
?canales <http://ex.org/a#Youtuber> ?canaln  . 
OPTIONAL {
?canales <http://ex.org/a#Youtuber> ?canalndos  . 
?videos <http://ex.org/a#channelTitle> ?canalndos  . 
}
FILTER (!BOUND(?canalndos))
}
"""
#g.query(query)
for r in g.query(query):
    print( r["canaln"])