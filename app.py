from flask import Flask, render_template_string
from datetime import datetime
app = Flask(__name__)

HTML = """
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-black text-white min-h-screen p-4">
<div class="max-w-lg mx-auto">
<div class="bg-zinc-900 rounded-[30px] p-7 border border-zinc-800">
<h1 class="text-3xl font-black">TikTok Studio Pro</h1>
<p class="bg-pink-600 inline-block px-3 py-1 rounded-full text-xs font-black mt-2">SUPER FREE - ALL IN ONE</p>

<input id="idea" class="w-full mt-6 p-4 rounded-2xl text-black font-bold text-lg" placeholder="Type your idea: e.g. makeup, football, ndole">

<button onclick="generate()" class="w-full mt-4 bg-white text-black p-4 rounded-2xl font-black text-lg">🚀 Generate 6 in 1 - FREE</button>

<div id="result" class="mt-6 hidden space-y-4">

<div class="bg-zinc-800 p-4 rounded-2xl"><p class="text-pink-400 text-xs font-bold">1. VIRAL IDEA</p><p id="o1" class="mt-1 font-bold"></p></div>

<div class="bg-zinc-800 p-4 rounded-2xl"><p class="text-yellow-400 text-xs font-bold">2. HOOK (First 3 seconds)</p><p id="o2" class="mt-1 font-black text-lg"></p></div>

<div class="bg-zinc-800 p-4 rounded-2xl"><p class="text-green-400 text-xs font-bold">3. FULL SCRIPT (30 sec)</p><p id="o3" class="mt-1 text-sm leading-6"></p></div>

<div class="bg-zinc-800 p-4 rounded-2xl"><p class="text-blue-400 text-xs font-bold">4. HASHTAGS</p><p id="o4" class="mt-1 text-sm"></p></div>

<div class="bg-zinc-800 p-4 rounded-2xl"><p class="text-purple-400 text-xs font-bold">5. BEST TIME TO POST (Yaounde)</p><p id="o5" class="mt-1 font-bold"></p></div>

<div class="bg-zinc-800 p-4 rounded-2xl"><p class="text-orange-400 text-xs font-bold">6. CAPTION READY</p><p id="o6" class="mt-1 text-sm"></p></div>

</div>

<p class="text-center text-zinc-500 text-[10px] mt-6">FREE BETA - Made in Yaounde 🇨🇲</p>
</div>
</div>

<script>
function generate(){
let topic = document.getElementById('idea').value;
if(!topic){ alert('Type idea first!'); return; }
document.getElementById('result').classList.remove('hidden');

document.getElementById('o1').innerText = `3 ${topic} mistakes you must stop today (Part ${Math.floor(Math.random()*3)+1})`;
document.getElementById('o2').innerText = `STOP! Don't post about ${topic} before watching this!`;
document.getElementById('o3').innerHTML = `[0-3s] HOOK: Stop scrolling!<br>[3-8s] PROBLEM: 90% people fail at ${topic} because they do this...<br>[8-20s] SOLUTION: Do this instead: 1. Show result 2. Show how 3. Show proof<br>[20-30s] CTA: Follow for Part 2 + Comment "${topic}"`;
document.getElementById('o4').innerText = `#${topic.replace(/ /g,'')} #fyp #viral #cameroon #yaounde #tiktokgrowth #${topic.replace(/ /g,'')}tips`;
document.getElementById('o5').innerText = `Today 7:00 PM - 9:30 PM (Yaounde time) - Best time, people are online`;
document.getElementById('o6').innerText = `I tried ${topic} for 7 days and this happened 😳 Full secret in video 👆 #${topic.replace(/ /g,'')} Follow for more!`;
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)