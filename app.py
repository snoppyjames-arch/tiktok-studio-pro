from flask import Flask, request, jsonify, render_template_string
import requests
import urllib.parse
import os
from datetime import datetime

app = Flask(__name__)

# [Keep your full HTML string here]

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    idea = data.get('idea', 'Funny Crypto Trading')
    viral_idea = f"Viral TikTok: {idea}"
    hook = f"Stop scrolling if you want to understand {idea}!"
    script = f"0-3s: [HOOK] Stop scrolling!\n3-10s: [PROBLEM] Why everyone fails at {idea}...\n10-25s: [SOLUTION] The professional way to fix it...\n25-30s: [CTA] Follow for Part 2!"
    hashtags = f"#{idea.replace(' ','')} #viral #fyp #foryoupage #trending"
    best_time = "Today 7–9 PM"
    
    p1 = urllib.parse.quote(f"vibrant 3D render illustration of {idea}, trending tiktok style, high contrast, neon aesthetic")
    p2 = urllib.parse.quote(f"cinematic shot of {idea}, professional dramatic studio lighting, 4k resolution")
    p3 = urllib.parse.quote(f"bold YouTube and TikTok thumbnail background style representing {idea}, eye-catching colors")
    
    image1 = f"https://image.pollinations.ai/prompt/{p1}?width=512&height=350&nologo=true"
    image2 = f"https://image.pollinations.ai/prompt/{p2}?width=512&height=350&nologo=true"
    image3 = f"https://image.pollinations.ai/prompt/{p3}?width=512&height=350&nologo=true"
    
    audio_text = urllib.parse.quote(f"Attention! Stop scrolling if you want to master {idea}. Watch this right now!")
    audio_url = f"https://text.pollinations.ai/{audio_text}?model=openai-audio"

    return jsonify({
        "viral_idea": viral_idea,
        "hook": hook,
        "script": script,
        "hashtags": hashtags,
        "best_time": best_time,
        "image1": image1,
        "image2": image2,
        "image3": image3,
        "audio_url": audio_url
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

.card {
    background: #0a0a0a;
    border: 1.5px solid #ff0050;
    border-radius: 16px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 0 12px rgba(255, 0, 80, 0.15);
    position: relative;
}

.card.cyan-border {
    border-color: #00f2ea;
    box-shadow: 0 0 12px rgba(0, 242, 234, 0.15);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.card-title {
    color: #ff0050;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
    margin: 0;
}

.card.cyan-border .card-title {
    color: #00f2ea;
}

.badge-type {
    border: 1px solid #00f2ea;
    color: #00f2ea;
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 8px;
    font-weight: 600;
}

.card.cyan-border .badge-type {
    border-color: #ff0050;
    color: #ff0050;
}

.card-content-title {
    font-size: 16px;
    font-weight: 700;
    margin: 5px 0;
    color: #fff;
}

.card-desc {
    font-size: 12px;
    color: #aaa;
    margin: 0 0 12px 0;
    line-height: 1.4;
}

img.ai-img {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #333;
    display: block;
    margin-bottom: 10px;
}

audio.hd-audio {
    width: 100%;
    margin: 10px 0;
    border-radius: 8px;
    outline: none;
}

.action-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 10px;
}

.action-btn {
    background: transparent;
    border: 1px solid #ff0050;
    color: #ff0050;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    text-decoration: none;
}

.card.cyan-border .action-btn {
    border-color: #00f2ea;
    color: #00f2ea;
}

.loading {
    text-align: center;
    padding: 30px;
    display: none;
}

.spinner {
    border: 3px solid #222;
    border-top: 3px solid #ff0050;
    border-radius: 50%;
    width: 35px;
    height: 35px;
    animation: spin 1s linear infinite;
    margin: 0 auto 10px auto;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Bottom Navigation Bar */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #080808;
    border-top: 1px solid #222;
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
    z-index: 1000;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #666;
    font-size: 10px;
    text-decoration: none;
    gap: 4px;
}

.nav-item.active {
    color: #ff0050;
}

.nav-item svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
}
</style>
</head>
<body>

<div class="header">
    <div class="logo-row">
        <h1>
            <svg viewBox="0 0 24 24" width="20" height="20" fill="#ff0050"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 3 15.68a6.33 6.33 0 0 0 10.85 4.48V11.2a8.16 8.16 0 0 0 4.96 1.67V9.4a4.85 4.85 0 0 1-1.22-.12z"/></svg>
            TikTok Studio Pro
        </h1>
        <span class="badge-super">SUPER FREE</span>
    </div>
    <div class="subtitle-container">
        <div class="subtitle-main">• HD AUDIO & VIDEO •</div>
        <div class="subtitle-desc">AI-powered voice narration, visual art & cinematic assets</div>
    </div>
</div>

<div class="input-container">
    <input id="idea" class="input-box" placeholder="Type your idea: e.g. Funny Crypto Trading">
</div>
<button class="btn-generate" onclick="generate()">Generate Viral Media & HD Audio ✨</button>

<div id="loading" class="loading">
    <div class="spinner"></div>
    <p style="font-size:12px; color:#888;">Synthesizing HD audio voiceover & AI visuals...</p>
</div>

<div id="result"></div>

<div class="bottom-nav">
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
        Home
    </a>
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
        Create
    </a>
    <a href="#" class="nav-item active">
        <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        Studio Pro
    </a>
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
        Inbox
    </a>
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
        Profile
    </a>
</div>

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
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">💡 VIRAL CONCEPT & IMAGE</h3>
            <span class="badge-type">AI VISUAL</span>
        </div>
        <div class="card-content-title">${data.viral_idea}</div>
        <div class="card-desc">Hook: "${data.hook}"</div>
        <img class="ai-img" src="${data.image1}" loading="lazy">
        <div class="action-row">
            <button class="action-btn" onclick="navigator.clipboard.writeText(\`${data.viral_idea}\`);alert('Idea Copied!')">Copy Idea</button>
            <a class="action-btn" href="${data.image1}" target="_blank" download="ai_image_1.jpg">Download Image 📥</a>
        </div>
    </div>

    <div class="card cyan-border">
        <div class="card-header">
            <h3 class="card-title">🎙️ HD AI VOICE NARRATION</h3>
            <span class="badge-type">HQ AUDIO</span>
        </div>
        <div class="card-desc">Listen to the synthesized HD voiceover for your hook and script line:</div>
        <audio controls class="hd-audio" src="${data.audio_url}"></audio>
        <div class="action-row">
            <a class="action-btn" href="${data.audio_url}" target="_blank" download="hd_voiceover.mp3">Download HD Audio 🔊</a>
        </div>
    </div>

    <div class="card cyan-border">
        <div class="card-header">
            <h3 class="card-title">🎬 AI CINEMATIC FRAME & SCRIPT</h3>
            <span class="badge-type">30S ASSET</span>
        </div>
        <img class="ai-img" src="${data.image2}" loading="lazy">
        <div class="card-content-title">Full Script Sequence</div>
        <div class="card-desc">${data.script.replace(/\\n/g,'<br>')}</div>
        <div class="action-row">
            <button class="action-btn" onclick="navigator.clipboard.writeText(\`${data.script}\`);alert('Script Copied!')">Copy Script</button>
            <a class="action-btn" href="${data.image2}" target="_blank" download="ai_image_2.jpg">Download Image 📥</a>
        </div>
    </div>

    <div class="card">
        <div class="card-header">
            <h3 class="card-title">🚀 THUMBNAIL & VIDEO ASSET IDEA</h3>
            <span class="badge-type">VIDEO CONCEPT</span>
        </div>
        <img class="ai-img" src="${data.image3}" loading="lazy">
        <div class="card-content-title">Peak Engagement: ${data.best_time}</div>
        <div class="card-desc">Hashtags: ${data.hashtags}</div>
        <div class="action-row">
            <button class="action-btn" onclick="navigator.clipboard.writeText(\`${data.hashtags}\`);alert('Hashtags Copied!')">Copy Hashtags</button>
            <a class="action-btn" href="${data.image3}" target="_blank" download="ai_image_3.jpg">Download Thumbnail 📥</a>
        </div>
    </div>
  `;
  window.scrollTo({top: 300, behavior: 'smooth'});
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
    idea = data.get('idea', 'Funny Crypto Trading')
    viral_idea = f"Viral TikTok: {idea}"
    hook = f"Stop scrolling if you want to understand {idea}!"
    script = f"0-3s: [HOOK] Stop scrolling!\\n3-10s: [PROBLEM] Why everyone fails at {idea}...\\n10-25s: [SOLUTION] The professional way to fix it...\\n25-30s: [CTA] Follow for Part 2!"
    hashtags = f"#{idea.replace(' ','')} #viral #fyp #foryoupage #trending"
    best_time = "Today 7–9 PM"
    
    # Generate tailored parameters for Pollinations AI image generation based on user input
    p1 = urllib.parse.quote(f"vibrant 3D render illustration of {idea}, trending tiktok style, high contrast, neon aesthetic")
    p2 = urllib.parse.quote(f"cinematic shot of {idea}, professional dramatic studio lighting, 4k resolution")
    p3 = urllib.parse.quote(f"bold YouTube and TikTok thumbnail background style representing {idea}, eye-catching colors")
    
    image1 = f"https://image.pollinations.ai/prompt/{p1}?width=512&height=350&nologo=true"
    image2 = f"https://image.pollinations.ai/prompt/{p2}?width=512&height=350&nologo=true"
    image3 = f"https://image.pollinations.ai/prompt/{p3}?width=512&height=350&nologo=true"
    
    # Generate HD Text-to-Speech audio using Pollinations AI audio endpoint
    audio_text = urllib.parse.quote(f"Attention! Stop scrolling if you want to master {idea}. Watch this right now!")
    audio_url = f"https://text.pollinations.ai/{audio_text}?model=openai-audio"

    return jsonify({
        "viral_idea": viral_idea,
        "hook": hook,
        "script": script,
        "hashtags": hashtags,
        "best_time": best_time,
        "image1": image1,
        "image2": image2,
        "image3": image3,
        "audio_url": audio_url
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

.card {
    background: #0a0a0a;
    border: 1.5px solid #ff0050;
    border-radius: 16px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 0 12px rgba(255, 0, 80, 0.15);
    position: relative;
}

.card.cyan-border {
    border-color: #00f2ea;
    box-shadow: 0 0 12px rgba(0, 242, 234, 0.15);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.card-title {
    color: #ff0050;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
    margin: 0;
}

.card.cyan-border .card-title {
    color: #00f2ea;
}

.badge-type {
    border: 1px solid #00f2ea;
    color: #00f2ea;
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 8px;
    font-weight: 600;
}

.card.cyan-border .badge-type {
    border-color: #ff0050;
    color: #ff0050;
}

.card-content-title {
    font-size: 16px;
    font-weight: 700;
    margin: 5px 0;
    color: #fff;
}

.card-desc {
    font-size: 12px;
    color: #aaa;
    margin: 0 0 12px 0;
    line-height: 1.4;
}

img.ai-img {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #333;
    display: block;
}

.action-btn {
    background: transparent;
    border: 1px solid #ff0050;
    color: #ff0050;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    margin-top: 10px;
}

.card.cyan-border .action-btn {
    border-color: #00f2ea;
    color: #00f2ea;
}

.loading {
    text-align: center;
    padding: 30px;
    display: none;
}

.spinner {
    border: 3px solid #222;
    border-top: 3px solid #ff0050;
    border-radius: 50%;
    width: 35px;
    height: 35px;
    animation: spin 1s linear infinite;
    margin: 0 auto 10px auto;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Bottom Navigation Bar */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #080808;
    border-top: 1px solid #222;
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
    z-index: 1000;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #666;
    font-size: 10px;
    text-decoration: none;
    gap: 4px;
}

.nav-item.active {
    color: #ff0050;
}

.nav-item svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
}
</style>
</head>
<body>

<div class="header">
    <div class="logo-row">
        <h1>
            <svg viewBox="0 0 24 24" width="20" height="20" fill="#ff0050"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 3 15.68a6.33 6.33 0 0 0 10.85 4.48V11.2a8.16 8.16 0 0 0 4.96 1.67V9.4a4.85 4.85 0 0 1-1.22-.12z"/></svg>
            TikTok Studio Pro
        </h1>
        <span class="badge-super">SUPER FREE</span>
    </div>
    <div class="subtitle-container">
        <div class="subtitle-main">• ALL IN ONE •</div>
        <div class="subtitle-desc">AI-powered content tools to grow faster</div>
    </div>
</div>

<div class="input-container">
    <input id="idea" class="input-box" placeholder="Type your idea: e.g. Neon Sneaker Review">
</div>
<button class="btn-generate" onclick="generate()">Generate Viral Package ✨</button>

<div id="loading" class="loading">
    <div class="spinner"></div>
    <p style="font-size:12px; color:#888;">Generating viral assets & AI imagery...</p>
</div>

<div id="result"></div>

<div class="bottom-nav">
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
        Home
    </a>
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
        Create
    </a>
    <a href="#" class="nav-item active">
        <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        Studio Pro
    </a>
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
        Inbox
    </a>
    <a href="#" class="nav-item">
        <svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
        Profile
    </a>
</div>

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
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">💡 VIRAL IDEA</h3>
            <span class="badge-type">3D RENDER</span>
        </div>
        <div class="card-content-title">${data.viral_idea}</div>
        <div class="card-desc">Hook: "${data.hook}"</div>
        <img class="ai-img" src="${data.image1}" loading="lazy">
        <button class="action-btn" onclick="navigator.clipboard.writeText(\`${data.viral_idea}\`);alert('Idea Copied!')">Use Idea →</button>
    </div>

    <div class="card cyan-border">
        <div class="card-header">
            <h3 class="card-title">📄 SCRIPT</h3>
            <span class="badge-type">CINEMATIC PHOTO</span>
        </div>
        <img class="ai-img" style="margin-bottom:10px;" src="${data.image2}" loading="lazy">
        <div class="card-content-title">30s Hook Script</div>
        <div class="card-desc">${data.script.replace(/\\n/g,'<br>')}</div>
        <button class="action-btn" onclick="navigator.clipboard.writeText(\`${data.script}\`);alert('Script Copied!')">Generate Script →</button>
    </div>

    <div class="card">
        <div class="card-header">
            <h3 class="card-title">⏰ BEST TIME TO POST</h3>
            <span class="badge-type">THUMBNAIL STYLE</span>
        </div>
        <img class="ai-img" style="margin-bottom:10px;" src="${data.image3}" loading="lazy">
        <div class="card-content-title">Peak Engagement: ${data.best_time}</div>
        <div class="card-desc">Hashtags: ${data.hashtags}</div>
        <button class="action-btn" onclick="navigator.clipboard.writeText(\`${data.best_time}\`);alert('Schedule info copied!')">Schedule →</button>
    </div>
  `;
  window.scrollTo({top: 300, behavior: 'smooth'});
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
    idea = data.get('idea', 'Neon Sneaker Review')
    viral_idea = f"{idea} Trends"
    hook = f"You won't believe how this {idea} performs..."
    script = f"0-3s: [HOOK] Stop scrolling if you love {idea}\\n3-10s: [PROBLEM] Why most fail...\\n10-25s: [SOLUTION] The exact method...\\n25-30s: [CTA] Follow for updates!"
    hashtags = f"#{idea.replace(' ','')} #viral #fyp #foryou"
    best_time = "Today 7–9pm"
    caption = f"{viral_idea} {hook} {hashtags}"
    p1 = urllib.parse.quote(f"3d render of {idea}, funny, viral tiktok style, bright colors")
    p2 = urllib.parse.quote(f"cinematic photo of {idea}, dramatic lighting
, professional")
p3 = urllib.parse.quote(f"thumbnail style, bold text {idea}, viral, colorful")
image1 = f"https://image.pollinations.ai/prompt/{p1}?width=512&height=350&nologo=true"
image2 = f"https://image.pollinations.ai/prompt/{p2}?width=512&height=350&nologo=true"
image3 = f"https://image.pollinations.ai/prompt/{p3}?width=512&height=350&nologo=true"
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
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
