import rdflib
from prettytable import PrettyTable

filename = r"/Users/fernanda/watos/project/xd.ttl"
g = rdflib.Graph()
result = g.parse(filename, format='ttl')

# Query que retorna el video con mayor cantidad de visitas para cada canal que esté en los top 1000.
# Video with the most views per channel in the top 30 (for showing purposes in ppt).
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
ORDER BY DESC(?visitasdos)
LIMIT 30
"""

# Create a PrettyTable instance
table = PrettyTable(['Canal', 'Views'])

# Iterate over the query results and add rows to the table
for r in g.query(query):
    table.add_row([str(r["canaln"]), str(r["visitasdos"])])
    
# Print the table
print(table)
