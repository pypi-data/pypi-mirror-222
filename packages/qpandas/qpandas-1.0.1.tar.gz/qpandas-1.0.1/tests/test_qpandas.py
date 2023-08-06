import pandas as pd

import qpandas as qpd
from qpandas import load_births

births = load_births()
assert type(births) == pd.DataFrame
query = """
SELECT b1.date d1
    , b1.births b1
    , b2.date d2
    , b2.births b2
FROM births b1, births b2
"""
df = qpd.mysql(query, locals())  # or .oracle, .spark, etc...
assert type(df) == pd.DataFrame
print(df)
