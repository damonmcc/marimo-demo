import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # marimo at DCP and HPD
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What is [marimo](https://marimo.io/)?

    marimo is an [open-source](https://github.com/marimo-team/marimo) reactive Python notebook.

    It's a modern version of Jupyter notebooks.

    It's a Python package.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Still just a notebook
    """)
    return


@app.cell
def _():
    my_value = "100"
    return (my_value,)


@app.cell
def _(my_value):
    print(my_value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Reactive cells
    """)
    return


@app.cell(hide_code=True)
def _(changed, mo):
    (
        mo.md(
            f"""
            **✨ Nice!** The value of `changed` is now {changed}.

            When you updated the value of the variable `changed`, marimo
            **reacted** by running this cell automatically, because this cell
            references the global variable `changed`.

            Reactivity ensures that your notebook state is always
            consistent, which is crucial for doing good science; it's also what
            enables marimo notebooks to double as tools and  apps.
            """
        )
        if changed
        else mo.md(
            """
            **🌊 See it in action.** In the next cell, change the value of the
            variable  `changed` to `True`, then click the run button.
            """
        )
    )
    return


@app.cell
def _():
    changed = False
    return (changed,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### interactive UI elements
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    return (slider,)


@app.cell(hide_code=True)
def _(mo, slider):
    mo.md(f"""
    marimo is a **reactive** Python notebook.

    This means that unlike traditional notebooks, marimo notebooks **run automatically** when you modify them or interact with UI elements...

    Like this slider: {slider}.

    {"Icons: " + "🍃" * slider.value}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `marimo tutorial intro`
    - [marimo docs - Getting Started](https://docs.marimo.io/getting_started/)
    - [marimo docs - Key Concepts](https://docs.marimo.io/getting_started/key_concepts/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Why and how we use it
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Why

    I'm a data engineer who likes Python and SQL.

    I used [Jupyter](https://jupyter.org/) notebooks to incrementally write Python code, explore data, and produce data.

    But Jupyter notebooks have some issues:
    - Jupyter lets developers execute cells one at a time, in any order, with each cell potentially modifying variables.
        - This "hidden state" is a problem for reproducibility. It’s why when you receive a notebook from a colleague and try to run it from top to bottom, the notebook often breaks.
        - "Over 75% of Jupyter notebooks on GitHub don’t run, 96% of notebooks don’t reproduce" according to a [2019 research paper](https://marimo.io/features/vs-jupyter-alternative).
    - The notebook's file format isn't plaintext, it's JSON
    - The final documents lack interactivity

    **Error-prone scratchpads shouldn't be our only option.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unlike Jupyter notebooks, marimo notebooks are:
    - reproducible
    - execute reactively
    - have interactive elements built-in
    - stored as pure Python
    - versionable with Git
    - deployable as web apps,
    - executable as scripts

    [marimo docs - What problems does marimo solve?](https://docs.marimo.io/faq/#faq-problems)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Notebooks are plain Python files

    This entire presentation is a `.py` file that looks like this:

    ```python
    @app.cell(hide_code=True)
    def _(mo):
        mo.md("# marimo at DCP and HPD")
        return
    ```

    - `git diff` works on it
    - Code review works on it
    - You can open it in any editor
    - `grep` and other CLI tools work on it
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### How
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have a lot of files and databases, often in the cloud.

    We often want to query them using python and SQL.

    So we use marimo notebooks:
    - [DCP Data Engineering wiki - Python management with uv](https://github.com/NYCPlanning/data-engineering/wiki/Python-management-with-uv)
    - Create and use a notebook
    - Save in it the "experimental" or "notebooks" folder
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We use it to:
    - Interact with data
        - `marimo edit exploration.py`
    - create runnable python scripts
        - `marimo run production.py`
    - create applications
        - `marimo export html-wasm --mode run application.py`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## DCP examples
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Engineering team
    - Explore our source data files ([GitHub](https://github.com/NYCPlanning/data-engineering/blob/main/experimental/dm/marimo_stuff/edm_recipes.py))
    - Maps! ([GitHub](https://github.com/NYCPlanning/data-engineering/blob/main/experimental/dm/marimo_stuff/leafmap_duckdb.py))
    - Compare the versions of data on our website and our Open Data pages (decided to do in our Streamlit app instead)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Helping OMB with census tract issue

    **Last November, a friend at OMB needed help cleaning census tract data.**
    - So, you know how we have census tracts? And there are different labels for them? Ctlable, ct2020, and boroct2020?
    - I have a bunch of data that uses the ctlabel, but those aren't unique across the City.
    - I need to somehow convert the ctlabel census codes to their correct boroct2020
        - Over the summer I thought I had found a formula in excel that would place a bunch of 0s in the ctlabel, but it didn't work 100% of the time, so I had a really horrible data cleaning process that I did by hand, but I don't have enough time to repeat that process now.
    - **Do you have any idea how I can convert ctlabel to boroct2020?**

    **I used marimo to quickly learn about and then transform the data.** ([GitHub](https://github.com/damonmcc/marimo-demo/blob/main/notebooks/clean_census_data_notebook.py))
    - "The attached file is what HPD sends me"
    - I Downloaded DCP's census tracts data from Open Data
    - ...
    - **"I joined the two tables using Borough Name + CTLabel and it worked!"**
    - **"Success!!! Thank you so much again. You have no idea how much this has saved my time!!!!"**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Land Use Lookup

    A marimo notebook deployed as a public website via GitHub pages ([GitHub repo](https://github.com/NYCPlanning/land-use-lookup/), [Application](https://nycplanning.github.io/land-use-lookup/))

    - Transform data
        - `marimo run process_data.py`
    - QA data
        - `marimo edit query_qa.py`
    - Create an application
        - `marimo export html-wasm --mode run query_app.py`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cool stuff
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Table UI
    """)
    return


@app.cell
def _(mo):
    simple_table = mo.ui.table(
        [
            {"agency": "DCP", "full_name": "Dept. of City Planning"},
            {"agency": "HPD", "full_name": "Housing Preservation & Development"},
            {"agency": "DOT", "full_name": "Dept. of Transportation"},
            {"agency": "DEP", "full_name": "Dept. of Environmental Protection"},
        ],
        label="Select rows",
    )
    simple_table
    return (simple_table,)


@app.cell
def _(mo, simple_table):
    mo.md(f"""
    **{len(simple_table.value)}** row(s) selected
    """)
    return


@app.cell
def _(mo):
    import numpy as _np
    import pandas as pd

    _rng = _np.random.default_rng(42)
    _n = 30
    _boroughs = (
        ["Manhattan"] * 6
        + ["Bronx"] * 7
        + ["Brooklyn"] * 8
        + ["Queens"] * 6
        + ["Staten Island"] * 3
    )
    housing_df = pd.DataFrame(
        {
            "community_district": range(1, _n + 1),
            "borough": _boroughs,
            "residential_units": _rng.normal(18_000, 5_000, _n)
            .clip(3_000)
            .astype(int),
            "buildings": _rng.normal(4_000, 1_200, _n).clip(500).astype(int),
            "open_violations": _rng.normal(900, 280, _n).clip(50).astype(int),
            "median_rent": _rng.normal(2_200, 420, _n).clip(1_000).astype(int),
        }
    )
    table = mo.ui.table(
        housing_df, label="Select community districts", show_column_summaries=True
    )
    table
    return housing_df, table


@app.cell
def _(mo, table):
    mo.md(
        f"""
    **{len(table.value)}** borough(s) selected — {table.value["residential_units"].sum():,} total residential units
    """
        if len(table.value) > 0
        else "**Select rows** to see a summary"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### SQL with DataFrames and DuckDB
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    marimo notebooks have SQL cells to query DataFrames and databases
    """)
    return


@app.cell
def _(housing_df, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM housing_df
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    DuckDB can query remote Parquet files directly — no download needed.

    Here we're querying **millions of NYC taxi trips** from a remote file on the [TLC website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page):
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT
            COUNT(*) AS row_count,
        FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-02.parquet')
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SUMMARIZE SELECT * FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-02.parquet')
        -- SUMMARIZE TABLE 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-02.parquet'
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT
            hour(tpep_pickup_datetime) AS pickup_hour,
            COUNT(*)                   AS trips,
            ROUND(AVG(fare_amount), 2) AS avg_fare,
            ROUND(AVG(trip_distance), 2) AS avg_distance_mi
        FROM read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-02.parquet')
        GROUP BY pickup_hour
        -- USING SAMPLE 10%
        ORDER BY pickup_hour
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Or a classic demo dataset — **nycflights13** (~336K rows, NYC-relevant):
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Stacking UI elements
    """)
    return


@app.cell
def _(mo):
    topic = mo.ui.dropdown(
        ["Zoning", "Housing", "Transportation"], label="Topic", value="Housing"
    )
    count = mo.ui.number(1, 100, value=3, label="Results")
    horizontal_stack = mo.hstack([topic, count], justify="center")
    horizontal_stack
    return count, topic


@app.cell
def _(count, mo, topic):
    mo.md(f"""
    Showing **{count.value}** results for **{topic.value}**
    """)
    return


if __name__ == "__main__":
    app.run()
