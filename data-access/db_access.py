import sqlite3

data_base = "/home/louis/Data/fgner/test.db"

class DataFactory(object):
    def __init__(self):
        self.conn =sqlite3.connect(data_base)

    def get_entity_article(self, entity_name):
        pass

    def get_entity_type_ontology(self, entity_type_name):
        pass

    def _run_sql(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        column_names = next(cur)
        return (data for data in cur)

    def _select(self, select_fields, table_name, equality_constraints):
        template = "SELECT {0} from {1} {2}"
        select = ','.join(select_fields)
        if equality_constraints:
            and_clause = 'WHERE ' + ' AND '.join(["{0}='{1}'".format(column, value)
                                                 for column, value in equality_constraints])
        else:
            and_clause = ''
        query = template.format(select, table_name, and_clause)
        return self._run_sql(query)