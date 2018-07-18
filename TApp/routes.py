import os
from sys import stdout
from TApp import appv
from flask import render_template, request, flash, redirect, url_for
from TApp.forms import FileDetailForm
from TApp.jsonopener import get_json_file
from werkzeug.utils import secure_filename


@appv.route('/', methods=["GET", "POST"])
@appv.route('/index', methods=["GET", "POST"])
def start_page():
    form = FileDetailForm()
    return render_template('start_detail.html', form=form)


@appv.route('/table/<file_url>', methods=["POST"])
def table(file_url):
    form = request.form
    selected_file = str(form["file_"])
    tabfl = get_json_file(selected_file)
    return render_template('table.html',
                           fields=[form[x] for x in form.keys() if "field" in x],
                           arrayofdict=tabfl, title=selected_file)


def check_ext(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() == 'json'


@appv.route('/upload', methods=["GET", "POST"])
def uploader():
    if request.method == "POST":
        # try:
        file_set = request.files.getlist('file[]', None)
        # except KeyError:
        #     flash('No File Part')
        #     return redirect(url_for('start_page'))
        for file_ex in file_set:
            if file_ex and check_ext(file_ex.filename):
                sec_filename = secure_filename(file_ex.filename)
                file_ex.save(os.path.join(appv.config['UPLOAD_FOLDER'],
                                          sec_filename))
                flash('Succesfully yours: ' + sec_filename)
        return redirect(url_for('start_page'))
    return render_template('upload_page.html')
