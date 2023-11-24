import rdflib
from prettytable import PrettyTable

filename = r"/Users/fernanda/watos/project/xd.ttl"
g = rdflib.Graph()
result = g.parse(filename, format='ttl')

# Query that retrieves all channels without a video in the trending list
# Channels without trending videos (30 for ppt purposes)
query = """
PREFIX : <http://ex.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?canaln (COUNT(?videos) AS ?count) WHERE {
  ?canales <http://ex.org/a#Youtuber> ?canaln .
  OPTIONAL {
    ?canales <http://ex.org/a#Youtuber> ?canalndos .
    ?videos <http://ex.org/a#channelTitle> ?canalndos .
  }
  FILTER (!BOUND(?canalndos))
}
GROUP BY ?canaln
LIMIT 30
"""

# Create a PrettyTable instance
table = PrettyTable(['Canal', 'Count'])

# Iterate over the query results and add rows to the table
for r in g.query(query):
    table.add_row([str(r["canaln"]), str(r["count"])])
    
# Print the table
print(table)
