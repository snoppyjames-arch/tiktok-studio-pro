from flask import Flask, request, jsonify, render_template_string
import requests
import urllib.parse
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TikTok Studio Pro - SUPER FREE</title>
<style>
body{font-family:Arial;background:#000;color:#fff;padding:15px;margin:0}
h1{color:#ff0050;text-align:center;font-size:24px}
.input-box{width:100%;padding:15px;font-size:16px;border-radius:10px;border:2px solid #ff0050;background:#111;color:#fff;box-sizing:border-box}
.btn{width:100%;padding:18px;background:linear-gradient(45deg,#ff0050,#00f2ea);border:none;border-radius:12px;color:#fff;font-size:18px;font-weight:bold;margin-top:15px;cursor:pointer}
.card{background:#111;border:1px solid #333;border-radius:12px;padding:15px;margin-top:15px}
.card h3{color:#00f2ea;margin-top:0}
img.ai-img{width:100%;border-radius:10px;margin-top:10px;border:2px solid #ff0050}
.tag{display:inline-block;background:#222;padding:5px 10px;border-radius:20px;margin:3px;font-size:12px}
.loading{text-align:center;padding:20px;display:none}
.spinner{border:4px solid #333;border-top:4px solid #ff0050;border-radius:50%;width:40px;height:40px;animation:spin 1s linear infinite;margin:20px auto}
@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
</style>
</head>
<body>
<h1>🎬 TikTok Studio Pro<br><small style="font-size:12px;color:#00f2ea">SUPER FREE - ALL IN ONE + AI IMAGES</small></h1>

<input id="idea" class="input-box" placeholder="Type your idea: e.g. funny crypto trader, makeup tutorial">
<button class="btn" onclick="generate()">🚀 Generate 6 in 1 + 3 AI Images - FREE</button>

<div id="loading" class="loading">
<div class="spinner"></div>
<p>Generating viral content + AI images... 10 seconds</p>
</div>

<div id="result"></div>

<script>
async function generate(){
  let idea = document.getElementById('idea').value;
  if(!idea){alert('Type an idea first!'); return;}

  document.getElementById('loading').style.display='block';
  document.getElementById('result').innerHTML='';

  let res = await fetch('/generate', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({idea:idea})
  });
  let data = await res.json();

  document.getElementById('loading').style.display='none';

  document.getElementById('result').innerHTML = `
    <div class="card"><h3>1. 🔥 VIRAL IDEA</h3><p>${data.viral_idea}</p>
    <img class="ai-img" src="${data.image1}" loading="lazy"><br><small>AI Image 1 - Hook Visual</small></div>

    <div class="card"><h3>2. 🎣 HOOK (First 3 seconds)</h3><p>${data.hook}</p></div>

    <div class="card"><h3>3. 📝 FULL SCRIPT (30 sec)</h3><p>${data.script.replace(/\\n/g,'<br>')}</p>
    <img class="ai-img" src="${data.image2}" loading="lazy"><br><small>AI Image 2 - Story Visual</small></div>

    <div class="card"><h3>4. #️⃣ HASHTAGS</h3><p>${data.hashtags.split(' ').map(h=>'<span class=tag>'+h+'</span>').join('')}</p></div>

    <div class="card"><h3>5. ⏰ BEST TIME TO POST</h3><p>${data.best_time}</p>
    <img class="ai-img" src="${data.image3}" loading="lazy"><br><small>AI Image 3 - Thumbnail</small></div>

    <div class="card"><h3>6. ✍️ CAPTION READY</h3><p>${data.caption}</p>
    <button class="btn" onclick="navigator.clipboard.writeText('${data.caption.replace(/'/g,"")}');alert('Copied!')">📋 Copy Caption</button>
    </div>
  `;
  window.scrollTo(0,400);
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    idea = data.get('idea', 'crypto trader')

    # Generate viral content templates
    viral_idea = f"{idea} mistakes you must stop today (Part 2)"
    hook = f"STOP! Don't post about {idea} before watching this! 99% get it wrong!"
    script = f"0-3s: [HOOK] Wait! You doing {idea} wrong?\n3-10s: [PROBLEM] Most people fail because they don't know this secret...\n10-25s: [SOLUTION] Here's what works: Tip 1, Tip 2, Tip 3 for {idea}...\n25-30s: [CTA] Follow for Part 3! Comment '{idea}' for full guide!"
    hashtags = f"#{idea.replace(' ','')} #viral #tiktokcameroon #yaounde #fyp #foryou #{idea.split()[0]}tok"
    best_time = "Today 7:00 PM - 9:30 PM Yaounde time (WAT) - Best engagement!"
    caption = f"{viral_idea} 🔥 {hook} {hashtags}"

    # FREE AI Images via Pollinations (no API key needed)
    # 3 different styles
    p1 = urllib.parse.quote(f"3d render of {idea}, funny, viral tiktok style, bright colors, high detail, 8k")
    p2 = urllib.parse.quote(f"cinematic photo of {idea}, dramatic lighting, professional, trending on tiktok")
    p3 = urllib.parse.quote(f"thumbnail style, bold text {idea}, youtube viral, colorful, attention grabbing")

    image1 = f"https://image.pollinations.ai/prompt/{p1}?width=512&height=512&nologo=true"
    image2 = f"https://image.pollinations.ai/prompt/{p2}?width=512&height=512&nologo=true"
    image3 = f"https://image.pollinations.ai/prompt/{p3}?width=512&height=512&nologo=true"

    return jsonify({
        "viral_idea": viral_idea,
        "hook": hook,
        "script": script,
        "hashtags": hashtags,
        "best_time": best_time,
        "caption": caption,
        "image1": image1,
        "image2": image2,
        "image3": image3
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)