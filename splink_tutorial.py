import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

from splink.duckdb.linker import DuckDBLinker
from splink.duckdb.blocking_rule_library import block_on
import splink.duckdb.comparison_library as cl
import splink.duckdb.comparison_template_library as ctl
# import altair as alt
# alt.renderers.enable('mimetype') # html
# from IPython.display import IFrame

st.title('Test Splink library')
st.header('Load and display the dataset')

@st.cache_data
def load_splink_data():
    df = pd.read_csv('fake_1000_from_splink_demos.csv')
    return df

df = load_splink_data()
st.write(df)

settings = {
    "link_type": "dedupe_only",
    "comparisons": [
        ctl.name_comparison("first_name"),
        ctl.name_comparison("surname"),
        ctl.date_comparison("dob", cast_strings_to_date=True),
        cl.exact_match("city", term_frequency_adjustments=True),
        ctl.email_comparison("email", include_username_fuzzy_level=False),
    ],
    "blocking_rules_to_generate_predictions": [
        block_on("first_name"),
        block_on("surname"),
    ],
    "retain_matching_columns": True,
    "retain_intermediate_calculation_columns": True,
}

linker = DuckDBLinker(df, settings)
# linker.missingness_chart()
# st.write(linker.missingness_chart())


# deterministic_rules = [
#     "l.first_name = r.first_name and levenshtein(r.dob, l.dob)",
#     "l.surname = r.surname and levenshtein(r.dob, l.dob)",
#     "l.first_name = r.first_name and levenshtein(r.surname, l.surname)",
#     "l.email = r.email"
# ]
# linker.estimate_probability_two_random_records_match(deterministic_rules, recall=0.7)
# linker.estimate_u_using_random_sampling(max_pairs=1e6)
# linker.estimate_m_from_label_column("dob")
# training_blocking_rule = block_on(["first_name", "surname"])
# training_session_fname_sname = linker.estimate_parameters_using_expectation_maximisation(training_blocking_rule)

# training_blocking_rule = block_on("dob")
# training_session_dob = linker.estimate_parameters_using_expectation_maximisation(training_blocking_rule)

# st.subheader('Visualising model parameters')
# linker.match_weights_chart()
# st.write(linker.match_weights_chart())
# linker.m_u_parameters_chart()
# st.write(linker.m_u_parameters_chart())

# Saving the model
# settings = linker.save_model_to_json('saved_model.json', overwrite=True)

# st.subheader('Detecting unlinkable records')
# linker.unlinkables_chart()
# st.write(linker.unlinkables_chart())

# Load estimated model
# linker = DuckDBLinker(df)
# linker.load_model('saved_model.json')

# st.subheader('Predicting match weights using the trained model')
# df_predictions = linker.predict(threshold_match_probability=0.2)
# predictions = df_predictions.as_pandas_dataframe()
# predictions
# st.write(predictions)

# st.subheader('Clustering')
# clusters = linker.cluster_pairwise_predictions_at_threshold(df_predictions, threshold_match_probability=0.5)
# clusters_pd = clusters.as_pandas_dataframe()
# clusters_pd
# st.write(clusters_pd)

# sql = f"""
#         select * 
#         from {df_predictions.physical_name}
#         limit 2
#         """
# linker.query_sql(sql)
# st.write(linker.query_sql(sql))


# st.subheader('Visualise predictions. Waterfall chart')
# records_to_view  = df_predictions.as_record_dict(limit=5)
# linker.waterfall_chart(records_to_view, filter_nulls=False)
# st.write(linker.waterfall_chart(records_to_view, filter_nulls=False))

# st.subheader('Comparison viewer dashboard')
# linker.comparison_viewer_dashboard(df_predictions, "scv.html", overwrite=True)
# st.write(linker.comparison_viewer_dashboard(df_predictions, "scv.html", overwrite=True))

# st.subheader('Cluster studio')
# df_clusters = linker.cluster_pairwise_predictions_at_threshold(df_predictions, threshold_match_probability=0.5)
# linker.cluster_studio_dashboard(df_predictions, df_clusters, "cluster_studio.html", sampling_method="by_cluster_size", overwrite=True)
# IFrame(src="./cluster_studio.html", width="100%", height=1200)
# st.write(IFrame(src="./cluster_studio.html", width="100%", height=1200))