# pylint: disable=missing-module-docstring # pour désactiver l'erreur pylint car notre code n'est pas un module
import logging

# Imports des librairies
import os
import duckdb
import pandas as pd
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("Création fichier data")
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())


con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# solution_df = duckdb.sql(ANSWER_STR).df()

st.write("SQL SRS Spaced Repetition SQL practice")

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "GroupBy", "window_functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected:", theme)

    exercise = (
        con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
        .df()
        .sort_values("last_reviewed")
        .reset_index()
    )
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()


st.header("Entrez votre code:")
query = st.text_area(label="Votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)
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
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)
