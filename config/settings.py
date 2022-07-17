import os
# ALLOWED_HOSTS = []を以下のようにして、vercel.appでも開けるようにする
ALLOWED_HOSTS = [
    '*',
    '.vercel.app'
]

# LANGUAGE_CODEとTIME_ZONEを以下のように変更して日本語表示にする
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
DATABASES = {}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')