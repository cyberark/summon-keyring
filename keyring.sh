#!/usr/bin/env bash
set -e

variable=$1

pip show keyring > /dev/null
OUT=$?
if [ $OUT -ne 0 ]; then
  pip install keyring
fi

./fetch.py ${variable}

