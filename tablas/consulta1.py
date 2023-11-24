import rdflib
from prettytable import PrettyTable

filename = r"/Users/fernanda/watos/project/xd.ttl"
g = rdflib.Graph()
result = g.parse(filename, format='ttl')

# Query que retorna cuántos videos trending tiene cada canal y su ranking.
# Trending videos count per channel and the channel ranking per suscribers.
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
LIMIT 30
"""

# Create a PrettyTable instance
table = PrettyTable(['Canal', 'Rank', 'Count'])

# Iterate over the query results and add rows to the table
for r in g.query(query):
    table.add_row([str(r["canal"]), str(r["rank"]), str(r["count"])])
    
# Print the table
print(table)
