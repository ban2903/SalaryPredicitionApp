from flask import Flask, render_template, request
from salary_prediction import SalaryPrediciton


app = Flask(__name__)
model = SalaryPrediciton()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # url = request.form.get('url')
        url = request.form['url']
        score = model.predict(url)[0][0]
        return score
    else:
        return render_template('form.html')
    
if __name__ == '__main__':
    app.run()