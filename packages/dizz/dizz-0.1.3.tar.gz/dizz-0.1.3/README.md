# dizz

An extremely fast Python SQL formatter, written in Rust.

## Developing

Create a new virtual environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then you can run the `maturin` tool (which should be installed):

```bash
maturin develop
```

This will build the Rust code and install the Python package within the virtual environment. Allowing you to open up a python console and import the package:

```python
>>> import dizz
>>> dizz.fmt_sql("SELECT * FROM foo")
'SELECT\n    *\nFROM\n    foo'
```
