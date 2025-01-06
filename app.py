from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Site Density Analysis in Minneapolis and Minnesota",
        # "thumb": "img/.png",
        # "hero": "img/.png",
        "categories": ["Python", "PySpark"],
        # "slug": "",
        # "prod": "",
    },
    {
        "name": "Material Work Order Tag Generator",
        # "thumb": "img/.png",
        # "hero": "img/.png",
        "categories": ["Flask", "Python", "Gunicorn", "Podman", "HTML", "CSS"],
        "slug": "web-application",
    },
    {
        "name": "Data pipeline development and analysis for kiwifruit drop in Italy ",
        "thumb": "img/kiwifruit.png",
        "hero": "img/kiwifruit.png",
        "categories": ["Python", "PySpark"],
        "slug": "api-docs",
    },
]

@app.route('/')
def home():  # put application's code here
    return render_template('home.html', projects = projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
