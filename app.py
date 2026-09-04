from flask import Flask, request, jsonify, render_template_string
import urllib.parse, os, random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TikTok Studio Pro - WORKING</title>
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#ff0050">
<style>
*{box-sizing:border-box}body{background:#000;color:#fff;font-family:-apple-system,sans-serif;margin:0;padding:0 15px 100px 15px}
.header{text-align:center;padding:20px 0 10px;border-bottom:1px solid #222}
.badge-super{background:#ff0050;color:#fff;font-size:10px;padding:4px 8px;border-radius:6px;font-weight:800}
.btn-generate{width:100%;background:linear-gradient(90deg,#ff0050,#00f2ea);color:#000;border:none;padding:18px;border-radius:14px;font-size:17px;font-weight:900;cursor:pointer;margin:15px 0}
.card{background:#111;border:1px solid #333;border-radius:16px;padding:15px;margin-bottom:15px}
.card-title{color:#ff0050;font-weight:800;margin-bottom:10px}
video,img{width:100%;border-radius:12px;background:#000;min-height:250px}
#canvas{display:none}
.progress{width:100%;height:6px;background:#222;border-radius:10px;overflow:hidden;margin:10px 0}
.progress-bar{height:100%;width:0%;background:linear-gradient(90deg,#ff0050,#00f2ea);transition:width 0.2s}
</style></head><body>
<div class="header"><h1>TikTok Studio Pro <span class="badge-super">STABLE V2</span></h1><p style="color:#00f2ea;font-size:11px">RELIABLE HTML5 CANVAS GENERATOR</p></div>
<input id="idea" style="width:100%;background:#111;border:1.5px solid #333;border-radius:14px;padding:16px;color:#fff;font-size:15px" placeholder="e.g. Crypto Trading Secrets">
<button class="btn-generate" onclick="generateFull()">Generate Video MP4 🎬</button>
<div id="loading" style="display:none;text-align:center;padding:20px"><div style="border:3px solid #222;border-top:3px solid #ff0050;border-radius:50%;width:35px;height:35px;animation:spin 1s linear infinite;margin:auto"></div><p>Assembling video frames & voice...</p><div class="progress"><div id="bar" class="progress-bar"></div></div></div>
<style>@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}</style>
<div id="result"></div>
<canvas id="canvas" width="576" height="1024"></canvas>
<script>
let aiData=null;
async function generateFull(){
 let idea=document.getElementById('idea').value; if(!idea){alert('Type an idea first');return;}
 document.getElementById('loading').style.display='block'; document.getElementById('result').innerHTML=''; document.getElementById('bar').style.width='20%';

 let res=await fetch('/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({idea})});
 aiData=await res.json(); document.getElementById('bar').style.width='50%';

 let imgs=await Promise.all([loadImg(aiData.image1),loadImg(aiData.image2),loadImg(aiData.image3)]);
 document.getElementById('bar').style.width='75%';

 let mp4Url=await buildMp4(imgs);
 document.getElementById('bar').style.width='100%';
 document.getElementById('loading').style.display='none';

 document.getElementById('result').innerHTML=`
   <div class="card"><div class="card-title">✅ SUCCESS - VIDEO READY</div>
   <video controls autoplay loop src="${mp4Url}" style="border:2px solid #00f2ea"></video>
   <p style="font-size:12px;color:#aaa"><b>${aiData.viral_idea}</b><br><br>${aiData.script.replace(/\\n/g,'<br>')}</p>
   <a href="${mp4Url}" download="tiktok-video-${Date.now()}.webm" style="display:block;background:#ff0050;color:#fff;text-align:center;padding:12px;border-radius:10px;text-decoration:none;font-weight:800;margin-top:10px">Download MP4/WebM 📥</a>
   </div>
   <div class="card"><div class="card-title">🎙️ AI NARRATION AUDIO</div><audio controls src="${aiData.audio_url}" style="width:100%"></audio></div>
   <div class="card"><div class="card-title">📦 ASSETS</div><img src="${aiData.image1}"><img src="${aiData.image2}" style="margin-top:8px"></div>
 `;
}
function loadImg(src){return new Promise((res)=>{let i=new Image();i.crossOrigin='anonymous';i.onload=()=>res(i);i.onerror=()=>{let f=new Image();f.src='https://picsum.photos/576/1024';f.onload=()=>res(f);};i.src=src;})}
async function buildMp4(images){
 return new Promise((resolve)=>{
  const canvas=document.getElementById('canvas'); const ctx=canvas.getContext('2d');
  const stream=canvas.captureStream(30); const chunks=[];
  const recorder=new MediaRecorder(stream,{mimeType:'video/webm'});
  recorder.ondataavailable=e=>chunks.push(e.data);
  recorder.onstop=()=>{let blob=new Blob(chunks,{type:'video/webm'}); resolve(URL.createObjectURL(blob));};
  recorder.start(); let frame=0; let total=30*8;
  let interval=setInterval(()=>{
    let idx=Math.floor((frame/total)*images.length); if(idx>=images.length) idx=images.length-1;
    let img=images[idx]; ctx.fillStyle='#000'; ctx.fillRect(0,0,576,1024);
    ctx.drawImage(img,0,0,576,1024);
    let captionText = "";
    if (frame < 90) {
      captionText = aiData.viral_idea;
    } else if (frame < 180) {
      captionText = "CORE VALUE REVELATION";
    } else {
      captionText = "CALL TO ACTION - FOLLOW!";
    }
    ctx.save();
    ctx.font = '900 26px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    let textWidth = ctx.measureText(captionText).width;
    let boxWidth = Math.min(textWidth + 50, 520);
    let boxHeight = 60;
    let boxX = (576 - boxWidth) / 2;
    let boxY = 780;
    ctx.fillStyle = 'rgba(168, 85, 247, 0.95)';
    ctx.beginPath();
    if (ctx.roundRect) {
      ctx.roundRect(boxX, boxY, boxWidth, boxHeight, 14);
    } else {
      ctx.rect(boxX, boxY, boxWidth, boxHeight);
    }
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = '#ffffff';
    ctx.stroke();
    ctx.fillStyle = '#ffffff';
    ctx.fillText(captionText, 576 / 2, boxY + boxHeight / 2);
    ctx.font = 'bold 16px sans-serif';
    ctx.fillStyle = '#00f2ea';
    ctx.fillText(aiData.hashtags, 576 / 2, boxY + boxHeight + 35);
    ctx.restore();
    frame++; if(frame>=total){clearInterval(interval); recorder.stop();}
  },1000/30);
 });
}
</script></body></html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/manifest.json')
def manifest():
    return jsonify({
        "name": "TikTok Studio Pro",
        "short_name": "TikTok Studio",
        "description": "Reliable HTML5 Canvas Generator for TikTok Videos",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#000000",
        "theme_color": "#ff0050",
        "icons": [
            {
                "src": "https://cdn-icons-png.flaticon.com/512/3046/3046120.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "https://cdn-icons-png.flaticon.com/512/3046/3046120.png",
                "sizes": "192x192",
                "type": "image/png"
            }
        ]
    })

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    idea = data.get('idea','Crypto Trading')[:50]
    seed = random.randint(1,9999)
    p = lambda txt: urllib.parse.quote(txt)
    viral_idea = f"Stop scrolling! The truth about {idea}"
    hashtags = f"#{idea.replace(' ','')} #viral #fyp #trending"
    script = f"0-3s: Hook about {idea}\\n3-6s: Core value revelation\\n6-8s: Call to action"
    base = "https://image.pollinations.ai/prompt"
    img1 = f"{base}/{p(idea+', vertical cinematic portrait')}?width=576&height=1024&nologo=true&seed={seed}"
    img2 = f"{base}/{p(idea+', neon lighting 4k vertical')}?width=576&height=1024&nologo=true&seed={seed+1}"
    img3 = f"{base}/{p(idea+', dark abstract background vertical')}?width=576&height=1024&nologo=true&seed={seed+2}"
    audio = f"https://translate.google.com/translate_tts?ie=UTF-8&q={p(viral_idea)}&tl=en&client=tw-ob"
    return jsonify({"viral_idea":viral_idea,"hashtags":hashtags,"script":script,"image1":img1,"image2":img2,"image3":img3,"audio_url":audio})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",10000)))
