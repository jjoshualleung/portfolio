from flask import Flask, render_template
from flask import abort

app = Flask(__name__)

projects = [
    {
        "name": "Site Density Analysis in Minneapolis and Minnesota",
        "thumb": "img/minneapolis_atat.png",
        "hero": "img/minneapolis_atat.png",
        "categories": ["Python", "PySpark"],
        "slug": "geospatial-analysis",
        # "prod": "",
    },
    {
        "name": "Material Work Order Tag Generator",
        "thumb": "img/material_tag_web.jpg",
        "hero": "img/material_tag_web.jpg",
        "categories": ["Flask", "Python"],
        "slug": "web-application",
    },
    {
        "name": "Data pipeline development and analysis for kiwifruit drop in Italy",
        "thumb": "img/kiwifruit.png",
        "hero": "img/kiwifruit.png",
        "categories": ["Python", "PySpark"],
        "slug": "data-pipeline-development",
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

slug_to_projects = {project["slug"] for project in projects}
@app.route('/projects/<string:slug>')
def projects(slug):
    if slug not in slug_to_projects:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_projects[slug])

if __name__ == '__main__':
    app.run()
