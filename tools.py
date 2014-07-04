import sys, ast, config


def abort(*message):
    sys.stderr.write(' '.join(str(part) for part in message) + '\n')
    sys.exit(1)


class Context(dict):
    "Global dictionary for eval(). Imports modules lazily."

    def __missing__(self, key):
        return __import__(key)


class NameDetector(ast.NodeVisitor):
    "AST walker that detects identifiers. Used to auto-detect input mode."

    def visit_Name(self, node):
        self.names.add(node.id)
        super(NameDetector, self).generic_visit(node)

    def detect(self, expr):
        self.names = set()
        self.visit(expr)
        return self.names

def detect_variable_names(expr):
    return NameDetector().detect(ast.parse(expr))