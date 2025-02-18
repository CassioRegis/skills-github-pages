import dash
from dash import dcc, html
from dash.dependencies import input, Output
import plotly.graph_objs as go

dados_conceitos = { #dicionário com as informações da caixa dropdown}
    'java' : {'variaveis':8, 'condicionais' :10, 'loops':4, 'poo':3,'funcoes':4},
              'python':{'variaveis':9, 'condicionais':7, 'loops':8, 'poo':4,'funcoes':5},
              'sql':{'variaveis':7, 'condicionais':10, 'loops':9, 'poo':4,'funções':4},
                'golang':{'variaveis':10, 'condicionais':5, 'loops':8, 'poo':3,
                     'funções':3},
                'javascript':{'variaveis':8, 'condicionais':57, 'loops':4, 'poo':3,
                     'funções':8}
}

cores_map=dict(
    java='red', 
    python='green',
    sql='yellow',
    golang='blue',
    javascript='pink'
)
app = dash.Dash(_nome_)

app.layout - html.Div({html.H4('Sebrae MA', style={'textAlign':'center'}),
                       html.div(dcc.dropdown(
                                    id="dropdown_Linguagens",
                                    options=[
                                        {'label':'Java','value':'java'},
                                        {'label':'Python','value':'python'},
                                        {'label':'SQL','value':'sql'},
                                        {'label':'Golang','value':'golang'},
                                        {'label':'JavaScript','value':'javascript'},
                                    ],
                                    value=['java'],
                                    multi=True,
                                    style={width:'50%','margin':'0 auto'}
                       )
                       ),
                       dcc.Graph(id='grafico_linguagens')
                     }, style={'width':'80%', 'margin':'0 auto'}
                     )
        
@app.callback(#uma função que vai ser chamada atraves de um evento
        Output('grafico_linguagem','figura'),
        [input('dropdown_linguagens','value')]
)

def scarter_linguagens (linguagens_selecionadas):
        scarter_trace=[]
        for linguagem in linguagens_selecionadas:
                dados_linguagem = dados_conceitos[linguagem]
                for conceito, conhecimento in dados_linguagem.items():
                        scarter_trace.append(
                                go.scatter(
                                x = [Conceito],
                                y = [conhecimento],
                                mode = 'markers',
                                nome=linguagem.title()
                                marker={'size':15,'color':cores_map
                                        [linguagem]},
                                        showlegend=False
                                    
                        )
                        scartter_layout = go.layout(
                            title='Meus conhecimentos em Linguagens'
                            xavis=dict(title='Conceitos',showgrid=false)
                            yaxis=dict(title='Nivel de Conhecimento', showgrid=False)
                        )
                        
                        return{'data':  scarter_trace,'layout':scarter_layout}
                        
                        if __name__ == '__main__':
                            app.run_server(debug=True)