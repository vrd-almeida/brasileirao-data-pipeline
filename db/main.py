import pandas as pd
import os
from db_config import supabase

from load_data import get_data_from_csv, get_data_from_database


def execute_query() -> None:

    df_database = get_data_from_database(supabase)

    df_csv = get_data_from_csv()

    index_diff = ~df_csv.index.isin(df_database.index)

    df_to_inject = df_csv.loc[index_diff]

    df_to_inject["Date"] = df_to_inject["Date"].apply(lambda x: x.isoformat())

    if len(df_to_inject) > 0:

        execution_mode = os.getenv("EXECUTION_MODE", "test")

        if execution_mode == "test":
            print(
                f"✅ Test has been executed: {len(df_to_inject)} row(s) to be injected."
            )
            return
        elif execution_mode != "production":
            raise ValueError(f"execution_mode must be 'test' or 'production'")

        records = df_to_inject.reset_index().to_dict(orient="records")

        n = len(df_to_inject)
        print(f"There are {n} row(s) to be injected...")
        i = 0
        time_initial = pd.Timestamp.now()
        for record in records:
            supabase.table("matches").insert(record).execute()
            i = i + 1
            if i % 10 == 0:
                time_remaining = (pd.Timestamp.now() - time_initial) * (n - i) / i
                total_seconds = int(time_remaining.total_seconds())
                minutes, seconds = divmod(total_seconds, 60)
                print(
                    f"{round(100*i/n, 2)}% completed... time remaining: {minutes}min{seconds:02d}s"
                )
        print(f"100% completed.")
        print(
            f"✅ Data has been injected to database: {len(df_to_inject)} row(s) injected."
        )

    else:
        print("✅ Database was already up to date; no data injected.")

    return


if __name__ == "__main__":
    execute_query()
