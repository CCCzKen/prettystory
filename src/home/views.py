# coding: utf-8
from flask import render_template, Blueprint, request
from flask import url_for, redirect

bp = Blueprint('home', __name__)


@bp.route('')
def index():
	return render_template('index.html')