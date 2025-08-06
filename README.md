# ⚽ Brasileirão Data Pipeline – PostgreSQL Integration 🇧🇷

A simple and modular Python project to manage **match result data** from the Brazilian football league (Brasileirão).  
This project connects to a PostgreSQL database, scrapes match data from a website, compares it with the data in the database, and inserts **only new rows**.

---

## 📌 What This Project Does

✅ Connects to a remote PostgreSQL database (Supabase)
✅ Fetches match results from a website
✅ Compares new data with existing database entries  
✅ Injects only the missing rows into the table (no duplicates)  

---

## 🧠 Project Structure and Flow

1. **Load Environment Variables**  
   Use `os.getenv()` to load database credentials (`SUPABASE_URL`, `SUPABASE_KEY`).  
   If any are missing, the script raises an error immediately.

2. **Create connection**  
   Connects to the Supabase using `supabase.client`.

3. **Load Existing Data from Database**  
   Uses `pd.read_sql_table()` to load current match data into a DataFrame.

4. **Scrape New Data from Website**  

5. **Compare and Find New Rows**  
   Drops irrelevant columns (if needed), and uses `set(df.index)` to find rows in the scraped data not already in the database.

6. **Insert Only Missing Rows**  

---

## 🔐 Environment Variables Required

The script relies on the following environment variables:

| Variable       | Purpose      |
|----------------|--------------|
| `SUPABASE_URL` | Database url |
| `SUPABASE_KEY` | Database key |


You can set these in a `.env` file (recommended) or directly in the terminal.

---

## 🧪 Example `.env` File

```env
SUPABASE_URL=my_urm
SUPABASE_key=my_key
```


👨‍💻 Author
Vinicius Rodrigues De Almeida
📍 Lyon, France
Mechanical/process engineer exploring data science and software engineering.

🔗 https://www.linkedin.com/in/vinicius-rodrigues-de-almeida-2a575084/

🧠 Interested in: Optimization, Machine Learning, AI, Software Design