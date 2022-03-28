from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
  parametri = ["IQ","Augums","Kājas izmērs"]
  images = ["https://cdn.santa.lv/media/2019/02/17/large/df097bea7673.jpg","https://rimibaltic-web-res.cloudinary.com/image/upload/f_auto,q_auto/v1/web-cms/831180b859f0ef9850f8669356fd50461b3e5f8f.jpg","https://cdn.santa.lv/media/2019/03/9/large/d3c3bfca15d6.jpg"]
  return render_template("test.html",parametri=parametri,images=images)

    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
