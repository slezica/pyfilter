import sys, ast, config


def abort(*message):
    sys.stderr.write(' '.join(str(part) for part in message) + '\n')
    sys.exit(1)


class Context(dict):
    "Global dictionary for eval(). Has built-ins and imports modules lazily."

    def __missing__(self, key):
        if key in __builtins__:
            return __builtins__[key]

        try:
            return __import__(key)
        except ImportError:
            abort("%s should be a built-in, variable or module" % key)


class NameDetector(ast.NodeVisitor):
    "AST walker that detects identifiers. Used to auto-detect input mode."

    def visit_Name(self, node):
        self.names.add(node.id)
        super(NameDetector, self).generic_visit(node)

    def detect(self, expr):
        self.names = set()
        self.visit(expr)
        return self.names

def detect_names(expr):
    return NameDetector().detect(ast.parse(expr))


def evaluate(expr, context):
    try:
        return eval(expr, context)

    except Exception as e:
        sys.stderr.write(str(e) + '\n')

        if config.ignore_exceptions:
            return None

        sys.exit(1)
