class NamedEntity(object):
    def __init__(self, name, ontology, article_contents):
        self.name = name
        self.ontology = ontology
        self.article_contents = article_contents

class EntityType(object):
    def __init__(self, name, parents=None, children=None):
        self.name = name
        self.parents = parents
        self.children = children

    def set_parents(self, parents):
        self.parents = parents

    def set_children(self, children):
        self.children = children

# Examples: These will eventually come from the SQLite API that I'll write.
person = EntityType('Person')
politician = EntityType('Politician')
american_politician = EntityType('American Politician')
zombie_hunter_president = EntityType('Zombie Hunting American President')

parents = [person, politician, american_politician]
chidren = [politician, american_politician, zombie_hunter_president]
for p,c in zip(parents, chidren):
    p.set_children([c])
    c.set_parents([p])

lincoln_entity = NamedEntity('Abraham Lincoln',
                             [person, politician, american_politician, zombie_hunter_president],
                             'American Poltician and zombie hunter from the mid 19th-century.')