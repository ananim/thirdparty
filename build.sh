#!/bin/sh
for d in `find . -depth 1 -type d`; do
  [ -f $d/setup.py ] && {
    echo ======\> running $d/setup.py build
    (cd $d; python setup.py build)
  }
done
