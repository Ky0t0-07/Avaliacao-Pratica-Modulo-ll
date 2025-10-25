from flask import Flask, render_template, request

app = Flask (__name__)

@app.route ('/')
def index():
    return render_template('index.html')
'''-----------------------------------------------'''
@app.route('/soma')
def soma():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))


    aa = n1 + n2 

    return{

        'Resultado da soma': aa
        
    }

'''-------------------------------------------'''

@app.route('/subtrair')
def subtrair():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))

    ab = n1 - n2 

    return{

        
        
        'Resultado da subtracao': ab
        
    }

'''-------------------------------------------'''

@app.route('/multiplicar')
def multiplicar():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))

    ac = n1 * n2 

    return{

        
        
        'Resultado da Multiplicacao': ac
        
    }

'''-------------------------------------------'''

@app.route('/dividir')
def divicao():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    ad = n1 / n2 

    return{
        
        
    'Resultado da Divicao': ad
        
        }

if __name__ == '__main__':
    app.run(debug=True)
