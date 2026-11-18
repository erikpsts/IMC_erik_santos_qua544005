from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # O .replace() deve vir ANTES do float() para tratar vírgulas como ponto decimal
            massa = request.form.get('massa', '').replace(',', '.')
            altura = request.form.get('altura', '').replace(',', '.')
            
            if massa and altura:
                massa = float(massa)
                altura = float(altura)
                
                if altura > 0:
                    imc = massa / (altura ** 2)
                    
                    if imc < 18.5:
                        diagnostico = 'Você está abaixo do peso.'
                    elif imc < 25:
                        diagnostico = 'Você está no peso ideal.'
                    elif imc < 30:
                        diagnostico = 'Você está com sobrepeso.'
                    elif imc < 35:
                        diagnostico = 'Você está com obesidade grau I.'
                    elif imc < 40:
                        diagnostico = 'Você está com obesidade grau II.'
                    else:
                        diagnostico = 'Você está com obesidade mórbida (grau III).'
                        
                    result = f"Seu IMC é {imc:.2f}.\n{diagnostico}"
                else:
                    result = "A altura deve ser maior que zero."
            else:
                result = "Por favor, preencha todos os campos."
                
        except ValueError:
            result = "Por favor, insira apenas números válidos."
            
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)