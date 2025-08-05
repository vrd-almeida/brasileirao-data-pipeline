# ⚽ Brasileirão Data Pipeline – PostgreSQL Integration 🇧🇷

A simple and modular Python project to manage **match result data** from the Brazilian football league (Brasileirão).  
This project connects to a PostgreSQL database, scrapes match data from a website, compares it with the data in the database, and inserts **only new rows**.

---

## 📌 What This Project Does

✅ Connects to a local or remote PostgreSQL database  
✅ Fetches match results from a website using `requests` and `pandas.read_html`  
✅ Compares new data with existing database entries  
✅ Injects only the missing rows into the table (no duplicates)  

---

## 🧠 Project Structure and Flow

1. **Load Environment Variables**  
   Use `os.getenv()` to load database credentials (`USER`, `PASSWORD`, `HOST`, `PORT`, `DB_NAME`).  
   If any are missing, the script raises an error immediately.

2. **Create SQLAlchemy Engine**  
   Connects to the PostgreSQL database using the credentials.

3. **Load Existing Data from Database**  
   Uses `pd.read_sql_table()` to load current match data into a DataFrame.

4. **Scrape New Data from Website**  
   Uses `requests` + `pandas.read_html()` to extract match results from a public web page.

5. **Compare and Find New Rows**  
   Drops irrelevant columns (if needed), and uses `set(df.index)` to find rows in the scraped data not already in the database.

6. **Insert Only Missing Rows**  
   Uses `DataFrame.to_sql(..., if_exists="append")` to inject only the new rows into the existing table.

---

## 🔐 Environment Variables Required

The script relies on the following environment variables:

| Variable     | Purpose                   |
|--------------|---------------------------|
| `USER`       | Database username         |
| `PASSWORD`   | Database password         |
| `HOST`       | Host                      |
| `PORT`       | Port                      |
| `DB_NAME`    | Name of the PostgreSQL DB |

You can set these in a `.env` file (recommended) or directly in the terminal.

---

## 🧪 Example `.env` File

```env
USER=postgres
PASSWORD=1234
HOST=localhost
PORT=5432
DB_NAME=brasileirao
```


👨‍💻 Author
Vinicius Rodrigues De Almeida
📍 Lyon, France
Mechanical/process engineer exploring data science and software engineering.

🔗 https://www.linkedin.com/in/vinicius-rodrigues-de-almeida-2a575084/

🧠 Interested in: Optimization, Machine Learning, AI, Software Design