from model import glove_model
from flask import Flask, render_template, request

app = Flask(__name__)

above = ["brow", "mist", "shape", "layer", "crag", "stone", "forest", "height", "fog", "mountain", "bird", "moon", "sun", "god"]

below = ["flow", "basin", "shape", "vein", "rippling", "stone", "cove", "rock", "ocean", "stream", "river", "ground", "dirt", "child", "dog", "dung", "kitten"]

trans = ["command", "pace", "roam", "trail", "frame", "sweep", "exercise", "range", "run", "chase", "exert", "control", "jump", "fight", "dance", "swing", "swim"]

intrans = ["linger", "dwell", "rest", "relax", "hold", "dream", "hum", "ponder", "think", "imagine", "sing", "stand"]

imper = ["track", "shade", "translate", "stamp", "progress", "direct", "run", "enter", "exit"]

texture = ["rough", "fine", "soft", "hard", "smooth", "rugged", "sharp", "dull", "wet", "dry"]

adjs = ["sinuous", "straight", "objective", "arched", "cool", "clear", "dim", "driven", "pretty", "ugly", "young", "old", "boiling", "salty", "tight", "shaky", "noisy", "loud", "blue", "crimson", "massive", "vast", "deep", "irregular", "speedy", "substantial"]


word = None

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('taroko_index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():

    if request.method == "POST":
        word = request.form['keyword']
    
    print("result page", word)


    def compare_similarity(w):

        return glove_model.similarity(word, w)

    above.sort(key=lambda w: compare_similarity(w), reverse=True)
    below.sort(key=lambda w: compare_similarity(w), reverse=True)
    trans.sort(key=lambda w: compare_similarity(w), reverse=True)
    intrans.sort(key=lambda w: compare_similarity(w), reverse=True)
    imper.sort(key=lambda w: compare_similarity(w), reverse=True)
    texture.sort(key=lambda w: compare_similarity(w), reverse=True)
    adjs.sort(key=lambda w: compare_similarity(w), reverse=True)

    return render_template("taroko_poem.html", above=above, below=below, trans=trans, intrans=intrans, imper=imper, texture=texture, adjs=adjs)


if __name__ == '__main__':
   app.run()
