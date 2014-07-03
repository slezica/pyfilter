# These values will be overridden by user-selected ones.

# Skip items that cause exceptions:
ignore_exceptions = True

# Use expression as filter, and print passing lines:
condition = False

# Commands to execute before and after processing starts:
before = None
after  = None


# ---


OPTIONS = [key for key in globals().keys() if not key.startswith('__')]

def update(args):
    for option in OPTIONS:
        globals()[option] = getattr(args, option)