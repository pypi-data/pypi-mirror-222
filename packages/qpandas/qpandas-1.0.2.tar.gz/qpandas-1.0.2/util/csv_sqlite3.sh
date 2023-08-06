#!/usr/bin/env bash
set -eou pipefail
sqlite3 x.db ".mode csv" ".import ../src/qpandas/data/meat.csv meat"
sqlite3 x.db
