from TApp import appv
from flask import render_template, request, redirect
from TApp.jsonopener import get_json_file, FIELDS


@appv.route('/', methods=["GET", "POST"])
@appv.route('/index', methods=["GET", "POST"])
def start_page():
    if request.method == "POST":
        return redirect('/table')
    return render_template('start_only.html')


@appv.route('/table')
def table_page():
    jsonfile = get_json_file()
    return render_template('table.html', fields=FIELDS, arrayofdict=jsonfile)
