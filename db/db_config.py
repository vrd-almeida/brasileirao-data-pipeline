import os
from supabase import create_client, Client


SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

if SUPABASE_URL is None or SUPABASE_KEY is None:
    raise ValueError(
        "❌ SUPABASE_URL and SUPABASE_KEY must be defined as environment variables."
    )

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
