from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on Github"

@app.route('/')
@app.route('/count')
def hello_world():
    if 'sessioncounter' in session:
        session['sessioncounter'] += 1
    else:
        session['sessioncounter'] = 1
    return render_template('index.html', sessioncounter=session['sessioncounter'])



@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)

