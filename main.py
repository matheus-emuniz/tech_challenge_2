import streamlit as st
import pandas as pd
import numpy as np
import random
import string
import math

st.title("Genetic algorithm")


col1, col2 = st.columns(2)

with col1:
    with st.form("config_form"):
        st.header("Password configuration")

        length = st.slider("Max length", 8, 64, value=32)
        upper = st.checkbox("Uppercase")
        lower = st.checkbox("Lowercase")
        digits = st.checkbox("Digits")
        special = st.checkbox("Special characters")

        st.header("Algorithm configuration")

        generations = st.slider("Generations", 1, 2000, value=1000)
        mutation_rate = st.slider(
            "Mutation rate", 0.0, 1.0, format="%0.2f", step=0.01, value=0.1
        )
        tournament_size = st.slider("Tournament size", 1, 10, value=5)
        population_size = st.slider("Population size", 1, 500, value=100)

        st.form_submit_button("Submit")


with col2:
    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )

    st.line_chart(chart_data, x="col1", y="col2", color="col3")


# This is outside the form
# st.write(my_number)
st.write(upper)
