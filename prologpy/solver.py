from prologpy.interpreter import Database, Variable
from prologpy.parser import Parser
from collections import defaultdict


class Solver(object):
    def __init__(self, rules_text):
        """Parse the rules text and initialize the database we plan to use to query
        our rules."""
        rules = Parser(rules_text).parse_rules()
        self.database = Database(rules)

    def find_solutions(self, query_text):
        """Parse the query text and use our database rules to search for matching
        query solutions. """
        pass
