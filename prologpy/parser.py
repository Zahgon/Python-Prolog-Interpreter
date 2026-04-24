import re
from prologpy.interpreter import Conjunction, Variable, Term, TRUE, Rule


TOKEN_REGEX = r"[A-Za-z0-9_]+|:\-|[()\.,]"
ATOM_NAME_REGEX = r"^[A-Za-z0-9_]+$"
VARIABLE_REGEX = r"^[A-Z_][A-Za-z0-9_]*$"

# Regex to parse comment strings. The first group captures quoted strings (
# double and single). The second group captures regular comments ('%' for
# single-line or '/* */' for multi-line)
COMMENT_REGEX = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|%[^\r\n]*$)"


def remove_comments(input_text):
    """Return the input text string with all of the comments removed from it"""
    pass


def parse_tokens_from_string(input_text):
    """Convert the input text into a list of tokens we can iterate over / process"""
    pass


class Parser(object):
    """
    NOTE: Instance can only be used once!
    """

    def __init__(self, input_text):
        self._tokens = parse_tokens_from_string(input_text)
        self._scope = None

    def parse_rules(self):
        pass

    def parse_query(self):
        pass

    @property
    def _current(self):
        pass

    def _pop_current(self):
        pass

    def _parse_atom(self):
        pass

    def _parse_term(self):
        # If we encounter an opening parenthesis, we know we're dealing with a
        # conjunction, so we process the list of arguments until we hit a closing
        # parenthesis and return the conjunction object.
        pass

    def _parse_arguments(self):
        pass

    def _parse_rule(self):

        pass
