from flask import Flask, request, send_from_directory, render_template_string
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

TOKEN_ADDRESS = "0xc8863de847ed7487cb276b657ac1331ac2731ed5"
RECEIVER_WALLET = "0x39300D499C23c23b682fDd02CCD54d123A0Aa740"

HTML = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ACHIEVE $ACHV - Smart Archiving</title>
<link rel="icon" href="/logo-192.png">
<script src="https://cdn.jsdelivr.net/npm/ethers@6.8.1/dist/ethers.umd.min.js"></script>
<style>
body{{margin:0;font-family:Arial,sans-serif;background:#0a1628;color:white;text-align:center}}
.top{{background:linear-gradient(135deg,#00a8ff,#0057ff);padding:25px 15px}}
.logo{{width:120px;height:120px;border-radius:24px;background:white;padding:8px}}
h1{{margin:5px 0 0 0;font-size:34px;color:#fff}} .h1-gold{{color:#ffcc00;margin:0;font-size:30px}}
.motto{{color:#00ff88;font-weight:bold;margin:10px 0}} .btn{{background:#00ff88;color:#000;padding:12px 20px;border:none;border-radius:10px;font-weight:bold;cursor:pointer;margin:6px}}
.btn-red{{background:#ff4444;color:white;padding:6px 12px}} .btn-blue{{background:#00a8ff;color:white}}
.card{{background:#122840;margin:15px auto;padding:18px;border-radius:14px;max-width:450px;border:1px solid #1e3a5f}}
.small{{font-size:11px;color:#8aa0b8;word-break:break-all}} .file-row{{background:#0f2340;padding:10px;margin:6px 0;border-radius:8px;display:flex;justify-content:space-between}}
</style>
</head>
<body>
<div class="top">
<img class="logo" src="/logo-512.png" alt="ACHV">
<h1>ACHIEVE</h1><h1 class="h1-gold">$ACHV</h1>
<div class="motto">We Fix Your Phone, Not Just Your Portfolio.<br><span style="color:white;font-size:13px">Free Your Phone. Save Your Data. Own Your Future.</span></div>
</div>
<div class="card">
<p><b>Token:</b><br><span class="small">{TOKEN_ADDRESS}</span></p>
<p><b>BSC Wallet:</b><br><span class="small">{RECEIVER_WALLET}</span></p>
<p>Phone FULL? Pay 1000 $ACHV to unlock</p>
<button class="btn" id="connect">Connect Wallet</button>
<button class="btn" id="pay">Pay 1000 $ACHV</button>
<p id="status" style="color:#00ff88;font-weight:bold"></p>
<form method="POST" action="/upload" enctype="multipart/form-data" id="upForm" style="margin-top:15px">
<input type="file" name="video" accept="image/*,video/*" required>
<button type="submit" class="btn btn-blue">Upload</button>
</form>
</div>
<div class="card"><h3>My Files</h3>
{{% for f in files %}}
<div class="file-row"><span>{{{{f}}}}</span><span><a href="/download/{{{{f}}}}"><button class="btn btn-blue" style="padding:6px 10px">Download</button></a> <a href="/delete/{{{{f}}}}"><button class="btn btn-red">Delete</button></a></span></div>
{{% endfor %}}
</div>
<script>
const tokenAddress="{TOKEN_ADDRESS}"; const receiver="{RECEIVER_WALLET}";
const abi=["function transfer(address to,uint amount) returns (bool)"]; let unlocked=false;
document.getElementById("connect").onclick=async()=>{{ await window.ethereum.request({{method:'eth_requestAccounts'}}); document.getElementById("status").innerText="Connected!"; }};
document.getElementById("pay").onclick=async()=>{{ try{{ const p=new ethers.BrowserProvider(window.ethereum); const s=await p.getSigner(); const t=new ethers.Contract(tokenAddress,abi,s); const tx=await t.transfer(receiver,ethers.parseUnits("1000",18)); document.getElementById("status").innerText="Paying..."; await tx.wait(); document.getElementById("status").innerText="Paid! Unlocked"; unlocked=true; }}catch(e){{document.getElementById("status").innerText=e.message}} }};
document.getElementById("upForm").onsubmit=(e)=>{{ if(!unlocked){{alert("Pay 1000 $ACHV first!"); e.preventDefault();}} }};
</script>
</body>
</html>
"""

@app.route('/')
def home():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML, files=files)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('video')
    if f: f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
    return '<script>window.location="/"</script>'

@app.route('/download/<name>')
def download(name): return send_from_directory(UPLOAD_FOLDER, name, as_attachment=True)

@app.route('/delete/<name>')
def delete_file(name):
    p=os.path.join(UPLOAD_FOLDER,name)
    if os.path.exists(p): os.remove(p)
    return '<script>window.location="/"</script>'

@app.route('/logo-192.png')
def l1(): return send_from_directory('.', 'logo-192.png')

@app.route('/logo-512.png')
def l2(): return send_from_directory('.', 'logo-512.png')

if __name__ == '__main__': app.run(host='0.0.0.0', port=10000)
