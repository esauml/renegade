from flask import render_template

def status_401(error):
    return render_template('404.html')

def status_404(error):
    return render_template('404.html')