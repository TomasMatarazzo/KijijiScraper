from flask import Flask,render_template, request
from flaskwebgui import FlaskUI
import pathlib
from engine.const import states_id, city_id , province_dict, city_dict
from engine.Scraping import Scraping

scrape = Scraping()

print(str(pathlib.Path(__file__).parent.parent.absolute()) + '\index.html')
app = Flask(__name__ , template_folder='GUI/frontend', static_folder='GUI/static')
ui = FlaskUI(app, width= 695)

@app.route('/')
def function():
    print('hi')
    return render_template('index.html')


@app.route('/scraping')
def scraping():
    args = request.args
    arg1 = request.args.get("location")
    arg2 = request.args.get("type")
    arg1 = int(arg1)
    arg2 = int(arg2)

    #We convert the id to the positions in the websites.
    arg1 = states_id[arg1]
    arg2 = city_id[arg1][arg2]
    print(arg1,'---')

    state_name = province_dict[arg1]
    city_name = city_dict[arg1][arg2]
    print(city_name)


    if (arg1 == 7 and arg2 >= 18):
        arg1 = 8
        if (arg2 == 18):
            arg2 = 4
        else:
            arg2 = 14
    info = scrape.FindPage(arg1, arg2 , state_name, city_name)
    if info:
        scrape.createExcel(info)
    return "nothing"

ui.run()

if __name__ == '__main__':
    app.run( host='127.0.0.1',debug = True)

