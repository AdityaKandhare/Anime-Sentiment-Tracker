from flask import Flask, render_template, send_file, request

from graph_scripts.politics_analysis import generate_politics_graph_by_date

from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


# Landing page route
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Routes to serve individual graphs

@app.route('/graph/myanimelist')
def myanimelist_graphs():
    return render_template('platform_graphs.html', platform="myanimelist")

@app.route('/graph/myanimelist/heatmap')
def myanimelist_heatmap():
    from graph_scripts.myanime_analysis import generate_myanime_graphs
    img1, _ = generate_myanime_graphs()
    return send_file(img1, mimetype='image/png') if img1 else "Error generating heatmap", 500

@app.route('/graph/myanimelist/favorites')
def myanimelist_favorites():
    from graph_scripts.myanime_analysis import generate_myanime_graphs
    _, img2 = generate_myanime_graphs()
    return send_file(img2, mimetype='image/png') if img2 else "Error generating favorites plot", 500

@app.route('/graph/4chan')
def fourchan_graphs():
    return render_template('platform_graphs.html', platform="4chan")

@app.route('/graph/4chan/sentiment')
def fourchan_sentiment_graph():
    from graph_scripts.chan_analysis import generate_4chan_graphs
    img1, _ = generate_4chan_graphs()
    return send_file(img1, mimetype='image/png') if img1 else "Error generating sentiment graph", 500

@app.route('/graph/4chan/comments')
def fourchan_comments_graph():
    from graph_scripts.chan_analysis import generate_4chan_graphs
    _, img2 = generate_4chan_graphs()
    return send_file(img2, mimetype='image/png') if img2 else "Error generating comments graph", 500
@app.route('/graph/reddit')
def reddit_graphs():
    return render_template('platform_graphs.html', platform="Reddit")

@app.route('/graph/reddit/comments')
def reddit_comments_graph():
    from graph_scripts.reddit_graphs import generate_reddit_graphs
    img1, _ = generate_reddit_graphs()
    return send_file(img1, mimetype='image/png') if img1 else "Error generating comments graph", 500

@app.route('/graph/reddit/score')
def reddit_score_graph():
    from graph_scripts.reddit_graphs import generate_reddit_graphs
    _, img2 = generate_reddit_graphs()
    return send_file(img2, mimetype='image/png') if img2 else "Error generating score graph", 500
# Route for Politics graphs landing page
@app.route('/graph/politics')
def politics_graphs():
    return render_template('platform_graphs.html', platform="Politics")

@app.route('/graph/politics/date-range', methods=['GET'])
def generate_politics_date_range_graph():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return "Start date and end date are required.", 400

    img = generate_politics_graph_by_date(start_date, end_date)
    if img:
        return send_file(img, mimetype='image/png')
    else:
        return "No posts found for the given date range.", 404

@app.route('/graph/myanimelist/anime/<anime_name>')
def anime_combined_graph(anime_name):
    from graph_scripts.myanime_analysis import generate_specific_anime_graph
    img = generate_specific_anime_graph(anime_name)
    return send_file(img, mimetype='image/png') if img else "Error generating graph", 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)