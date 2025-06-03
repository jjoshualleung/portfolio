from flask import Flask, render_template
from flask import abort

app = Flask(__name__)

projects = [
    {
        "name": "Data pipeline development and analysis for kiwifruit drop in Italy",
        "thumb": "img/kiwifruit.png",
        "hero": "img/kiwifruit.png",
        "categories": ["Python", "PySpark"],
        "slug": "data-pipeline-development",
        "prod": "https://gitlab.com/jjoshualleung/kiwifruit-analysis"
    },
    {
        "name": "Material Work Order Tag Generator",
        "thumb": "img/material_tag_web.jpg",
        "hero": "img/material_tag_web.jpg",
        "categories": ["Python", "Flask"],
        "slug": "material-wo-generator-web-application",
        "prod": "https://gitlab.com/jjoshualleung/document-converter-platform"
    },
    {
        "name": "Site Density Analysis in Minneapolis and Minnesota",
        "thumb": "img/minneapolis_atat.png",
        "hero": "img/minneapolis_atat.png",
        "categories": ["Python", "PySpark"],
        "slug": "site-density-analysis",
    },
    {
        "name": "adjusttxt – Line‑Based Text Transformation",
        "thumb": "img/tsl.jpg",
        "hero": "img/tsl.jpg",
        "categories": ["Java", "TSL"],
        "slug": "adjusttxt-text-transformation",
        "prod": "https://gitlab.com/jjoshualleung/adjusttxt"
    },
    {
        "name": "Autonomous Spaceship Asteroid-Hopping Navigation",
        "thumb": "img/spaceship.png",
        # "hero": "img/spaceship.png",
        "categories": ["Python", "Robotics"],
        "slug": "autonomous-spaceship-navigation",
        # "prod": "https://gitlab.com/jjoshualleung/adjusttxt"
    }

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

slug_to_projects = {project["slug"]:project for project in projects}
@app.route('/projects/<string:slug>')
def project(slug):
    if slug not in slug_to_projects:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_projects[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run()
