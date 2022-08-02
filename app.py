import dash
import pandas as pd
from dash import dcc, html, Input, Output, dash_table
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc

colors = {
    'bg': 'white',
    'text': '#7FDBFF'
}

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country')
fig.update_layout(paper_bgcolor=colors['bg'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                ])

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app.layout = html.Div([
        html.H3(['Relatório personalizavel com gráficos e tabelas.'], className='title', id='title'),

        html.Div([
            html.Div([
                    html.H4(['Lorem Ipsum'], className='subtitle', id="sub1"),
                    html.P(['   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget libero euismod, consequat sapien ut faucibus tellus.',
                    'Cras placerat ligula sit amet erat maximus, vitae tristique massa pulvinar. Mauris faucibus, libero',
                    'eu faucibus ultrices, sapien purus volutpat diam, eget fringilla libero orci id nibh. Sed ut vestibulum ipsum. Nulla',
                    'lorem neque, efficitur varius libero eu, imperdiet mattis metus. Quisque accumsan egestas risus a condimentum. Nullam',
                    'commodo blandit est sed elementum. Sed non ex ut massa gravida semper sed ut sapien. In hac habitasse platea dictumst.']),
                    html.Div([
                        html.H5(['Fonte: Plotly'], className="cit"),
                        html.A(['Link'], href="https://www.kaggle.com/code/jhossain/explore-the-gapminder-dataset-with-plotly-express", className="cit")],
                        className='citacao'),
                ], className='text', id='txt1'),
            dcc.Graph(figure=fig, className='graph'),
        ], className='first-box', id="first-box"),

        html.Div([
            html.Div(
                dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df.columns],
                    style_cell_conditional=[{
                        'if': {'column_id': c},
                        'textAlign': 'left'
                        } for c in ['Date', 'Region']],
                        style_data={
                            'color': 'black',
                            'backgroundColor': 'white'},
                            style_data_conditional=[{
                                'if': {'row_index': 'odd'},
                                'backgroundColor': 'rgb(220, 220, 220)',}],
                                style_header={
                                    'backgroundColor': 'rgb(210, 210, 210)',
                                    'color': 'black',
                                    'fontWeight': 'bold'}), className="table"),
            html.Div([
                    html.H4(['Lorem Ipsum'], className='subtitle', id="sub2"),
                    html.P(['   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget libero euismod, consequat sapien ut faucibus tellus.',
                    'Cras placerat ligula sit amet erat maximus, vitae tristique massa pulvinar. Mauris faucibus, libero',
                    'eu faucibus ultrices, sapien purus volutpat diam, eget fringilla libero orci id nibh. Sed ut vestibulum ipsum. Nulla',
                    'lorem neque, efficitur varius libero eu, imperdiet mattis metus. Quisque accumsan egestas risus a condimentum. Nullam',
                    'commodo blandit est sed elementum. Sed non ex ut massa gravida semper sed ut sapien. In hac habitasse platea dictumst.']),
                    html.Div([
                        html.H5(['Fonte: Plotly'], className="cit"),
                        html.A(['Link'], href="https://raw.githubusercontent.com/plotly/datasets/master/solar.csv", className="cit")],
                        className='citacao'),
                ],className='text', id='txt2'),
        ], className='second-box', id='second-box'),

        html.Div([
            html.H4(['Powered by:']),
            html.A(href='https://www.ifsc.edu.br/web/campus-florianopolis/pecce', children=[
                html.Img(src=app.get_asset_url('logo.png'), alt='PECCE', className='image')], className='logo'),
            html.A(['contato'], className='link'),
            html.Button('Baixar em PDF', id='run', className='btn')
            ], className='footer')

        ], className='outter-box-style', id='outter-box')

if __name__ == '__main__':
    app.run_server(debug=True)