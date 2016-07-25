#!/usr/bin/env python2

import sys, argparse
from tools import *


def parse_args():
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

    return parser.parse_args().__dict__


def main():
    args = parse_args()
    config.update(args)

    results = execute(args['expression'], sys.stdin)

    for result in results:
        if result is not None:
            print str(result).rstrip('\n')


if __name__ == '__main__':
    main()
