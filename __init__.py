from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
    title = 'Data Science'
    paragraph = ['This is my data science blog', 'Zero to Hero in Data Science']
    return render_template('index.html', title=title,
                           paragraph=paragraph)


@app.route('/about')
def aboutpage():

    title = "About this website"
    paragraph = ['blahhhhhh']
    pageType = 'about'
    return render_template('index.html', title=title,
                    paragraph=paragraph, pageType=pageType)


if __name__ == "__main__":
    app.run()

