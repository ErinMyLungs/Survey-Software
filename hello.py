from flask import Flask, render_template, request, redirect, url_for, session
import PSQLFunc as p
import pyFunc as py

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('Question1React.html')


@app.route('/question2', methods=['GET', 'POST'])
def question2():
    return render_template('Question2.html')
#TODO Delete once questions are in React and redirect is removed


@app.route('/question3', methods=['GET', 'POST'])
def question3():
    return render_template('Question3.html')
#TODO delete once redirect is removed and React fully setup


class DataWork:
    #TODO delete user_ID Print statements
    user_id = None

    @app.route('/posttest', methods=['GET', 'POST'])
    def post_Test():
        identifier = str(request.get_json()['identifier'])
        DataWork.user_id = py.find_userID(identifier)
        print(str(DataWork.user_id) + ' returned')
        return 'ok'

    @app.route('/updatedata', methods=['GET', 'POST'])
    def update_Data():
        identifier = str(request.get_json()['identifier'])
        user_id = DataWork.user_id
        print(str(user_id) + "is /updateData USERID")
        p.update_data(user_id, identifier, request.get_json()[identifier])
        return 'ok'
