from flask import Flask, render_template
import requests
from datetime import date
import data

app = Flask(__name__)

hari_ini = date.today().strftime('%d-%m-%Y')
dt_indo1 = data.indo1()
dt_prov = data.prov()
harian = data.data_harian()
detail = data.detail()


@app.route("/")
def index():
    labels = []
    for i in harian:
        labels.append(i['tanggal'][:10])

    values = []
    for x in harian:
        values.append(x['positif_kumulatif'])
    
    start_at = values[0]
    
    det_value = []
    for item in detail:
        det_value.append(item['doc_count'])
    return render_template("index.html", dt=dt_indo1, 
        dt_sulteng=dt_prov, hari_ini=hari_ini, labels=labels, 
        values=values, max=300000, start_at=start_at, det_value=det_value )

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
