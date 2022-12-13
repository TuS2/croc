from flask import Flask, render_template
import requests
import schedule

app = Flask(__name__)
q = 0
a = 0
y = 0
m = 0
with open("/root/croc/num.txt", "r") as f:
    y = f.read(1)
    f.close()


def clear():
    with open("/root/croc/num.txt", "wb"):
        pass


schedule.every().day.at("09:14").do(clear)
schedule.every().day.at("10:09").do(clear)
schedule.every().day.at("11:09").do(clear)
schedule.every().day.at("12:09").do(clear)
schedule.every().day.at("13:04").do(clear)
schedule.every().day.at("13:59").do(clear)
schedule.every().day.at("14:59").do(clear)


@app.route('/')
@app.route('/1')
def first():
    global a
    a += 1
    with open("/root/croc/num.txt", "w") as f:
        f.write(str(a))
        f.close()
    return render_template('main1.html')


@app.route('/3')
def third():
    return render_template('num3.html', minute=int(a) * 0.5, queue=y)


@app.route('/4')
def fourth():
    return render_template('yourturn4.html')


@app.route('/6')
def sixth():
    return render_template('kyh.html')


@app.route('/7')
def seventh():
    return render_template('exit.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
