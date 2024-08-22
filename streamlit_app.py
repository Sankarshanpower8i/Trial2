import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Sales dashboard',
    page_icon='data:image/png;base64,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', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 2016
    MAX_YEAR = 2024

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''

min_value = gdp_df['Year'].min()
max_value = gdp_df['Year'].max()

from_year, to_year = st.slider(
    'Which years are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

countries = gdp_df['Country Code'].unique()

if not len(countries):
    st.warning("Select at least one country")

selected_countries = st.multiselect(
    'Which countries would you like to view?',
    countries,
    ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

''
''
''

# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
