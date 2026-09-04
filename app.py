from flask import Flask, request, jsonify, render_template_string
import urllib.parse, os, random, time

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TikTok Studio Pro - SUPER FREE</title>
<style>
*{box-sizing:border-box}body{background:#000;color:#fff;font-family:-apple-system,sans-serif;margin:0;padding:0 15px 90px 15px}
.header{text-align:center;padding:20px 0 10px 0;border-bottom:1px solid #1a1a1a;margin-bottom:20px}
.logo-row{display:flex;justify-content:center;align-items:center;gap:10px}.logo-row h1{margin:0;font-size:20px}
.badge-super{background:#ff0050;color:#fff;font-size:9px;padding:3px 7px;border-radius:6px;font-weight:800}
.subtitle-main{color:#00f2ea;font-size:11px;letter-spacing:2px;margin-top:8px;font-weight:700}
.subtitle-desc{color:#666;font-size:11px;margin-top:4px}
.input-container{margin:20px 0 10px 0}.input-box{width:100%;background:#111;border:1.5px solid #333;border-radius:14px;padding:16px;color:#fff;font-size:15px;outline:none}
.btn-generate{width:100%;background:linear-gradient(90deg,#ff0050,#ff2a6d);color:#fff;border:none;padding:16px;border-radius:14px;font-size:16px;font-weight:800;cursor:pointer;margin-bottom:20px}
.card{background:#0a0a0a;border:1.5px solid #ff0050;border-radius:16px;padding:15px;margin-bottom:20px}
.card.cyan-border{border-color:#00f2ea}.card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.card-title{color:#ff0050;font-size:13px;font-weight:700;margin:0}.card.cyan-border .card-title{color:#00f2ea}
.badge-type{border:1px solid #00f2ea;color:#00f2ea;font-size:10px;padding:3px 8px;border-radius:8px}
.card-content-title{font-size:16px;font-weight:700;margin:8px 0;color:#fff}.card-desc{font-size:12px;color:#aaa;line-height:1.5;margin-bottom:12px}
img.ai-img{width:100%;border-radius:12px;border:1px solid #222;display:block;margin-bottom:12px;min-height:200px;background:#111}
audio.hd-audio{width:100%;margin:10px 0}
.action-row{display:flex;gap:8px;flex-wrap:wrap}.action-btn{background:transparent;border:1px solid #ff0050;color:#ff0050;padding:7px 14px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;text-decoration:none}
.card.cyan-border .action-btn{border-color:#00f2ea;color:#00f2ea}
.loading{text-align:center;padding:30px;display:none}.spinner{border:3px solid #222;border-top:3px solid #ff0050;border-radius:50%;width:35px;height:35px;animation:spin 1s linear infinite;margin:0 auto 10px auto}
@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.bottom-nav{position:fixed;bottom:0;left:0;right:0;background:#080808;border-top:1px solid #222;display:flex;justify-content:space-around;padding:10px 0;z-index:1000}
.nav-item{display:flex;flex-direction:column;align-items:center;color:#666;font-size:10px;text-decoration:none;gap:4px}.nav-item.active{color:#ff0050}
</style></head><body>
<div class="header"><div class="logo-row"><h1>TikTok Studio Pro</h1><span class="badge-super">SUPER FREE</span></div><div class="subtitle-main">• HD VIDEO & AUDIO STUDIO •</div><div class="subtitle-desc">AI-powered video generation, voice narration & cinematic assets</div></div>
<div class="input-container"><input id="idea" class="input-box" placeholder="Type your idea: e.g. Funny Crypto Trading"></div>
<button class="btn-generate" onclick="generate()">Generate Real AI Video & HD Audio ✨</button>
<div id="loading" class="loading"><div class="spinner"></div><p style="font-size:12px;color:#888;">Rendering AI video, voiceover & cinematic assets...</p></div>
<div id="result"></div>
<script>
async function generate(){
  let idea=document.getElementById('idea').value; if(!idea){alert('Type an idea first!'); return;}
  document.getElementById('loading').style.display='block'; document.getElementById('result').innerHTML='';
  let res=await fetch('/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({idea:idea})});
  let data=await res.json(); document.getElementById('loading').style.display='none';
  document.getElementById('result').innerHTML=`
    <div class="card"><div class="card-header"><h3 class="card-title">🎬 AI CINEMATIC FRAME</h3><span class="badge-type">AI IMAGE</span></div>
    <div class="card-content-title">${data.viral_idea}</div>
    <img class="ai-img" src="${data.video_url}" loading="eager" onerror="this.src='https://picsum.photos/576/1024?random='+Date.now()">
    <div class="action-row"><a class="action-btn" href="${data.video_url}" target="_blank">Download Frame 📥</a></div></div>
    <div class="card cyan-border"><div class="card-header"><h3 class="card-title">🎙️ HD AI VOICE</h3><span class="badge-type">HQ AUDIO</span></div>
    <audio controls class="hd-audio" src="${data.audio_url}"></audio>
    <div class="action-row"><a class="action-btn" href="${data.audio_url}" target="_blank">Download Audio 🔊</a></div></div>
    <div class="card cyan-border"><div class="card-header"><h3 class="card-title">🖼️ CINEMATIC FRAME & SCRIPT</h3><span class="badge-type">30S ASSET</span></div>
    <img class="ai-img" src="${data.image2}" onerror="this.src='https://picsum.photos/512/512?random='+Date.now()">
    <div class="card-content-title">Full Script Sequence</div><div class="card-desc">${data.script.replace(/\\n/g,'<br>')}</div></div>
    <div class="card"><div class="card-header"><h3 class="card-title">🚀 THUMBNAIL & METADATA</h3><span class="badge-type">GROWTH</span></div>
    <img class="ai-img" src="${data.image3}" onerror="this.src='https://picsum.photos/512/512?random='+Date.now()">
    <div class="card-content-title">Peak: ${data.best_time}</div><div class="card-desc">${data.hashtags}<br><br>${data.caption}</div></div>`;
  window.scrollTo({top:300,behavior:'smooth'});
}
</script></body></html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    idea = data.get('idea', 'Funny Crypto Trading')[:60]
    seed = random.randint(1, 999999)
    viral_idea = f"Viral TikTok: {idea} - You Won't Believe This!"
    hook = f"Stop scrolling if you want to understand {idea}!"
    script = f"0-3s: [HOOK] Stop scrolling if you love {idea}!\n3-10s: [PROBLEM] Why everyone fails at {idea}...\n10-25s: [SOLUTION] The professional way to fix it...\n25-30s: [CTA] Follow for Part 2!"
    hashtags = f"#{idea.replace(' ', '')} #viral #fyp #foryoupage #trending"
    best_time = "Today 7-9 PM"
    caption = f"{viral_idea} {hook} {hashtags}"

    # FAST MODEL + CACHE BUSTER - THIS FIXES EMPTY BOX
    v_prompt = urllib.parse.quote(f"{idea}, cinematic 4k vertical, dramatic lighting")
    video_url = f"https://image.pollinations.ai/prompt/{v_prompt}?width=576&height=1024&nologo=true&model=turbo&seed={seed}"

    p2 = urllib.parse.quote(f"cinematic shot of {idea}, studio lighting, 4k")
    p3 = urllib.parse.quote(f"viral TikTok thumbnail {idea}, eye-catching colors")

    image2 = f"https://image.pollinations.ai/prompt/{p2}?width=512&height=512&nologo=true&model=turbo&seed={seed+1}"
    image3 = f"https://image.pollinations.ai/prompt/{p3}?width=512&height=512&nologo=true&model=turbo&seed={seed+2}"

    audio_text = urllib.parse.quote(f"Attention! Stop scrolling if you want to master {idea}. Watch this right now!")
    audio_url = f"https://text.pollinations.ai/{audio_text}?model=openai-audio&voice=nova"

    return jsonify({
        "viral_idea": viral_idea, "hook": hook, "script": script,
        "hashtags": hashtags, "best_time": best_time, "caption": caption,
        "video_url": video_url, "image2": image2, "image3": image3, "audio_url": audio_url
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
