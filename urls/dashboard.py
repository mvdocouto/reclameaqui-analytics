from flask import Blueprint, jsonify, render_template


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def homepage():
	return render_template('dashboard.html')

