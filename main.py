import streamlit as st
import pandas as pd
import time

from genetic_algorithm import GeneticAlgorithm

st.title("Genetic algorithm")

with st.form("config_form"):
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.subheader("Password configuration")

        length = st.slider("Max length", 8, 64, value=32)
        upper = st.checkbox("Uppercase", value=True)
        lower = st.checkbox("Lowercase", value=True)
        digits = st.checkbox("Digits", value=True)
        special = st.checkbox("Special characters", value=True)

    with col2:
        st.subheader("Algorithm configuration")

        generations = st.slider("Generations", 1, 2000, value=100)
        mutation_rate = st.slider(
            "Mutation rate", 0.0, 1.0, format="%0.2f", step=0.01, value=0.2
        )
        tournament_size = st.slider("Tournament size", 1, 10, value=2)
        population_size = st.slider("Population size", 1, 500, value=100)

    submit = st.form_submit_button("Submit")

if submit:
    with st.container():
        st.subheader("Results")

        initial_df = pd.DataFrame(
            {"generations": [0], "best_fitness": [0.0]},
            columns=["generations", "best_fitness"],
        )

        line_chart = st.line_chart(
            initial_df, x="generations", y="best_fitness")

        ga = GeneticAlgorithm(
            max_length=length,
            population_size=population_size,
            generations=generations,
            mutation_rate=mutation_rate,
            tournament_size=tournament_size,
            uppercase=upper,
            lowercase=lower,
            digits=digits,
            special=special,
        )

        results = ga.genetic_algorithm()

        with st.empty():
            for best_fitness, best_password, generations in results:
                new_row = pd.DataFrame(
                    {"generations": [generations],
                        "best_fitness": [best_fitness]},
                    columns=["generations", "best_fitness"],
                )

                st.session_state.best_password = best_password
                line_chart.add_rows(new_row)

                st.text(
                    f"Best fitness: {best_fitness}\nGeneration: {generations}\nBest password: {best_password}"
                )
