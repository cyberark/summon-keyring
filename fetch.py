#!/usr/bin/env python

import keyring
import os
import sys

if __name__ == '__main__':
    variable = sys.argv[1]
    value = keyring.get_password(
        os.environ.get('SUMMON_KEYRING_SERVICE', 'summon'),
        variable
    )
    if value is None:
        sys.stderr.write('{} could not be retrieved'.format(variable))
        sys.stderr.flush()
        sys.exit(1)

    sys.stdout.write(value)
    sys.stdout.flush()
