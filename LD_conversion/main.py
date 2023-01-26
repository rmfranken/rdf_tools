from rdflib import Graph

g = Graph()
#add desired prefixes here
context = {"@context": {
    "@sdsc": "https://sdsc.ch/",
    "@owl": "http://www.w3.org/2002/07/owl#",
    "@rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "@rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@schema": "http://schema.org/",
    "@sd": "https://w3id.org/okn/o/sd#",
    "@sh": "http://www.w3.org/ns/shacl#",
    "@skos": "http://www.w3.org/2004/02/skos/core#",
    "@xsd": "http://www.w3.org/2001/XMLSchema#"

}}
#input file name and file format here
g.parse('input\geospecies.rdf', format="application/rdf+xml")


#output file name and file format here
g.serialize(destination='output\pretty.ttl', format='ttl')