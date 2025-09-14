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


def get_data_from_database(supabase) -> pd.DataFrame:
    """Loads all data from Supabase 'matches' table with pagination."""

    all_data = []
    step = 1000
    offset = 0

    while True:
        response = (
            supabase.table("matches")
            .select("*")
            .range(offset, offset + step - 1)
            .execute()
        )

        chunk = response.data
        all_data.extend(chunk)

        if len(chunk) < step:
            break

        offset += step

    df = pd.DataFrame(all_data)
    df.set_index("id", inplace=True)
    validate_dataframe(df)
    df.sort_index(inplace=True)

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

    columns = [
        "Season",
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
    ]

    df_csv = df_csv[columns]

    df_csv.index.name = "id"

    validate_dataframe(df_csv)

    return df_csv
