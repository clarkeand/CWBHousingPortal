"""Server for the CWB Housing Portal"""

from flask import (Flask, render_template, request, flash, session,redirect,)

app = Flask(__name__, static_folder='static')

@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/rental_rates')
def rental_rates():
    """View Rental Rates."""
    return render_template('rental_rates.html')

@app.route('/pictures')
def pictures():
    """View pictures/floorplan."""
    return render_template('pictures.html')

@app.route('/amenities')
def amenities():
    """View amenities."""
    return render_template('amenities.html')

@app.route('/calendar')
def calendar():
    """View calendar."""
    return render_template('calendar.html')

@app.route('/contact_info')
def contact_info():
    """View contact information."""
    return render_template('contact_info.html')

@app.route('/openings')
def openings():
    """View openings."""
    return render_template('openings.html')

@app.route('/forms')
def forms():
    """View forms."""
    return render_template('forms.html')

@app.route('/sp_sm_contracts')
def sp_sm_contracts():
    """View spring summer forms/contracts."""
    return render_template('sp_sm_contracts.html')

@app.route('/fl_w_contracts')
def fl_w_contracts():
    """View fall and winter forms/contracts."""
    return render_template('fl_w_contracts.html')

if __name__ == "__main__": 
    app.run()