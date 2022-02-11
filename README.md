# Random Indian Recipe 🍛🍚🍲🥘
Simple API to suggest one random Indian recipe

Check it out here -> https://random-indian-receipe.herokuapp.com/


### Recipe Database 

CSV data downloded from https://www.kaggle.com/nehaprabhavalkar/indian-food-101

How to prepare database 

```python
import pandas as pd
import sqlite3 as sql

conn = sql.connect('indian_food.db')

df = pd.read_csv(r"path\to\indian_food.csv")
df.to_sql('recipes', conn, if_exists='append', index=False)
```


### Local Testing

To start the app locally 

```bash
uvicorn app:app --reload
```


### Request & Response

```bash
PS> Invoke-RestMethod -Uri http://127.0.0.1:8000/


name           : Mag Dhokli
ingredients    : Moong beans, jaggery, red chillies, oil, salt
diet           : vegetarian
prep_time      : -1
cook_time      : -1
flavor_profile : spicy
course         : snack
state          : Gujarat
region         : West


{"name":"Mag Dhokli","ingredients":"Moong beans, jaggery, red chillies, oil, salt","diet":"vegetarian","prep_time":-1,"cook_time":-1,"flavor_profile":"spicy","course":"snack","state":"Gujarat","region":"West"}

```