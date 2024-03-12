from flask import Flask, request, render_template
import sys, random

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == 'POST':
        print(request)
        data =  request.form["inputTexto"]
        return render_template("index.html", distext=dyslexicate(data))
    return render_template("index.html", title="Jinja and Flask")


def dyslexicate(text):
    result = ''
    for word in text.split():
        result += dyslexicate_word(word,['-f3'])+' '
    return result                

def dyslexicate_word(word, opts):
    size = len(word)
    if size == 2 and '-f2' in opts:
        return word[::-1]
    if size == 3 and '-f3' in opts:
        return word[0]+word[1:][::-1]
    
    inside_orig = word[1:len(word)-1]
    if size == 4 and '-f4' in opts:
        return word.replace(inside_orig,inside_orig[::-1])
    
    l = list(inside_orig)
    random.shuffle(l)
    inside_dyslexed = ''.join(l)
    return word.replace(inside_orig,inside_dyslexed )

