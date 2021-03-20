import os
import logging

from flask import Flask
from flask import render_template
from flask import request
from flaskr import evaluation_actions as eval_action

def create_app(test_config=None):
    global logger
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)   

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'cta_evaluation.db'),
    )
    app.logger.setLevel(logging.DEBUG)
    logger = app.logger
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/evaluation', methods=['GET'])
    def show_evaluation_form():
        return render_template('eval_form.html')

    @app.route("/evaluation/submit", methods=['POST'])
    def submit_evaluation_form():
        ev_Rec,message = eval_action.submit_eval_form(request,'cta_evaluation.db')
        page = "eval_recommendation.html"
        if message != "Success" :
            page="eval_error.html"
        elif not ev_Rec.skills:
            page = "no_eval.html"
        return render_template(page, evRec=ev_Rec,message=message)

    @app.route("/recommendation/save", methods=['POST'])
    def submit_evaluation_recommendation():
        eval_rec = eval_action.submit_eval_rec(request, 'cta_evaluation.db')
        return render_template('eval_confirmation.html', evRec=eval_rec)

    return app
