# pylint: disable=missing-module-docstring # pour désactiver l'erreur pylint car notre code n'est pas un module

# Imports des librairies
import io
import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# -----------------------------------------------------------------
# EXERCICES LIST
# -----------------------------------------------------------------
data = {
    "theme": ["cross_joins", "cross_joins"],
    "exercise_name": ["beverages_and_food", "sizes_and_trademarks"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
    "last_reviewed": ["1980-01-01", "1970-01-01"],
}

memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# -----------------------------------------------------------------
# CROSS JOIN EXERCICES
# -----------------------------------------------------------------

# Boissons
CSV = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

# Nourriture
CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

# -----------------------------------------------------------------
# CROSS JOIN EXERCICES
# -----------------------------------------------------------------

# Taille
sizes = """
size
XS
S
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

# Marques
trademarks = """
trademark
Nike
Asphalte
Abercombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")
con.close()
