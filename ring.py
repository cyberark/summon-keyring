#!/usr/bin/env python

import os
import sys

def write_and_flush(pipe, message):
    pipe.write(message)
    pipe.flush()

try:
    import keyring
except ImportError:
    write_and_flush(sys.stderr, '"keyring" library missing, run "pip install keyring"')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        write_and_flush(sys.stderr, 'No variable was provided.')
        sys.exit(1)

    variable = sys.argv[1]
    value = keyring.get_password(
        os.environ.get('SUMMON_KEYRING_SERVICE', 'summon'),
        variable
    )
    if value is None:
        write_and_flush(sys.stderr, '{} could not be retrieved'.format(variable))
        sys.exit(1)

    write_and_flush(sys.stdout, value)
