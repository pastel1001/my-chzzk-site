import json
import urllib.request
import os
from flask import Flask, render_template

app = Flask(__name__)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

CHANNEL_IDS = [
    "b5ed5db484d04faf4d150aedd362f34b",
    "45e71a76e949e16a34764deb962f9d9f",
    "36ddb9bb4f17593b60f1b63cec86611d",
    "a6c4ddb09cdb160478996007bff35296",
    "4325b1d5bbc321fad3042306646e2e50",
    "b044e3a3b9259246bc92e863e7d3f3b8",
    "4515b179f86b67b4981e16190817c580",
    "64d76089fba26b180d9c9e48a32600d9",
    "8fd39bb8de623317de90654718638b10",
    "516937b5f85cbf2249ce31b0ad046b0f",
    "4d812b586ff63f8a2946e64fa860bbf5"
]

def get_data(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

@app.route('/')
def home():
    streamers = []
    for cid in CHANNEL_IDS:
        ch_info = get_data(f"https://api.chzzk.naver.com/service/v1/channels/{cid}")
        if not ch_info or not ch_info.get('content'):
            continue
        
        name = ch_info['content']['channelName']
        is_live = ch_info['content']['openLive']
        
        live_data = {}
        if is_live:
            detail = get_data(f"https://api.chzzk.naver.com/service/v2/channels/{cid}/live-detail")
            if detail and detail.get('content'):
                c = detail['content']
                live_data = {
                    'title': c.get('liveTitle', '제목 없음'),
                    'users': c.get('concurrentUserCount', 0),
                    'category': c.get('liveCategoryValue', '일반')
                }
        
        streamers.append({
            'id': cid,
            'name': name,
            'is_live': is_live,
            'live': live_data
        })
        
    return render_template('index.html', streamers=streamers)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
