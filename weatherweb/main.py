from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        continent = request.form['continent']
        return render_template(f'{continent}.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)