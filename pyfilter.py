import sys, argparse

import config
from tools import *


def execute(expr, stream):
    # Input handling mode (x: line, l: list of lines, i: one string) is
    # detected by variables used in the expression:
    names   = detect_names(expr)
    special = names.intersection({'x', 'l', 'i'})

    if len(special) > 1:
        abort("Only one of 'x', 'l' and 'i' can be used in the expression")


    context = Context() # dict that auto-imports modules
    context.update(__builtins__.__dict__)

    if len(special) == 0: # ignore input stream
        yield evaluate(expr, context)

    # The only item in special is 'x', 'l' or 'i':
    (mode,) = special

    if mode == 'i':
        context['i'] = stream.read()
        yield evaluate(expr, context)

    elif mode == 'l':
        context['l'] = stream.read().split('\n')
        yield evaluate(expr, context)

    elif mode == 'x':
        for line in stream:
            context['x'] = line.rstrip()
            yield evaluate(expr, context)


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument("expression",
        nargs   = '?',
        default = 'None'
    )

    parser.add_argument("-c", "--condition",
        action = 'store_true',
        help   = "only print lines where expr is true"
    )
    
    parser.add_argument('-i', '--ignore-exceptions',
        action  = 'store_true',
        help    = "skip items that raise exceptions"
    )
    
    parser.add_argument('-b', '--before',
        help = "run command before processing"
    )

    parser.add_argument('-a', '--after',
        help = "run command after processing"
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = cli()
    config.update(args)

    results = execute(args.expression, sys.stdin)

    for result in results:
        if result is not None:
            print str(result).rstrip('\n')