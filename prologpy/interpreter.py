from functools import reduce


class Term(object):
    """Prolog has only one data type — the term.

    The simplest term is an atom. Atoms can be combined to form compound terms.
    Example: are_friends(mark, michael) is a compound term where are_friends is
    called a functor and mark and michael are arguments.
    """

    def __init__(self, functor, arguments=None):
        if not arguments:
            arguments = []
        self.functor = functor
        self.arguments = arguments

    def match_variable_bindings(self, other_term):
        """Return a map of matching variable bindings"""
        pass

    def substitute_variable_bindings(self, variable_bindings):
        """Take the variable bindings map and return a term with all occurrences of
        the term variables replaced with the corresponding variable values from our
        variable bindings map.
        """
        pass

    def query(self, database):
        """Query the database for terms matching this one"""
        pass

    def __str__(self):
        return (
            str(self.functor)
            if len(self.arguments) == 0
            else str(self.functor)
            + " ( "
            + ", ".join(str(argument) for argument in self.arguments)
            + " ) "
        )

    def __repr__(self):
        return str(self)


class TRUE(Term):
    """A predefined term used to represent facts as rules. i.e. functor(argument1,
    argument2) for example gets translated to functor(argument1, argument2) :- TRUE """

    # TODO should take no arguments?
    def __init__(self, functor="TRUE", arguments=None):
        if not arguments:
            arguments = []
        super().__init__(functor, arguments)

    def substitute_variable_bindings(self, variable_bindings):
        # Simply return our truth term since there is nothing to bind
        pass

    def query(self, database):
        pass


class Variable(object):
    """A variable is a type of term. Variables start with an uppercase letter and
    represent placeholders for actual terms. """

    def __init__(self, name):
        self.name = name

    def match_variable_bindings(self, other_term):
        """ If the passed in term doesn't represent the same variable, we bind our
        current variable to the outer term and return the mapped binding. """
        pass

    def substitute_variable_bindings(self, variable_bindings):
        """Fetch the currently bound variable value for our variable and return the
        substituted bindings if our variable is mapped. If our variable isn't mapped,
        we simply return the variable as the substitute. """
        pass

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)


class Rule(object):
    """Rules are used to define relationships between facts and other rules.They
    allow us to make conditional statements about our world. Let's say we want to say
    that all humans are mortal. We can do so using the rule below: mortal(X) :-
    human(X) """

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __str__(self):
        return str(self.head) + " :- " + str(self.tail)

    def __repr__(self):
        return str(self)


class Conjunction(Term):
    """# A conjunction is a logical operator that connects two terms. A conjunction
    between the two terms will result in the expression evaluating to true only if
    both terms evaluate to true. As an example, we could state that a teacher
    teaches another student if the student lectures a course and the student
    studies the course using the rule below:

    teaches(Teacher, Student) :- lectures(Teacher, Course), studies(Student, Course).

    """

    def __init__(self, arguments):
        super().__init__("", arguments)

    def query(self, database):
        """Return a generator that iterates over all of the conjunction terms which
        match the database rules. """
        pass

    def substitute_variable_bindings(self, variable_bindings):
        """ Take the variable bindings map and return a conjunction with all
        occurrences of the variables present in our current conjunction terms
        replaced with a list of terms containing the substituted variable bindings
        from our variable bindings map.

        """
        pass

    def __str__(self):
        return ", ".join(str(argument) for argument in self.arguments)

    def __repr__(self):
        return str(self)


class Database(object):
    """The database object is an object which contains a list of our declared rules.

    It's used to query our data for items matching a goal. It also contains the
    helper function used to merge variable bindings.

    """

    def __init__(self, rules):
        self.rules = rules

    def query(self, goal):
        """Return a generator that iterates over all of the terms matching the given
        goal.

        """
        pass

    @staticmethod
    def merge_bindings(first_bindings_map, second_bindings_map):
        """Takes two variable binding maps and returns a combined bindings map if
        there are no conflicts. If any of the bound variables are present in both
        bindings maps but the terms they are bound to do not match, merge_bindings
        returns None. """
        pass

    def __str__(self):
        return ".\n".join(str(rule) for rule in self.rules)

    def __repr__(self):
        return str(self)
