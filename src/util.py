import pyxel as px
import json


h_texts = " 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ /+-:*#()[]"
z_texts = "　１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ　／＋－：＊＃（）［］"
h2z = str.maketrans(h_texts, z_texts)
z2h = str.maketrans(z_texts, h_texts)


# JSONロード
def load_json(file):
    with open("./" + file + ".json", "r") as fin:
        return json.loads(fin.read())


# 「ピッ」音
def beep():
    if px.play_pos(3) is None:
        px.play(3, 6)


# キャラクタ表示
def draw_member(x, y, member, motion=0):
    u, v = member.img
    if member.health == 4:
        px.blt(x, y + 8, 1, u, v, 24, 16, 0)
    else:
        px.blt(x, y, 1, u + motion * 16, v, 16, 24, 0)


# ジョブイメージの座標
def job_uv(job, pat):
    u = job // 4 * 128 + pat * 16
    v = job % 4 * 24 + 128
    return u, v


# ループ計算
def loop(target, dist, length, min_val=0):
    if dist is None:
        return target
    value = target + dist if target else dist
    if value >= length + min_val:
        value -= length
    if value < min_val:
        value += length
    return value


# 範囲内に抑える
def maxmin(target, max_val, min_val=0):
    return max(min(target, max_val), min_val)


# 乱数計算
def rnd_value(intensity):
    val = 0
    for _ in range(intensity):
        val += px.rndi(3, 6)
    return val


# 全角化
def zen(val):
    return str(val).translate(h2z)


# パディング左よせ
def spacing(val, length):
    return str(val).ljust(length).translate(h2z)[-length:]


# パディング右よせ
def pad(val, length, fill=" "):
    return str(val).rjust(length, fill).translate(h2z)[-length:]


# プレイ時間取得
def play_time(frames, with_seconds=False):
    seconds = frames // 30
    minutes = (seconds // 60) % 60
    hours = min(seconds // 3600, 99)
    seconds = seconds % 60
    if with_seconds:
        return f"{pad(hours,2,'0')}：{pad(minutes,2,'0')}：{pad(seconds,2,'0')}"
    else:
        return f"{pad(hours,2,'0')}：{pad(minutes,2,'0')}"
