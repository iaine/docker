'''
   Simple browser for the export file

   @author: iain emsley
'''
from flask import Flask, render_template
from browser import Browser

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Probably ought to retun a list of containers'

@app.route('/prov/<fname>')
def find_prov(fname):
    if fname is None:
        return "<p>You need to provide a name"
    b = Browser()
    datarow = b.browse(fname + "_plan.ttl", "select.rq")
    return render_template("layout.html", datarow=datarow)

@app.route('/software/<fname>/')
def find_prov_xml(fname):
    with open(fname, 'rb') as fh:
        return fh.read()
    fh.closed

@app.route('/container/<fname>')
def find_container(fname):
    if fname is None:
        return "<p>You need to provide a name"
    b = Browser()
    datarow = b.browse(fname + "_docker.ttl", "select.rq")
    return render_template("container.html", datarow=datarow, title=datarow[0][0])
