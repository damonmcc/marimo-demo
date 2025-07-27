import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Hello World!""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Key concepts""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    There are some [key concepts](https://docs.marimo.io/getting_started/key_concepts/) to marimo notebooks:

    - marimo lets you rapidly experiment with data using Python, SQL, and interactive elements in a reproducible notebook environment.
    - Unlike Jupyter notebooks, marimo notebooks are reusable software artifacts. marimo notebooks can be shared as as interactive web apps and executed as Python scripts.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Reactivity""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    marimo notebooks are reactive: they automatically react to your code changes and UI interactions and keep your notebook up-to-date, not unlike a spreadsheet. This makes your notebooks reproducible, eliminating [hidden state](https://docs.marimo.io/faq/#faq-problems); it's also what enables marimo notebooks to double as apps and Python scripts.

    Try updating the values of variables below and see what happens! You can also try deleting a cell.
    """
    )
    return


@app.cell
def _():
    x = 3
    return (x,)


@app.cell
def _():
    y = 1
    return


@app.cell
def _(x):
    x
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Visualizing outputs""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Use `mo.md` with an `f-string` to create markdown that depends on the value of Python objects.""")
    return


@app.cell
def _():
    name = "Alice"
    return (name,)


@app.cell
def _(mo, name):
    mo.md(f"""Hello, {name}!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Embed marimo UI elements in markdown directly:""")
    return


@app.cell
def _(mo):
    text_input = mo.ui.text(placeholder="My name is ...", debounce=False)
    return (text_input,)


@app.cell
def _(mo, text_input):
    mo.md(
        f"""
    What's your name? {text_input}

    Hello, {text_input.value}!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo, title_slider):
    mo.md(f"## {title_slider.value * 'Interactive elements '}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    One of marimo's most powerful features is its first-class support for interactive user interface (UI) elements, or "widgets", created using [`marimo.ui`](https://docs.marimo.io/api/inputs/).

    Interacting with a UI element bound to a global variable automatically runs all cells that reference it.
    """
    )
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(start=1, stop=10)
    slider
    return (slider,)


@app.cell
def _(slider):
    slider.value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The next example uses a slider and [LaTeX](https://docs.marimo.io/api/markdown/#marimo.md) markdown text to display an exponential function.""")
    return


@app.cell
def _(mo):
    exponent = mo.ui.slider(start=1, stop=9)
    exponent
    return (exponent,)


@app.cell
def _(exponent, mo):
    import math

    mo.md(f"$e^{exponent.value} = {math.exp(exponent.value):0.3}$")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Use the slider below to change the title text of this section!""")
    return


@app.cell
def _(mo):
    title_slider = mo.ui.slider(start=1, stop=5, label="Title Slider")
    title_slider
    return (title_slider,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Dataframes and databases with SQL""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""marimo has built-in support for SQL: you can query Python dataframes, databases, CSVs, Google Sheets, or anything else. After executing your query, marimo returns the result to you as a dataframe, making it seamless to go back and forth between SQL and Python.""")
    return


@app.cell
def _():
    import pandas as pd

    df_cars = pd.read_json(
        "https://raw.githubusercontent.com/vega/vega-datasets/master/data/cars.json"
    )
    df_cars
    return (pd,)


@app.cell
def _(pd):
    import random

    df = pd.DataFrame(
        {
            "category": [random.choice(["A", "B", "C"]) for _ in range(20)],
            "value": list(range(20)),
        }
    )
    return (df,)


@app.cell
def _(df, mo):
    _df = mo.sql(
        f"""
        SELECT
            category,
            MEAN(value) as mean
        FROM df
        GROUP BY category ORDER BY mean;
        """
    )
    return


if __name__ == "__main__":
    app.run()
