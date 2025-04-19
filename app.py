import os
from flask import Flask, render_template, request, redirect, url_for, flash
from keybert import KeyBERT
from transformers import pipeline
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from urllib.parse import quote_plus
from flask import redirect


load_dotenv()  # reads .env for your API keys

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "supersecret")
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ---- Initialize models once ----
kw_model = KeyBERT('all-MiniLM-L6-v2')
img_classifier = pipeline("image-classification")

# ---- Helper functions ----
def extract_text_tags(text, top_n=5):
    kw = kw_model.extract_keywords(text,
        keyphrase_ngram_range=(1,2),
        stop_words='english',
        top_n=top_n)
    return [f"#{w.replace(' ', '')}" for w,score in kw]

def extract_image_tags(image_path, top_k=5):
    preds = img_classifier(image_path, top_k=top_k)
    tags = [p['label'].replace('_', '') for p in preds]
    return [f"#{t}" for t in tags]

def combine_tags(text, image_path):
    tags = []
    if text:
        tags += extract_text_tags(text)
    if image_path:
        tags += extract_image_tags(image_path)
    # dedupe and limit
    seen = set()
    out = []
    for t in tags:
        if t.lower() not in seen:
            seen.add(t.lower())
            out.append(t)
        if len(out) >= 5:
            break
    return out

def post_to_twitter(text, image_path, tags):
    # combine text + tags into one string
    full = text + "\n" + " ".join(tags)
    # URL‑encode and build Twitter “intent” link
    tweet_url = "https://twitter.com/intent/tweet?text=" + quote_plus(full)
    # send the user off to Twitter’s site to finish the post
    return redirect(tweet_url)

def post_to_linkedin(text, image_path, tags):
    full = text + "\n" + " ".join(tags)
    # Our app URL (LinkedIn displays it as the “shared” link)
    share_url = "http://localhost:5000"
    params = {
        "mini":     "true",
        "url":      quote_plus(share_url),
        "title":    quote_plus("Check this out!"),
        "summary":  quote_plus(full)
    }
    query = "&".join(f"{k}={v}" for k, v in params.items())
    linkedin_url = "https://www.linkedin.com/shareArticle?" + query
    return redirect(linkedin_url)


# ---- Routes ----
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text') or ""
    file = request.files.get('image')
    img_path = None
    if file and file.filename:
        fn = secure_filename(file.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], fn)
        file.save(img_path)

    tags = combine_tags(text, img_path)
    return render_template('analyze.html',
                           text=text, img_path=img_path,
                           tags=tags)

@app.route('/post', methods=['POST'])
def post():
    # platform = request.form['platform']
    # text = request.form['text']
    # img_path = request.form.get('img_path') or None
    # tags = request.form.getlist('tags')

    # success = False
    # if platform == 'twitter':
    #     success = post_to_twitter(text, img_path, tags)
    # else:
    #     success = post_to_linkedin(text, img_path, tags)

    # if success:
    #     flash(f"Posted to {platform.title()}!")
    #     return redirect(url_for('index'))
    # else:
    #     flash("Error posting. Check logs.", "error")
    #     return redirect(url_for('index'))
        text     = request.form['text']
        image    = request.form.get('img_path')  # still there if you want it
        tags     = request.form.getlist('tags')
        platform = request.form['platform']

        if platform == 'twitter':
            return post_to_twitter(text, image, tags)
        else:
            return post_to_linkedin(text, image, tags)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
