from flask import Flask, render_template, request, url_for, redirect

flashcard = {}
fruits = [1, 2, 3]
data=[
    {
        'name':'Audrin',
        'place': 'kaka',
        'mob': '7736'
    },
    {
        'name': 'Stuvard',
        'place': 'Goa',
        'mob' : '546464'
    }
]
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/testfeature')
def testfeature():
    global fruits 
    hiii = "whhh"
    return render_template('testfeature.html', data=data)
@app.route('/flashCards', methods=['GET', 'POST'])
def flashCards():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('flashCards.html')
@app.route('/flashCard', methods = ['GET', 'POST'])
def extract():
    if request.method == 'POST':
        word = request.form.get("gname")
        meaning = request.form.get("fname")
        flashcard[word] = meaning
        return render_template('flashCards.html')
    elif request.method == 'GET': 
        return render_template('testfeature.html')


if __name__ == "__main__":
    app.run(debug = True)

