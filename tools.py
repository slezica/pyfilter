import sys, ast, config


def error(message = None, exception = None, abort = False):
    if exception:
        message = type(exception).__name__ + ": " + exception.message

    sys.stderr.write(message + '\n')

    if abort:
        sys.exit(1)


class Context(dict):
    "Global dictionary for eval(). Imports modules lazily."

    def __missing__(self, key):
        return __import__(key)


class NameCollector(ast.NodeVisitor):
    "AST walker that detects identifiers. Used to auto-detect input mode."

    def visit_Name(self, node):
        self.names.add(node.id)
        super(NameCollector, self).generic_visit(node)

    def detect(self, expr):
        self.names = set()
        self.visit(expr)
        return self.names

def collect_variable_names(expr):
    return NameCollector().detect(ast.parse(expr))