import pandas as pd


expected_columns = {
    "Season",
    "Date",
    "Home",
    "Away",
    "HG",
    "AG",
    "Res",
    "PSCH",
    "PSCD",
    "PSCA",
    "MaxCH",
    "MaxCD",
    "MaxCA",
    "AvgCH",
    "AvgCD",
    "AvgCA",
}


def validate_dataframe(df: pd.DataFrame) -> None:
    actual_columns = set(df.columns)

    # Check if all expected columns are present
    missing_columns = expected_columns - actual_columns
    extra_columns = actual_columns - expected_columns

    if missing_columns:
        print("Missing columns:", missing_columns)

    if extra_columns:
        print("Unexpected columns:", extra_columns)

    if not missing_columns and not extra_columns:
        print("✅ DataFrame has exactly the expected columns.")

    return


def get_data_from_database(engine) -> pd.DataFrame:

    # Example: load entire table into a DataFrame
    df = pd.read_sql("SELECT * FROM matches", con=engine, index_col="id")

    validate_dataframe(df)

    return df


def get_data_from_csv() -> pd.DataFrame:
    # Link direto para o Brasileirão
    url = r"https://www.football-data.co.uk/new/BRA.csv"

    df_csv = pd.read_csv(
        url,
        parse_dates=["Date"],
        dayfirst=True,
        dtype={
            "Country": "string",
            "League": "string",
            "Season": "int64",
            "Time": "string",
            "Home": "string",
            "Away": "string",
            "HG": "Int64",
            "AG": "Int64",
            "Res": "string",
            "PSCH": "float64",
            "PSCD": "float64",
            "PSCA": "float64",
            "MaxCH": "float64",
            "MaxCD": "float64",
            "MaxCA": "float64",
            "AvgCH": "float64",
            "AvgCD": "float64",
            "AvgCA": "float64",
            "BFEC1": "float64",
            "BFECX": "float64",
            "BFECA": "float64",
        },
    )
    df_csv_dropped = df_csv.drop(
        ["Country", "League", "Time", "BFECH", "BFECD", "BFECA"], axis=1
    )

    df_csv_dropped.index.name = "id"

    validate_dataframe(df_csv_dropped)

    return df_csv_dropped
