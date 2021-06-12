from flask import Flask, app, render_template, jsonify
import numpy as np
app = Flask(__name__)

random_decimal = np.random.rand()


@app.route('/update_decimal', methods=['POST'])
def updatedecimal():
    random_decimal = np.random.rand()
    return jsonify('', render_template('random_decimal_model.html', x=random_decimal))


@app.route('/')
def homepage():
    return render_template('home.html', x=random_decimal)


app.run(port=random_decimal)
