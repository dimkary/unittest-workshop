#!/bin/bash

cd /workspace/unittest-workshop 2>/dev/null 

python3 -m coverage run -m unittest -v
python3 -m coverage report
python3 -m coverage html
