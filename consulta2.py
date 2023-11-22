filename = r"C:\Users\Deme\Desktop\U\watos\xd.ttl" 
import rdflib
g = rdflib.Graph()
result = g.parse(filename, format='ttl')
print(result)
#Query que retorna la cantidad de videos trending por categoría y años de creacion para los canales creados en los mismos años que la NBA o T-series.
query = """
PREFIX : <http://ex.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?cat ?an (COUNT(DISTINCT ?videos) AS ?count) WHERE {
?nba <http://ex.org/a#Youtuber> "NBA" .
?ts <http://ex.org/a#Youtuber> "T-Series" .
{ ?ts <http://ex.org/a#started> ?an .}
UNION
{ ?nba <http://ex.org/a#started> ?an .}
?canales <http://ex.org/a#started> ?an .
?canales <http://ex.org/a#Youtuber> ?canaln .
?videos <http://ex.org/a#channelTitle> ?canaln .
?canales <http://ex.org/a#category> ?cat .
?canales <http://ex.org/a#started> ?an .
}
GROUP BY ?cat ?an
ORDER BY DESC(?count)
"""
#g.query(query)
for r in g.query(query):
    print( r["cat"] + " " + r["an"] + " " + r["count"])