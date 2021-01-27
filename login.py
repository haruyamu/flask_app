from flask import Flask, request, session, redirect
app = Flask(__name__)
app.secret_key = 'aaaaaaaaaaaaaaaaa'

USERLIST = {
    'taro': "aaa",
    'jiro': "bbb",
    'sabu': "ccc",
}


@app.route('/')
def index():
    return """
    <html>
      <body>
        <h1>login</h1>
        <form action="/check_login" method="post">username: <br>
            <input type="text" name="user">
        </form>
        <p><a href="/private">private page</a></p>
         """


@app.route("/check_login", methods={"POST"})
def check_login():
    user, pw = (None, None)
    if 'user' in request.form:
        user = request.form['user']
    if 'pw' in request.form:
        pw = request.form['pw']
    if (user is None) or (pw is None):
        return redirect('/')

    if try_login(user, pw) == False:
        return """
      <h1>mistake user or pw</h1>
      <p><a href="/">back</a></p>
      """
    return redirect('private')


@app.route('/private')
def private_page():
    if not is_login():
        return """
     <h1>please login</h1>
     <p><a href="/">do login</a></p>
"""
        return """
     <h1>here is private room</h1>
     <p>you are now login</p>
     <p><a href="/logout">logout</a></p>
"""


app.route('/logout')


def logout_page():
    try_logout()
    return """
  <h1>do logout</h1>
  <p>back</p>
"""


def is_login():
    if 'login' in session:
        return True
    return False


def try_login(user, password):
    if not user in USERLIST:
        return False
    if USERLIST[user] != password:
        return False
    session['login'] == user
    return True


def try_logout():
    session.pop('login, None')
    return True


if __name__ == '__main__':
    app.run(host='0.0.0.0')
