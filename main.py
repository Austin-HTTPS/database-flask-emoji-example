import flask
from replit import db

EMOJI = ['💯', '❤️', '🥳', '💩', '💻', '💾']

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def comments():
	counts = db.get('emoji', {})
	if flask.request.method == "POST" and 'emoji' in flask.request.form:
		emoji = flask.request.form['emoji']
		if emoji in EMOJI:
			try:
				counts[emoji] += 1
			except KeyError:
				counts[emoji] = 1
			db['emoji'] = counts
	sorted_counts = sorted(counts.items(), key=lambda el: el[1], reverse=True)
	return flask.render_template(
	    'emoji.html', emoji=EMOJI, counts=sorted_counts)


app.run('0.0.0.0')
