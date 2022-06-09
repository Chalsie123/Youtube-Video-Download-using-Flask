import logging
from flask import *
from pytube import YouTube

app = Flask(__name__)

fsaveloc = "C:\\Pytube videos"
list1 = []

def download_video(opt, linklist):
    try:
        ytd = YouTube(linklist[0])
        print(opt)
        yt_video = ytd.streams.get_by_itag(opt)
        try:
            print("Starting....")
            yt_video.download(fsaveloc)
            print("Done")
        except:
            logging.exception("Fffff")
            return render_template('error.html')

    except Exception as e:
        print(e)
        return render_template('error.html', e=e)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/download/", methods=["GET", "POST"])
def download():
    if request.method=="POST":
        lnk = request.form['lnk']
        list1.append(lnk)
        try:
            yt = YouTube(lnk)
        except Exception as e:
            return render_template('error.html', e=e)

        strea = yt.streams.filter(progressive=True)
        return render_template('download.html', yt=yt, strea=strea)
    return "hello"

@app.route("/result", methods=['POST'])
def result():
    if request.method=='POST':
        option = request.form['qt']
        download_video(option, list1)
        return render_template('result.html')
    
    return "HEllo"

if __name__=="__main__":
    app.run(debug=True)