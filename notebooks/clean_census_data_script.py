import pandas as pd


def run():
    dcp_census_tracts_source = pd.read_csv(
        ".data/2020_Census_Tracts_20251107.csv", dtype=str
    )
    dcp_census_tracts_source



    dcp_census_tracts = dcp_census_tracts_source.copy()
    dcp_census_tracts["CTLabel"] = dcp_census_tracts["CTLabel"].str.replace(
        ".", ""
    )
    dcp_census_tracts



    hpd_census_tracts_source = pd.read_csv(".data/HPD_census_tracts.csv", dtype=str)
    hpd_census_tracts = hpd_census_tracts_source
    hpd_census_tracts



    dcp_census_tracts[["CTLabel", "BoroName"]]



    hpd_census_tracts_source[["HPD CTLabel", "Borough Name"]]



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



    merged_tracts[merged_tracts["_merge"] == "both"]



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



    hpd_tracts_export = tracts_export[tracts_export["Is in HPD data"]]
    hpd_tracts_export



    tracts_export.to_csv(".data/tracts_export.csv", index=False)
    hpd_tracts_export.to_csv(".data/hpd_tracts_export.csv", index=False)

if __name__ == "__main__":
    run()
