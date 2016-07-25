from distutils.core import setup

setup(
    name     = 'quickpy',
    url      = 'http://github.com/slezica/quick-py',
    version  = '1.0.0',
    packages = ['quickpy'],
    scripts  = ['bin/py'],

    author       = 'Santiago Lezica',
    author_email = 'salezica@gmail.com',

    description = 'Quick python for command-line pipelines',
)
