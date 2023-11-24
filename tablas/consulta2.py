import rdflib
from prettytable import PrettyTable

filename = r"/Users/fernanda/watos/project/xd.ttl"
g = rdflib.Graph()
result = g.parse(filename, format='ttl')

# Query que retorna la cantidad de videos trending por categoría y años de creacion para los canales creados en los mismos años que la NBA o T-series.
# Trending videos count per category and year of creation for channels created in the same year as the NBA or T-series.
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

# Create a PrettyTable instance
table = PrettyTable(['Categorie', 'Year', 'Count'])

# Iterate over the query results and add rows to the table
for r in g.query(query):
    table.add_row([str(r["cat"]), str(r["an"]), str(r["count"])])
    
# Print the table
print(table)
