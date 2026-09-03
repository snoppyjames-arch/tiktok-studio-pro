import telebot
import requests
import os
import time
import urllib.parse
import random
# Modernized moviepy import compatibility for 2026 (v2.x+)
from moviepy import ImageSequenceClip

BOT_TOKEN = "8862760861:AAGQkVyMDXBa8-_zXXNPLJcepLtUqpDgMGI"
bot = telebot.TeleBot(BOT_TOKEN)

# TikTok viral hashtags
HASHTAGS = "#tiktok #viral #fyp #foryou #hd #4k #aesthetic #luxury #motivation #trending"

def get_hd_image(prompt, seed=None):
    q = urllib.parse.quote(f"{prompt}, ultra detailed 8k, sharp focus, cinematic lighting, vertical 9:16, masterpiece")
    s = seed or random.randint(1, 9999999)
    url = f"https://image.pollinations.ai/prompt/{q}?width=1080&height=1920&nologo=true&enhance=true&model=flux&seed={s}"
    r = requests.get(url, timeout=120)
    return r.content

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, """🎬 TikTok Studio PRO - MONEY BOT READY! 💰
🖼️ /pic [idea] - 4K HD Pic
🎥 /video [idea] 40s - 40s Video
🎥 /video [idea] 60s - 60s Video
COMMANDS:🎥 /video [idea] 90s - 90s Video
💰 /niche luxury - Luxury viral prompts
💰 /niche motivation - Motivation prompts
💰 /niche business - Business prompts
MONEY COMMANDS:💵 /income - How to make money today

Just type: /pic a billionaire villa Dubai 4k
Or: /video supercar driving Dubai 60s
""")

@bot.message_handler(commands=['income'])
def income(m):
    bot.reply_to(m, """💰 HOW THIS BOT MAKES YOU $500+/MONTH:
1️⃣ TikTok Page: Post 1 bot video daily -> 10k followers in 14 days -> Sell account $200 or get Creator Fund
2️⃣ Sell Content: /pic luxury house -> Sell on Shutterstock/Freepik ($2 per download)
3️⃣ Service: Charge shops $50/month for 30 TikTok videos. Bot does it in 30 mins!
4️⃣ YouTube Shorts: Same videos -> YouTube pays $3/1000 views

START NOW: Create TikTok account 'LuxuryMotivationHD' and run /video 10x
""")

@bot.message_handler(commands=['niche'])
def niche(m):
    txt = m.text.lower()
    if "luxury" in txt:
        prompts = ["Dubai penthouse view at sunset 4k", "private jet interior luxury 4k", "supercar collection garage 4k", "billionaire morning routine 4k", "yacht party Monaco 4k"]
    elif "motivation" in txt:
        prompts = ["lion king mountain motivation 4k", "gym discipline hard work 4k", "money rain luxury mindset 4k", "never give up quote background 4k", "success is lonely road 4k"]
    else:
        prompts = ["restaurant food plating 4k", "barber shop fade 4k", "makeup transformation 4k", "clothing brand model 4k", "real estate house tour 4k"]
    
    msg = "🔥 VIRAL PROMPTS FOR YOU (Copy & use /pic or /video):\n\n" + "\n".join([f"{i+1}. {p}" for i, p in enumerate(prompts)])
    bot.reply_to(m, msg)

@bot.message_handler(commands=['pic', 'p', 'hdpic'])
def gen_pic(m):
    prompt = m.text.split(' ', 1)[1] if ' ' in m.text else ""
    if not prompt:
        bot.reply_to(m, "❌ Type: /pic a luxury villa Dubai sunset 4k")
        return
    
    bot.reply_to(m, f"🎨 Generating 4K HD: {prompt}...")
    try:
        img_data = get_hd_image(prompt)
        caption = f"✅ 4K HD READY FOR TIKTOK\n\nPrompt: {prompt}\n\n{HASHTAGS}\n\n💡 Sell this on Shutterstock/Freepik!"
        bot.send_photo(m.chat.id, img_data, caption=caption)
    except Exception as e:
        bot.reply_to(m, f"Error, try again: {e}")

@bot.message_handler(commands=['video', 'v', 'tiktok', 'clip'])
def gen_video(m):
    raw = m.text.split(' ', 1)[1] if ' ' in m.text else ""
    if not raw:
        bot.reply_to(m, "❌ Type: /video a lion roaring mountain 40s")
        return

    duration = 40
    if "120s" in raw: duration = 120
    elif "90s" in raw: duration = 90
    elif "60s" in raw: duration = 60
    
    prompt = raw.replace("40s", "").replace("60s", "").replace("90s", "").replace("120s", "").strip()
    bot.reply_to(m, f"🎬 MONEY VIDEO STARTED\n\nIdea: {prompt}\nDuration: {duration}s\nScenes: {duration//5}\n\nGenerating HD scenes... Please wait 2-3 mins ⏳")
    
    try:
        paths = []
        # Ensure temporary folder context exists safely across environments
        os.makedirs("/tmp", exist_ok=True)
        
        for i in range(duration // 5):
            scene_prompt = f"{prompt}, cinematic scene {i+1}, dynamic angle, 4k, story sequence"
            img_data = get_hd_image(scene_prompt, seed=int(time.time()) + i * 123)
            p = f"/tmp/scene_{m.chat.id}_{i}.jpg"
            with open(p, 'wb') as f:
                f.write(img_data)
            paths.append(p)
            time.sleep(1)
            
        out = f"/tmp/final_{m.chat.id}.mp4"
        clip = ImageSequenceClip(paths, fps=1/5).with_duration(duration) # Updated method for modern MoviePy versions
        clip.write_videofile(out, fps=24, codec='libx264', audio=False, logger=None)

        caption = f"✅ *{duration}s VIRAL TIKTOK VIDEO DONE*\n\nIdea: {prompt}\n\nTikTok Caption:\n{prompt} 🔥💰\n\n{HASHTAGS}\n\n💵 Post this NOW on TikTok & YouTube Shorts!"
        
        with open(out, 'rb') as video_file:
            bot.send_video(m.chat.id, video_file, caption=caption, supports_streaming=True)

        # Cleanup files
        for p in paths: 
            if os.path.exists(p): os.remove(p)
        if os.path.exists(out): os.remove(out)

    except Exception as e:
        bot.reply_to(m, f"⚠️ Video merge failed (moviepy). Sending as HD photo sequence:\nError: {e}")
        for i in range(min(5, duration // 5)):
            img_data = get_hd_image(f"{prompt} scene {i}", seed=i)
            bot.send_photo(m.chat.id, img_data)

print("TikTok Studio Pro Money Bot Running...")
bot.infinity_polling()
