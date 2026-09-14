from process import preparation, generate_response
from flask import Flask, render_template, request

# download nltk
preparation()

#Start Chatbot
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",data=home,data2=aboutus,data3=gambar,data4=hotissue,data5=information,data6=vid,data7=home2)

@app.route("/index.html")
def home2():
    return render_template("index.html",data=home,data2=aboutus,data3=gambar,data4=hotissue,data5=information,data7=home2)

@app.route("/aboutus.html")
def aboutus():
    return render_template("aboutus.html",data=home,data2=aboutus,data3=gambar,data4=hotissue,data5=information,data6=vid,data7=home2)

@app.route("/gambar.html")
def gambar():
    return render_template("aboutus.html",data=home,data2=aboutus,data3=gambar,data4=hotissue,data5=information,data6=vid,data7=home2)

@app.route("/hotissue.html")
def hotissue():
    return render_template("aboutus.html",data=home,data2=aboutus,data3=gambar,data4=hotissue,data5=information,data6=vid,data7=home2)

@app.route("/information.html")
def information():
    return render_template("aboutus.html",data=home,data2=aboutus,data3=gambar,data4=hotissue,data5=information,data6=vid,data7=home2)

@app.route("/vid.html")
def vid():
    return render_template("aboutus.html",data=home,data2=aboutus,data3=gambar,data4=hotissue,data5=information,data6=vid,data7=home2)

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)