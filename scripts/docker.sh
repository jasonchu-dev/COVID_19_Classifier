#!/bin/bash

count=$(find "/reports" -mindepth 1 -maxdepth 1 -type f | wc -l)

python src/train.py
python src/test.py > reports/report_$count.txt