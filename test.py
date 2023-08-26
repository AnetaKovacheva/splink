import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv('fake_1000_from_splink_demos.csv')
st.write('Hellor **world!** :sunglasses:')

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.title('Title')
st.header('Header')
st.subheader('Subheader')
st.text('Pure text here')
st.markdown('This is a **new** example, please, follow the [link](https://github.com/AnetaKovacheva/splink)')
st.markdown('Just to test how coloured text work. Lets see the :blue[blue] word')
st.markdown('''If you end a line with two spaces,  n\
            a soft return is used for the next line.
            
Just test the two lines''')

st.header('This is a header with a divider - divider does not work')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

st.subheader('This is a subheader with a divider')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.text('This is some text.')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write("This is some text.")
st.slider("This is a slider", 0, 100, (25, 75))
st.divider()  # 👈 Draws a horizontal rule
st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)


df = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [np.random.randint(0, 1000) for _ in range(3)],
        "views_history": [[np.random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")



