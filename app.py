from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/football"> Football </a></li>
        </ul>
    '''


@app.route('/football', methods=['GET', 'POST'])
def ftball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_ftball_seasons(sortby, sortorder)
    else:
        seasons = model.get_ftball_seasons()

    return render_template("games.html", seasons=seasons)



if __name__ == '__main__':
    model.init_ftball()
    app.run(debug=True)
