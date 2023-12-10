from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/t', methods=['POST', 'GET'])
def t():
    if request.method == 'POST':
        answer = request.form.get('name')
        print(answer)
        return 'POST t-text' + str(answer)
    else:
        return 'GET t-text'

@app.route('/departed_clients')
def departed_clients():
    return render_template('departed_clients.html')

        

if __name__ == '__main__':
    app.run(debug=True)