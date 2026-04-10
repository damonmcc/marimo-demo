import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import pandas as pd


@app.cell
def _():
    dcp_census_tracts_source = pd.read_csv(
        "2020_Census_Tracts_20251107.csv", dtype=str
    )
    dcp_census_tracts_source
    return (dcp_census_tracts_source,)


@app.cell
def _(dcp_census_tracts_source):
    dcp_census_tracts = dcp_census_tracts_source.copy()
    dcp_census_tracts["CTLabel"] = dcp_census_tracts["CTLabel"].str.replace(
        ".", ""
    )
    dcp_census_tracts
    return (dcp_census_tracts,)


@app.cell
def _():
    hpd_census_tracts_source = pd.read_csv("HPD_census_tracts.csv", dtype=str)
    hpd_census_tracts = hpd_census_tracts_source
    hpd_census_tracts
    return hpd_census_tracts, hpd_census_tracts_source


@app.cell
def _(dcp_census_tracts):
    dcp_census_tracts[["CTLabel", "BoroName"]]
    return


@app.cell
def _(hpd_census_tracts_source):
    hpd_census_tracts_source[["HPD CTLabel", "Borough Name"]]
    return


@app.cell
def _(dcp_census_tracts, hpd_census_tracts):
    merged_tracts = pd.merge(
        left=dcp_census_tracts,
        left_on=["CTLabel", "BoroName"],
        right=hpd_census_tracts,
        right_on=["HPD CTLabel", "Borough Name"],
        how="left",
        indicator=True,
    )
    merged_tracts = merged_tracts.sort_values(by="GEOID", ascending=True)
    merged_tracts
    return (merged_tracts,)


@app.cell
def _(merged_tracts):
    merged_tracts[merged_tracts["_merge"] == "both"]
    return


@app.cell
def _(merged_tracts):
    mapping_dict = {
        "both": True,
        "left_only": False,
    }
    tracts_export = merged_tracts[
        [
            "GEOID",
            "BoroName",
            "BoroCode",
            "CT2020",
            "BoroCT2020",
            "CDEligibil",
            "NTAName",
            "HPD CTLabel",
            "Some Number A",
            "Some Number B",
            "_merge",
        ]
    ]
    # Apply the mapping to the 'Category' column
    tracts_export["Is in HPD data"] = tracts_export["_merge"].map(mapping_dict)
    tracts_export = tracts_export.drop("_merge", axis="columns")
    tracts_export
    return (tracts_export,)


@app.cell
def _(tracts_export):
    hpd_tracts_export = tracts_export[tracts_export["Is in HPD data"]]
    hpd_tracts_export
    return (hpd_tracts_export,)


@app.cell
def _(hpd_tracts_export, tracts_export):
    tracts_export.to_csv("tracts_export.csv", index=False)
    hpd_tracts_export.to_csv("hpd_tracts_export.csv", index=False)
    return


if __name__ == "__main__":
    app.run()
