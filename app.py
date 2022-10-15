from flask import Flask, render_template
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'

# If you would like to protect you entire site with basic access authentication,
# just set BASIC_AUTH_FORCE configuration variable to True:

# app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

@app.route('/passwordProtectedPage')
@basic_auth.required
def secret_view():
    return render_template('mypage.html')


