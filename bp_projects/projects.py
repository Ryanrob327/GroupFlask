from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/stocks',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/AAPL/')
def AAPL():
    return render_template("AAPL.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/GME/')
def GME():
    return render_template("GME.html")

@app_projects.route('/GOOGL/')
def GOOGL():
    return render_template("GOOGL.html")

@app_projects.route('/TSLA/')
def TSLA():
    return render_template("TSLA.html")