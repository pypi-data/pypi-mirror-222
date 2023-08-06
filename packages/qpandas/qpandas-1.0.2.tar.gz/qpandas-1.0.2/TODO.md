# Version 0

- [ ] DELETE FROM has no effect unless persist=True, should it?
- [ ] Problem calling MyPandas(URI, persist=True) twice, probably logic error of creating/deleting database twice?
- [ ] Fix remaining two pytest tests from pandasql
- [ ] Add MySQL syntax specific pytest tests in `test_mypandas.py`
- [ ] Fix dependencies not installing based on `pyproject.toml` setting

# Version 1

```py
# syntax idea
#   - want syntax to be more concise
#   - dont need a sqlalchemy connection anymore
import pandas as pd

import qpandas as qpd # lower case
                      # pandas -> pd is convention already, very short!
                      # hard to get pypi names that are shorter than "pandas"
                      # alias is easy was to make it short
                      #
                      # I know google's style guide says:
                      # Use import y as z only when z is a standard
                      # abbreviation (e.g., np for numpy).
                      # but if I just say that's the standard, it's fine

people = pd.read_csv("people.csv")
df1 = qpd.mysql("""
SELECT name
FROM people""", locals())
df2 = qpd.hive("""
SELECT name
FROM people""", locals())
# Use `.mysql`, `.hive` because it's shorter than `qpd.query('mysql',...)`
# `qpd.query` is redundant because of the q twice, q stands for 'query'
# and is longer to type!
```

- [ ] Use sqlglot to transpile every dialect into sqlite, then you just need to support sqlite internally and then you can support every dialect, and the code actually gets simpler... Or you could leave in the current mysql/postgres/sqlite connection details and add the transpile logic. IMO it's annoying to provide a mysql connection. You could just do `MyPandas('mysql')(QUERY, locals())` instead of `MyPandas("mysql://root:root@localhost/")(QUERY, locals())`.
    - [ ] When loading dataframe into sqlite, you get behavior that isn't exactly like mysql. Example, loading a date `YYYY-MM-DD` into sqlite you get `"date" TEXT` in the format `ISO 8601`, so like `2012-06-01 00:00:00`. Which is changing the data just from loading it :( One thing I was thinking could be done was to use a custom insertion method for the dataframe https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-sql-method. Infact the datetime behavior is described here https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#datetime-data-types.
    - [ ] The second problem is that sqlglot isn't doing what I thought it would, here's an example:
    ```py
    >>> from sqlglot import transpile
    >>> transpile('select year(date) from meat', read='mysql', write='sqlite')
    ['SELECT YEAR(date) FROM meat']
    ```
    "SQLite supports six date and time functions as follows:" https://www.sqlite.org/lang_datefunc.html, `YEAR` isn't one of them I don't think? I don't understand the internal details and I'm unsure if the mysql year function is unsupported https://github.com/tobymao/sqlglot/blob/main/sqlglot/dialects/mysql.py here, although I don't exactly understand how `_date_trunc_sql(self, expression)` works internally. I was expecting sqlglot to do some form of `strftime` to mimmick the year function. I'm not sure if this is a `mysql.py` or a `sqlite.py` https://github.com/tobymao/sqlglot/blob/main/sqlglot/dialects/sqlite.py feature.
- [x] Name change? If I'm supporting every dialect naming it MyPandas is confusing. Can't use `pandasql` it's used on pypi, come up with better name.
    - What about `qpandas`, it's available. `import qpandas as qpd; qpd.mysql(QUERY, locals())`
- [ ] Does sqlglot support paramaterized query transpilation?
- [ ] How do you tell if a string is a sqlalchemy connection? Maybe look at the internal code in https://docs.sqlalchemy.org/en/14/core/engines.html, or do something cheeky. Does some builtin like urlparse work because it's a URI?
- [ ] Copy the CD stuff from ty-command.
- [ ] Update the docstrings
- [ ] Could the example data be simplier? Do we need it for tests?
