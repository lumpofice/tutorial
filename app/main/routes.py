from flask import redirect, render_template, url_for, request
from app.main import bp
import subprocess


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    my_cmd = ['app/templates/index']
    with open('app/templates/index.html', 'w') as outfile:
        subprocess.run(my_cmd, stdout=outfile)
    return render_template('index.html', title='Tutorials')

