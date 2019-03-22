##{}dicionario##
##[]lista##
import os

from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/tim-maia', methods=['POST', 'GET'])
def tim():

        
    MUSICA_E_DO_TIM = ''

    def verificar_se_musica_e_do_tim(musica):
        MUSICA_E_DO_TIM =[
            'destino',
            'telefone',
            'ela partiu',
            'lamento',
        ]
        

        if musica.lower() in MUSICA_E_DO_TIM:
            return True
        else:
            return False

    if request.method == 'POST':
            musica = request.form['nome-musica']
            if verificar_se_musica_e_do_tim(musica):
                MUSICA_E_DO_TIM = 'É do Tim Mais'
            else:
                MUSICA_E_DO_TIM = 'Num é não pô'

    return '''
        <form action="/tim-maia" method="POST">
        
            <label for="nome-musica">Nome da Musica</label>
            <input type="text" id="nome-musica" name="nome-musica">
            <button>Ver se é a musica do Tim ;D </button>
        </from>

        <p>{}</p>

    '''.format(MUSICA_E_DO_TIM)


@app.route("/")
def hello():
    return '''

    <style>
        img{
            width: 500px;
            height: 500px; 
        }

        .imagem-pequena {
                width: 250px;
                height: 250px;
        }
        .imagem-grande {
                width: 350px;
                height: 350px;
        } 

        #letreiro {
            font-size: 25px;
            color: blue;
            
        }               
    </style>

    <h1>Flask App </h1>
    <hr>
    <h2> Meu primeiro aplicativo em Flask</h2>

    <p>
     a cada dia aprendendo 
     <marquee>ESTUDANDO !!! > < </marquee>
     <img class= 'imagem-grande'/home/fabio/Imagens.png/>
     <img class= 'imagem-pequena'/home/fabio/imagem.jpg/>
    </p> 
    <p> by: <strong>Fabio Santos</strong></p>

    '''

if __name__== '__main__':
    os.environ['FLASK_APP'] = 'app'
    os.environ['FLASK_ENV'] = 'development'
    
    app.run()