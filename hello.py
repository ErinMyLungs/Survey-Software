from flask import Flask, render_template, request, redirect, url_for
import PSQLFunc as p

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('Question1React.html')


@app.route('/nextpage', methods=['GET'])
def next_Page():
    return redirect(url_for('question2'))


@app.route('/posttest', methods=['GET', 'POST'])
def post_Test():
    identifier = str(request.get_json()['identifier'])
    user_id = p.insert_data(identifier, request.get_json()[identifier])
    print(str(user_id) + ' returned')
    return user_id


@app.route('/updatedata', methods=['GET', 'POST'])
def update_Data():
    identifier = str(request.get_json()['identifier'])
    user_id = request.get_json()['userID']
    p.update_data(user_id, identifier, request.get_json()[identifier])
    return 'ok'


@app.route('/question2', methods=['GET', 'POST'])
def question2():
    return render_template('Question2.html')


@app.route('/question3', methods=['GET', 'POST'])
def question():
    return render_template('Question3.html')
