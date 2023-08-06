from subprocess import run


def _run(cmd: str) -> None:
    run(cmd, shell=True)


_run("touch TEST_QPANDAS_OUTPUT")
_run("py ./tests/test_qpandas.py > TEST_QPANDAS_OUTPUT")

README = f"""\
# qpandas


---


WORK IN PROGRESS


---


Query Panadas DataFrames with SQL


## Install

Currently available on [PyPI](https://pypi.org/project/qpandas/), to install:
```
pip install qpandas
```

## Example

```py
{''.join(open('./tests/test_qpandas.py').readlines())}```
```
{open('TEST_QPANDAS_OUTPUT').read()}```

### Example explanation
TODO
"""

_run("rm TEST_QPANDAS_OUTPUT")


if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(README)
