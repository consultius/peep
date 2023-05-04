from flask import Flask, render_template

app = Flask(__name__)

print("***BASIC BASIC BASIC***")

@app.route("/basic")
def hello():
    message = """\
    Hello,
    World!
    line3
    line4
    """
    message_lines = message.split('\n')
    print(message_lines)
    return render_template('index_basic.html', message=message_lines)

# another app route which just points to apitest.html
@app.route("/apitest")
def apitest():
    return render_template('apitest.html')


if __name__ == "__main__":
    app.run(debug=True)
