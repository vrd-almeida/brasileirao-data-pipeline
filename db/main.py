from db_config import engine

from load_data import get_data_from_csv, get_data_from_database


def execute_query() -> None:

    df_database = get_data_from_database(engine)

    df_csv = get_data_from_csv()
    df_dropped = df_csv.drop(
        ["Country", "League", "Time", "BFECH", "BFECD", "BFECA"], axis=1
    )
    df_dropped.to_sql("matches", engine, if_exists="replace", index=False)

    index_diff = set(df_csv.index.astype(int)) - set(df_database.index.astype(int))

    df_to_inject = df_csv.loc[list(index_diff), :]

    df_to_inject.to_sql("matches", engine, if_exists="append", index=False)

    return
