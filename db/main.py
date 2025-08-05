from db_config import engine

from load_data import get_data_from_csv, get_data_from_database


def execute_query() -> None:

    df_database = get_data_from_database(engine)

    df_csv = get_data_from_csv()

    index_diff = set(df_csv.index.astype(int)) - set(df_database.index.astype(int))

    df_to_inject = df_csv.loc[list(index_diff), :]

    if len(df_to_inject) > 0:

        df_to_inject.to_sql("matches", engine, if_exists="append", index=True)
        print(
            f"✅ Data has been injected to database: {len(df_to_inject)} row injected."
        )

    else:
        print("✅ Database was already up to date; no data injected.")

    return
