from flask import Flask, render_template, request
from salary_prediction import SalaryPrediciton


app = Flask(__name__)
model = SalaryPrediciton()
data = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        data = model.get_features(url)
        score = model.predict(data)[0][0]
        return render_template('form.html', score=score)
    
    return render_template('form.html')

def shap():
    model.shap_plot(data)

if __name__ == '__main__':
    app.run()