import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                         "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                 "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                 "https://codepen.io/arvindreddy47/pen/ZEGvbeN.css",
                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                 "https://codepen.io/dmcomfort/pen/JzdzEZ.css"]
ex= ["body.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets )
server = app.server
app.config.suppress_callback_exceptions = True

import dash_html_components as html
import dash_core_components as dcc
import dash_table

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://desertinsurancesolutions.com/wp-content/uploads/2019/05/Chubb-Logo-Vector-Free-Download-800x400.jpg', height='60', width='141')
        ], className="ten columns padded"),

        # html.Div([
        #     dcc.Link('Full View   ', href='/cc-travel-report/full-view')
        # ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Bureau Reporting')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Reconciliation', href='/Reconciliation/', className="tab first"),

        dcc.Link('Testing', href='/Test_scripts/', className="tab"),

        dcc.Link('Statistical Analysis', href='/cc-travel-report/paid-search/', className="tab"),

        dcc.Link('Report Generation', href='/cc-travel-report/display/', className="tab"),

        dcc.Link('Publishing   ', href='/cc-travel-report/publishing/', className="tab"),

        dcc.Link('Netezza Console', href='/Netezza_Console', className="tab"),

    ], className="row ")
    return menu



layout_ga_category =  html.Div([
    html.Div([
        # CC Header
        Header(), html.Br(),html.Br(),
        html.Div([ 
    html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select File'), ' to run test Scripts'
        ]),
        style={
            'width': '60%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True,className = 'four columns'
    ),
    html.Div([
        dcc.Dropdown(
                                id = 'reports1',
                                options=[{'label':'CAAS','value':'CAAS'},
                                         {'label':'ISO_HOME','value':'ISO_HOME'},
                                        {'label':'ISO_MISC','value':'ISO_MISC'}],
                                value = None
                        ),
    ], className = 'two columns',
    style={
            'width': '30%',
            'height': '40px',
            'lineHeight': '40px',
            'borderWidth': '1px',
            'borderRadius': '4px',
            'textAlign': 'center',
            'margin-top' : '6px'
        }
    )],className = 'row'),
    
    html.Div(id='output-data-upload'), html.Br(),html.Br(),
    html.Div([
    html.H3(children='Test Results'),
        
    html.Div([
 
 html.Div([dcc.Graph(id = 'Test_analysis')],className='five columns',style={'margin-top': '10','bgcolor':'#FFF'}),

#     html.Div([dash_table.DataTable(
#         id='datatable-interactivity1',
# #         filter_action="native",
#         sort_action="native",
#         sort_mode="multi",
# #         column_selectable="single",
# #         row_selectable="single",
#         row_deletable=False,
#         selected_columns=[],
#         selected_rows=[],
#         page_action="native",
# #         virtualization=True,
#         page_current= 0,
#         page_size= 27,
#         style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
#                 css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
#                 style_cell_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#FBDFE1'}]  
#                       + [{'if': {'column_id': c}, 'backgroundColor': '#BEA9A4'} for c in ['Spend TY', 'Spend - LP', 'Spend PoP (Abs)', 'Spend PoP (%)', 'Spend LY', 'Spend YoY (%)',]] 
#         )],className='six columns',style={'margin-left':'3'}),
       
		
		],className='row'),
         html.Div([
        html.Pre(id='click-data1')])
]),
    dcc.Link(html.Button('Back to Menu' ,id = 'Bk_button' ), href='/')
])
        
        ], className="subpage")
    ], className="page")
# see https://dash.plot.ly/external-resources to alter header, footer and favicon
app.index_string = ''' 
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Bureau Reporting</title>
        {%css%}
        {%renderer%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>Accenture copyright</div>
    </body>
</html>
'''
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
# # # # # # # # #
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Reconciliation/' or pathname == '/Reconciliation/' or pathname == '/':
        return layout_ga_category
    elif pathname == '/Test_scripts/':
        return layout_ga_category
    elif pathname == '/Stat_Analysis/':
        return 'no'
    elif pathname == '/cc-travel-report/display/':
        return 'nooo'
    elif pathname == '/Admin/':
        return 'yes'
    elif pathname == '/Netezza_Console':
        return 'nope'
    elif pathname == '/table':
        return 'yup'
        
    else:
        return noPage

if __name__ == '__main__':
    app.run_server(debug=False)

