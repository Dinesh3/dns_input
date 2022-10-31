import sqlite3
from db_con import create_dns_request
from flask import Flask, render_template, request
@app.route('/srv')
def srv():
    return render_template("srv.html")