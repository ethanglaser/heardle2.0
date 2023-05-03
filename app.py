from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form['message']
        # do something with message
        return render_template('contact.html', message_sent=True)
    else:
        return render_template('contact.html', message_sent=False)

if __name__ == '__main__':
    app.run(debug=True)
