# pylint: disable=missing-module-docstring # pour désactiver l'erreur pylint car notre code n'est pas un module

# Imports des librairies
import io
import duckdb
import pandas as pd
import streamlit as st

## Déclaration des df
# Boissons
CSV = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

# Nourriture
CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

# Solution
ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(ANSWER_STR).df()

st.write("SQL SRS Spaced Repetition SQL practice")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected:", option)


st.header("Entrez votre code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    # Test
    if len(result.columns) != len(solution_df.columns):
        st.write("Il manque des colonnes")
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Il manque des colonnes")

    n_lines_differences = abs(result.shape[0] - solution_df.shape[0])
    if n_lines_differences != 0:
        st.write(
            f"Le résultat a {n_lines_differences} lignes différentes par rapport à la solution"
        )


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("Table : beverages")
    st.dataframe(beverages)
    st.write("Table : food_items")
    st.dataframe(food_items)
    st.write("Solution")
    st.dataframe(solution_df)

with tab3:
    st.write(ANSWER_STR)
