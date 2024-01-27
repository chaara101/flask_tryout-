from flask import flask

app=flask(__name__)

@app.route('/prijzen') 
def prijzen():
    return "<p>Hello world!</p>"

@app.route('/recepten')
def recepten():
    return "basic flask code"
    return "<p> hello flask<p>"

if __name__ == '__main__':
    app.run(debug=True)
