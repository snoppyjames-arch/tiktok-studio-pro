from flask import Flask, request, send_from_directory, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = """
<h1 style="text-align:center">My Studio - Learning Project</h1>
<p style="text-align:center">Upload your OWN videos only</p>

<form method="POST" action="/upload" enctype="multipart/form-data" style="text-align:center">
  <input type="file" name="video" accept="video/*" required>
  <button type="submit">Upload Video</button>
</form>

<hr>
<h3>My Videos - Download</h3>
{% for f in files %}
  <div>{{f}} - <a href="/download/{{f}}"><button>Download</button></a></div>
{% endfor %}
"""

@app.route('/')
def home():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML, files=files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['video']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return '<script>window.location="/"</script>'

@app.route('/download/<name>')
def download(name):
    return send_from_directory(UPLOAD_FOLDER, name, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
