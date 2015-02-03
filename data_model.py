class NamedEntity(object):
    def __init__(self, name, ontology, article_contents):
        self.name = name
        self.ontology = ontology
        self.article_contents = article_contents

example_entity = NamedEntity('Abraham Lincoln',
                             ['Person','Politician','American Politician','Zombie Hunting American President'],
                             'American Poltician and zombie hunter from the mid 19th-century.')