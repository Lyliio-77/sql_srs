# pylint: disable=missing-module-docstring # pour désactiver l'erreur pylint car notre code n'est pas un module

# Imports des librairies
import io
import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb",read_only=False)

#solution_df = duckdb.sql(ANSWER_STR).df()

st.write("SQL SRS Spaced Repetition SQL practice")

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

st.header("Entrez votre code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)
#
#     # Test
#     if len(result.columns) != len(solution_df.columns):
#         st.write("Il manque des colonnes")
#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         st.write("Il manque des colonnes")
#
#     n_lines_differences = abs(result.shape[0] - solution_df.shape[0])
#     if n_lines_differences != 0:
#         st.write(
#             f"Le résultat a {n_lines_differences} lignes différentes par rapport à la solution"
#         )
#
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("Table : beverages")
#     st.dataframe(beverages)
#     st.write("Table : food_items")
#     st.dataframe(food_items)
#     st.write("Solution")
#     st.dataframe(solution_df)
#
# with tab3:
#     st.write(ANSWER_STR)
