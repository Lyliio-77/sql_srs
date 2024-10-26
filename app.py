# Imports
import streamlit as st
import pandas as pd
import duckdb
import io


# Boissons
csv = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))

# Nourriture
csv2 = """
food_item,price
cookie,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))

# Solution
answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()

st.header("Entrez votre code:")
query = st.text_area(label="Votre code SQL ici",key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("Table : beverages")
    st.dataframe(beverages)
    st.write("Table : food_items")
    st.dataframe(food_items)
    st.write("Solution")
    st.dataframe(solution)

with tab3:
    st.write(answer)