from flask import Flask, request, render_template
import dotenv,os

dotenv.load_dotenv(dotenv.find_dotenv())

app = Flask(__name__)
app.debug = True

@app.route("/",methods=['GET'])
def index():
    return render_template('index.html')

app.run(port=os.getenv("PORT") or 80)