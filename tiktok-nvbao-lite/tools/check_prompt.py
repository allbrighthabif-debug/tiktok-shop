#!/usr/bin/env python3
"""Check a Seedance prompt before delivery.

Usage: python3 tools/check_prompt.py prompt.txt
Prints the self-check line and a list of problems.
Exit code 1 when there is an error that must be fixed.
"""
import re
import sys

LIMIT_CHARS = 5000
LIMIT_RATE = 3.8

BANNED = [
    ("柔和的阳光", "太阳写成柔和会出阴天的平光,改成直接照在她身上"),
    ("阳光柔和", "太阳写成柔和会出阴天的平光"),
    ("半边脸", "不写半边脸在阴影里,只写阴影一侧不发黑"),
    ("屋里比她暗", "房间本身要亮"),
    ("曝光充足", "结果词没用,写光落在哪几处"),
    ("特写", "不写特写,写拍摄者凑近"),
    ("推近", "不写推近,写拍摄者走过去凑近"),
    ("近景", "不写近景,写拍摄者凑近"),
    ("低头", "看包写垂眼,不写低头"),
    ("——", "不用破折号"),
    ("—", "不用破折号"),
    ("link in bio", "不说 link in bio"),
    ("% off", "不说折扣"),
]
PRICE = re.compile(r"\$\s?\d|\d+\s*(美元|刀|dollars?|bucks)", re.I)

SEG = re.compile(r"【\s*(\d+(?:\.\d+)?)\s*[-–~]\s*(\d+(?:\.\d+)?)\s*秒\s*[|｜]?([^】]*)】")
BLOCK = re.compile(r"^【[^】\d]*】", re.M)
QUOTE = re.compile(r"[\"“]([^\"”]+)[\"”]")
WORD = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")

TOUCH_VERBS = ["握住", "握着", "提起", "往身前提", "拎起", "按一下", "按了", "按下", "轻轻按", "抹过", "抹过去",
               "托起", "托着", "点一下", "拉开", "拉上", "拉链头", "挎上", "摸了", "摸一下", "捏住", "掀开",
               "松开提手", "放进", "掏出"]
CAM = ["画面跟着", "画面往", "镜头往", "往前凑近", "凑近", "退回", "往后一漂", "往下带", "往上抬", "画面回到"]


def main(path):
    text = open(path, encoding="utf-8").read().strip()
    errors, warns = [], []

    # total length
    n_chars = len(text)
    if n_chars > LIMIT_CHARS:
        errors.append(f"总字数 {n_chars},超过 {LIMIT_CHARS},先删重复的")

    # headline
    first = text.splitlines()[0] if text else ""
    m = re.search(r"(\d+(?:\.\d+)?)\s*秒", first)
    total = float(m.group(1)) if m else None
    multi_scene = "硬切" in text or "个场景" in first
    if not multi_scene and "一镜到底" not in first:
        errors.append("第一行没有总述\"N 秒一镜到底(……)\"")
    if not multi_scene:
        if "同一个连续镜头" not in text:
            errors.append("【时间轴】开头缺\"下面是同一个连续镜头里的时间段……\"")
        if "禁止快速剪辑" not in text:
            errors.append("【约束】缺\"禁止快速剪辑\"")

    # required pieces
    bag = re.search(r"【包】(.*?)(?=^【[^】\d]*】)", text, re.S | re.M)
    if bag:
        b = bag.group(1)
        if "大小" not in b or not re.search(r"\d+\s*(cm|厘米)", b):
            errors.append("【包】缺大小:实际尺寸 cm + 身体比 + 背上落点")
    else:
        warns.append("没找到【包】这一块")
    if "HDR" not in text:
        warns.append("【整体】没写\"iPhone 默认 HDR 拍的,暗部有细节\"")

    # banned words
    for word, why in BANNED:
        if word in text:
            errors.append(f"有禁用词\"{word}\":{why}")
    if PRICE.search(text):
        errors.append("有价格数字,台词和提示词不说具体价格")

    # segments
    segs = list(SEG.finditer(text))
    max_rate, max_touch, max_cam = 0.0, 0, 0
    if not segs:
        errors.append("没找到时间段标题,格式是【0-2 秒|这段在干嘛】")
    prev_end = 0.0
    for i, s in enumerate(segs):
        a, b, title = float(s.group(1)), float(s.group(2)), s.group(3).strip()
        label = f"{s.group(1)}-{s.group(2)} 秒"
        if abs(a - prev_end) > 0.05:
            errors.append(f"{label}:和上一段没接上(上一段结束在 {prev_end:g} 秒)")
        prev_end = b
        dur = b - a
        start = s.end()
        stop = segs[i + 1].start() if i + 1 < len(segs) else len(text)
        nxt = BLOCK.search(text, start)
        if nxt and nxt.start() < stop:
            stop = nxt.start()
        body = text[start:stop]
        words = sum(len(WORD.findall(q)) for q in QUOTE.findall(body))
        if dur <= 0:
            errors.append(f"{label}:时长不对")
            continue
        rate = words / dur
        max_rate = max(max_rate, rate)
        if rate > LIMIT_RATE:
            errors.append(f"{label}:{words} 词 / {dur:g} 秒 = 每秒 {rate:.1f} 词,超过 {LIMIT_RATE}")
        clauses = [c for c in re.split(r"[;;。\n]", body) if c.strip()]
        touch = sum(1 for c in clauses if any(v in c for v in TOUCH_VERBS))
        cam = sum(1 for c in clauses if any(k in c for k in CAM))
        max_touch, max_cam = max(max_touch, touch), max(max_cam, cam)
        if touch > 1:
            warns.append(f"{label}:可能有 {touch} 个碰包动作,人工确认一段只有一个")
        if cam > 1:
            warns.append(f"{label}:可能有 {cam} 个镜头动作,人工确认一段只有一个连续动作")
    if segs and total is not None and abs(prev_end - total) > 0.05:
        errors.append(f"最后一段结束在 {prev_end:g} 秒,第一行写的是 {total:g} 秒")

    print(f"自查:最快一段 {max_rate:.1f} 词/秒(上限 {LIMIT_RATE})|每段碰包最多 {max_touch} 个|"
          f"每段镜头动作最多 {max_cam} 个|共 {n_chars} 字(上限 {LIMIT_CHARS})")
    for e in errors:
        print("错误:" + e)
    for w in warns:
        print("提醒:" + w)
    if not errors and not warns:
        print("没有发现问题")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
