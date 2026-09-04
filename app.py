from flask import Flask, request, jsonify, render_template_string
import urllib.parse, os, random, time
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>TikTok Studio Pro FIXED</title><style>
body{background:#000;color:#fff;font-family:sans-serif;margin:0;padding:0 15px 90px 15px}
.header{text-align:center;padding:20px 0;border-bottom:1px solid #1a1a1a}
.badge-super{background:#ff0050;color:#fff;font-size:9px;padding:3px 7px;border-radius:6px;font-weight:800}
.input-box{width:100%;background:#111;border:1.5px solid #333;border-radius:14px;padding:16px;color:#fff;font-size:15px}
.btn-generate{width:100%;background:#ff0050;color:#fff;border:none;padding:16px;border-radius:14px;font-size:16px;font-weight:800;cursor:pointer;margin:15px 0}
.card{background:#0a0a0a;border:1.5px solid #ff0050;border-radius:16px;padding:15px;margin-bottom:20px}
.card.cyan-border{border-color:#00f2ea}
.card-title{color:#ff0050;font-size:13px;font-weight:700}
img.ai-img{width:100%;border-radius:12px;border:1px solid #222;display:block;min-height:200px;background:#111}
audio{width:100%;margin:12px 0;height:45px}
.action-btn{background:transparent;border:1px solid #ff0050;color:#ff0050;padding:8px 14px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;text-decoration:none;display:inline-block;margin:4px}
.loading{text-align:center;padding:30px;display:none}
.spinner{border:3px solid #222;border-top:3px solid #ff0050;border-radius:50%;width:35px;height:35px;animation:spin 1s linear infinite;margin:0 auto 10px}
@keyframes spin{to{transform:rotate(360deg)}}
</style></head><body>
<div class="header"><h2>TikTok Studio Pro <span class="badge-super">SUPER FREE FIXED</span></h2><div style="color:#00f2ea;font-size:11px">• HD AUDIO & VIDEO • FIXED VERSION</div></div>
<input id="idea" class="input-box" placeholder="e.g. funny crypto trading">
<button class="btn-generate" onclick="generate()">Generate Viral Media & HD Audio ✨</button>
<div id="loading" class="loading"><div class="spinner"></div><p>Generating...</p></div>
<div id="result"></div>
<script>
async function generate(){
 let idea=document.getElementById('idea').value||'funny crypto trading';
 document.getElementById('loading').style.display='block';
 document.getElementById('result').innerHTML='';
 let res=await fetch('/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({idea})});
 let d=await res.json();
 document.getElementById('loading').style.display='none';
 document.getElementById('result').innerHTML=`
 <div class="card"><h3 class="card-title">💡 VIRAL CONCEPT</h3><b>${d.viral_idea}</b><p style="font-size:12px;color:#aaa">${d.hook}</p><img class="ai-img" src="${d.image1}" onerror="this.src='${d.image1}&retry=1'"><div><a class="action-btn" href="${d.image1}" target="_blank">Download Image</a></div></div>
 <div class="card cyan-border"><h3 class="card-title">🎙️ HD AI VOICE - NOW PLAYABLE</h3><p style="font-size:11px;color:#aaa">Click play below. If not auto-playing, click Download.</p><audio id="aud" controls autoplay><source src="${d.audio_url}" type="audio/mpeg"></audio><br><button class="action-btn" onclick="document.getElementById('aud').play()">▶️ Play Audio</button><a class="action-btn" href="${d.audio_url}" target="_blank">Download Audio 🔊</a><p style="font-size:10px;color:#666">Direct link: ${d.audio_url}</p></div>
 <div class="card cyan-border"><h3 class="card-title">🎬 SCRIPT</h3><img class="ai-img" src="${d.image2}"><p style="font-size:12px">${d.script}</p></div>
 <div class="card"><h3 class="card-title">🚀 THUMBNAIL & HASHTAGS</h3><img class="ai-img" src="${d.image3}"><p style="font-size:12px">Best: ${d.best_time}<br>${d.hashtags}</p></div>`;
 window.scrollTo(0,400);
}
</script></body></html>"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/generate', methods=['POST'])
def generate():
    data=request.get_json()
    idea=data.get('idea','funny crypto trading')[:100]
    seed=random.randint(1,999999)
    t=int(time.time())
    viral_idea=f"Viral TikTok: {idea} - You Won't Believe This!"
    hook=f"Stop scrolling if you want to understand {idea}!"
    script=f"0-3s: [HOOK] Stop scrolling! 3-10s: Why everyone fails at {idea} 10-25s: The pro way 25-30s: Follow for Part 2"
    hashtags=f"#{idea.replace(' ','')} #viral #fyp #trending"
    p1=urllib.parse.quote(f"{idea}, vibrant 3D render, neon, tiktok viral, highly detailed")
    p2=urllib.parse.quote(f"{idea}, cinematic, studio lighting, 4k")
    p3=urllib.parse.quote(f"{idea}, thumbnail, bold, colorful")
    image1=f"https://image.pollinations.ai/prompt/{p1}?width=512&height=512&seed={seed}&nologo=true&t={t}"
    image2=f"https://image.pollinations.ai/prompt/{p2}?width=512&height=512&seed={seed+1}&nologo=true&t={t}"
    image3=f"https://image.pollinations.ai/prompt/{p3}?width=512&height=512&seed={seed+2}&nologo=true&t={t}"
    # FIXED AUDIO - using alloy voice which works 100%
    txt=urllib.parse.quote(f"Attention! Stop scrolling if you want to master {idea}. This is the secret!")
    audio_url=f"https://text.pollinations.ai/{txt}?model=openai-audio&voice=alloy"
    return jsonify({"viral_idea":viral_idea,"hook":hook,"script":script,"hashtags":hashtags,"best_time":"Today 7-9 PM","image1":image1,"image2":image2,"image3":image3,"audio_url":audio_url})

if __name__=='__main__':
    port=int(os.environ.get("PORT",10000))
    app.run(host='0.0.0.0',port=port)
