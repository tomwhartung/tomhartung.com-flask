""" Ye olde hello world sanity check, using only the base template.

Purpose: ensure we can process the request to render a simple template
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
    Chapter 3 of the "Flask Web Development" book (M.Grinberg 2014)
Usage:
    bin/hello-run.sh
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    """ Say "hello" by rendering the hello.html template """
    return render_template('hello.html')


@app.route('/v')
def versions():
    """ Show the versions.html template to see what versions we are using """

    import platform
    python_version = platform.python_version()
    import flask
    flask_version = flask.__version__

    template_name = 'versions.html'
    return render_template(
        template_name,
        python_version=python_version,
        flask_version=flask_version
    )


@app.errorhandler(404)
def page_not_found(e):

    """
    Handle 404 errors by showing the 404.html template
    Found this code here:
        http://flask.pocoo.org/docs/0.12/patterns/errorpages/
    """

    return render_template('404.html'), 404


# =============================================================================

#
# Run the app!
#
if __name__ == '__main__':
    app.run(debug=True)
