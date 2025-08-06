from db_config import supabase

from load_data import get_data_from_csv, get_data_from_database


def execute_query() -> None:

    df_database = get_data_from_database(supabase)

    df_csv = get_data_from_csv()

    index_diff = set(df_csv.index.astype(int)) - set(df_database.index.astype(int))

    df_to_inject = df_csv.loc[list(index_diff), :]

    df_to_inject["Date"] = df_to_inject["Date"].apply(lambda x: x.isoformat())

    if len(df_to_inject) > 0:

        records = df_to_inject.reset_index().to_dict(orient="records")

        for record in records:
            supabase.table("matches").insert(record).execute()
        print(
            f"✅ Data has been injected to database: {len(df_to_inject)} row injected."
        )

    else:
        print("✅ Database was already up to date; no data injected.")

    return
