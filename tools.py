import sys, ast, config


def error(err, abort = True):
    message = str(err)

    if isinstance(err, Exception):
        message = type(err).__name__ + ": " + message

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
    try:
        return NameCollector().detect(ast.parse(expr))

    except SyntaxError:
        error("SyntaxError: " + expr)


def evaluate(expr, context):
    try:
        return eval(expr, context)

    except Exception as e:
        error(e, abort = not config.ignore_exceptions)
