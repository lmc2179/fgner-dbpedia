from SPARQLWrapper import SPARQLWrapper, JSON

class DBPedia(object):
    def __init__(self):
        self.sparql_wrapper = SPARQLWrapper("http://dbpedia.org/sparql")

    def run_query(self, query):
        self.sparql_wrapper.setQuery(query)
        self.sparql_wrapper.setReturnFormat(JSON)
        results = self.sparql_wrapper.query().convert()
        return results