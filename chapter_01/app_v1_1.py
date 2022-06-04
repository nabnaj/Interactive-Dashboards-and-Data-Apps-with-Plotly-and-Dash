#%% step1: imports
import dash
from dash import html                       #    dash,html
from  dash import   dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import pandas as pd

#%% step2: data
poverty_data = pd.read_csv(r'D:\repos\Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash\data\PovStatsData.csv')

#%% step3: App        
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])#   02  Dash(__name__)

'''
BOOTSTRAP,CERULEAN,COSMO,CYBORG,DARKLY,FLATLY,GRID,JOURNAL,LITERA,LUMEN,LUX,
MATERIA,MINTY,MORPH,PULSE,QUARTZ,SANDSTONE,SIMPLEX,SKETCHY,SLATE,SOLAR,SPACELAB,
SUPERHERO,UNITED,VAPOR,YETI,ZEPHYR

Themes, Grid system:rows/columns  not  pixels/percentages, Responsiveness,
Prebuilt: Alerts/buttons/drop-down menus/tabs , Encoded colors

'''

#%% step4: layout
app.layout = html.Div([                     # html. division 
    html.H1('Poverty And Equity Database', style={'color': 'blue','fontSize': '40px'}),
    html.P('Key Facts:'),                   # H1 H2 P   style_dictionary color/fontSize
    html.Ul([                               #  unordered (bulleted) list
        html.Li('Number of Economies: 170'),# list
        html.Li(['Source: ',                # <a href="https://www.w3schools.com">Visit W3Schools.com!</a>  
    html.A(children='data',href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database') ]),
    
    dcc.Slider(id='slider'),
    html.Br(),
    
    dbc.Tabs([
        dbc.Tab([ html.P('external_stylesheets=[dbc.themes.BOOTSTRAP]'),
                  html.P('external_stylesheets=[dbc.themes.BOOTSTRAP2]')], #list of html in tab
                label="tab1"),
        dbc.Tab( html.P('another tab'), label="tab2") 
    ]),#tabs
    
    dcc.Dropdown(id='country',options=[{'label': country, 'value': country}
                          for country in poverty_data['Country Name'].unique()]),
    html.Br(),
    html.Div(id='report')    
    ])
])

# step5: callbak functions   :  component_id / component_property
@app.callback(Output('report', 'children'),  Input('country', 'value'))
def display_country_report(country):
    if country is None:        return ''
    filtered_df = poverty_data[(poverty_data['Country Name']==country) &
                               (poverty_data['Indicator Name']=='Population, total')]
    population = filtered_df.loc[:, '2010'].values[0]
    return [html.H3(country),  f'The population of {country} in 2010 was {population:,.0f}.']



# step 6: run server
if __name__ == '__main__':
    app.run_server(debug=True,port=8050)
