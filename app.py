from flask import Flask, request, redirect
from flask import render_template
import logics

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
#@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        size = request.form['size']
        logics.GameOfLife(int(size),int(size))
        return redirect('/live')
    else:
        logics.GameOfLife(25,25)
    return render_template('index.html')

@app.route('/live')
def live():
    x = logics.GameOfLife()
    if x.counter > 0:
        x.form_new_generation()
    x.counter += 1
    return render_template('live.html', world = x, world_old =x.old_world)

if __name__ == '__main__':
    app.run(debug=True)