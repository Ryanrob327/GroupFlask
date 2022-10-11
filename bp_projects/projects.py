from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/weeks',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/week08/')
def week08():
    return render_template("week08.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/week09/')
def week09():
    return render_template("week09.html")

@app_projects.route('/week10/')
def week10():
    return render_template("week10.html")

@app_projects.route('/week11/')
def week11():
    return render_template("week11.html")