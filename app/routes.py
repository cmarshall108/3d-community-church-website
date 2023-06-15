import os

from flask import render_template, redirect, url_for, flash, request

from . import app


@app.route('/')
@app.route('/index')
def render_index_page():
    return render_template('index.html', is_index=True)
