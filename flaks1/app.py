from flask import Flask, render_template
import pickle
import numpy as np

model = pickle.load(open('setD.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data1 = 128
    data2 = 1
    data3 = 1
    arr = np.array([[data1, data2, data3]])

    df = pd.read_csv('FixData.csv')
    df = df.drop(['status'], axis=1)

    dataf = df.values
    dataf = sc.fit_transform(dataf)

    pred = model.predict(dataf)
    return render_template(pred)


if __name__ == '__main__':
    app.run(debug=True)
