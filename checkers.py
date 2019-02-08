from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<x>/<y>")
def render(x,y):

    return render_template("checkers.html", x = int(x), y = int(y))


@app.route("/<x>/<y>/<color1>/<color2>")
def render_color(x, y, color1,color2):

    return render_template("checkers.html", x=int(x), y=int(y),color1=color1,color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
