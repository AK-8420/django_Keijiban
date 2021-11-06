from django.utils import timezone
from .models import Thread, Post
import hashlib

class get_ipID:
    def hashing(ip):
        date = timezone.localdate(timezone.now())#現在の日付
        secret = "Omoti_Daisuki_himitu_dayo" #秘密の文字列
        #ハッシュ計算
        dat = str(ip) + str(date) + secret
        hs = hashlib.md5(dat.encode()).hexdigest()
        ipID = hs[1:9] #8文字取得
        return ipID