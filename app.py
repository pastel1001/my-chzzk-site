import json
import urllib.request

# 1. 조회하고 싶은 스트리머 채널 ID 목록
channel_ids = [
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

# 차단 방지용 헤더
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_channel_info(channel_id):
    """채널 ID를 입력받아 치지직 방송 상태 및 정보를 출력하는 함수"""
    url = f"https://api.chzzk.naver.com/service/v1/channels/{channel_id}"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            channel_info = data['content']
            channel_name = channel_info['channelName']
            follower_count = channel_info['followerCount']
            open_live = channel_info['openLive']

            print("\n" + "=" * 35)
            print(f"🟢 스트리머: {channel_name}")
            print(f"👥 팔로워 수: {follower_count:,}명")
            
            if open_live:
                print("🔴 현재 방송 상태: [생방송 중 (LIVE)]")
            else:
                print("⚪️ 현재 방송 상태: [방송 꺼짐 (OFF)]")
            print("=" * 35)

    except Exception as e:
        print(f"\n[ID: {channel_id}] 채널 정보를 가져오는 데 실패했습니다.")
        print(f"오류 내용: {e}")

# 2. 반복문을 통해 등록된 모든 채널 조회
print("🚀 치지직 스트리머 방송 상태 조회를 시작합니다...")
for cid in channel_ids:
    get_channel_info(cid)