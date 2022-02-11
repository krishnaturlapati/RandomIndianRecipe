import uvicorn
import pandas as pd
from fastapi import FastAPI
import sqlite3 as sql

app = FastAPI()

conn = sql.connect('indian_food.db', check_same_thread=False)


@app.get("/", status_code=200)
def get_recipe():
    """ query database and return one recipe """
    sql = "select * from recipes order by random() limit 1"
    return pd.read_sql(sql,conn).to_dict(orient='records')[0]
    

@app.get("/health", status_code=200)
def get_health():
    """ basic health check """
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
