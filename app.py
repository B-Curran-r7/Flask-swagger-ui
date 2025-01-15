from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    print("Request received.")
    if request.headers.get('Authorization') == 'Bearer testSecretValue':
        response = make_response(render_template('index.html'))
        return response, 200
    return "Unauthorized", 401

if __name__ == '__main__':
    app.run()