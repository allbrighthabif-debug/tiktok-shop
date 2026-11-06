#!/usr/bin/env python3
"""Sample the bag's colors from a product image.

Usage: python3 tools/sample_color.py image.png [--box x1,y1,x2,y2]
--box is optional, fractions of width/height (e.g. 0.2,0.1,0.8,0.9) to crop to the bag.
Prints the main color, the shadow and the highlight as HEX with the nearest color name.
Works best on a white-background image; busy backgrounds or big prints make it unreliable.
"""
import sys
from PIL import Image

NAMES = {
    "black": (20, 20, 22), "charcoal": (54, 57, 61), "grey": (128, 128, 128), "light grey": (200, 200, 200),
    "white": (245, 245, 242), "ivory": (247, 242, 231), "cream": (242, 234, 217), "oatmeal": (217, 207, 192),
    "beige": (214, 196, 168), "sand": (194, 178, 128), "khaki": (176, 160, 120), "taupe": (136, 119, 112),
    "camel": (193, 154, 107), "tan": (190, 150, 110), "caramel": (198, 139, 78), "cognac": (154, 70, 30),
    "rust": (160, 72, 40), "chocolate brown": (90, 58, 46), "espresso brown": (46, 27, 16),
    "coffee brown": (74, 44, 26), "dark chocolate": (61, 43, 38), "charcoal brown": (62, 54, 50),
    "warm grey": (150, 140, 130), "greige": (180, 170, 155), "mocha": (164, 120, 100), "burgundy": (100, 20, 35), "wine red": (114, 33, 45),
    "cherry red": (180, 20, 35), "red": (205, 30, 40), "coral": (240, 120, 100), "orange": (235, 120, 30),
    "mustard": (205, 160, 40), "yellow": (240, 210, 60), "butter yellow": (245, 228, 150),
    "olive": (110, 110, 50), "forest green": (46, 74, 52), "sage": (160, 175, 140), "emerald": (20, 120, 80),
    "navy": (35, 54, 86), "cobalt blue": (30, 70, 170), "sky blue": (140, 190, 230), "baby blue": (190, 215, 240),
    "lavender": (190, 170, 220), "purple": (110, 50, 140), "plum": (90, 40, 70), "hot pink": (230, 50, 140),
    "pink": (240, 140, 180), "blush pink": (240, 200, 200), "dusty rose": (200, 140, 140),
    "silver": (190, 192, 195), "gold": (200, 160, 70),
}


def to_lab(rgb):
    def lin(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(v) for v in rgb)
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def nearest(rgb):
    l1 = to_lab(rgb)
    return min(NAMES, key=lambda n: sum((p - q) ** 2 for p, q in zip(l1, to_lab(NAMES[n]))))


def hexc(rgb):
    return "#%02X%02X%02X" % tuple(int(round(v)) for v in rgb)


def kmeans(px, k=5, rounds=12):
    px = sorted(px, key=sum)
    centers = [px[int(i * (len(px) - 1) / (k - 1))] for i in range(k)]
    for _ in range(rounds):
        groups = [[] for _ in centers]
        for p in px:
            i = min(range(len(centers)), key=lambda j: sum((a - b) ** 2 for a, b in zip(p, centers[j])))
            groups[i].append(p)
        centers = [tuple(sum(c) / len(g) for c in zip(*g)) if g else centers[i] for i, g in enumerate(groups)]
    return [(c, len(g)) for c, g in zip(centers, groups) if g]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    img = Image.open(argv[1]).convert("RGB")
    w, h = img.size
    if "--box" in argv:
        x1, y1, x2, y2 = (float(v) for v in argv[argv.index("--box") + 1].split(","))
        img = img.crop((int(x1 * w), int(y1 * h), int(x2 * w), int(y2 * h)))
    img.thumbnail((160, 160))
    px = list(img.get_flattened_data()) if hasattr(img, "get_flattened_data") else list(img.getdata())
    def bg(p):  # white background and its soft grey shadow
        l, a, b = to_lab(p)
        return l > 74 and (a * a + b * b) ** 0.5 < 9
    keep = [p for p in px if not bg(p)]
    share = len(keep) / max(len(px), 1)
    if len(keep) < 50:
        print("取不到颜色:图里几乎全是白色。用 --box 框住包再试。")
        return 1
    clusters = kmeans(keep)
    total = sum(n for _, n in clusters)
    big = [(c, n) for c, n in clusters if n / total >= 0.06]
    main_c = max(big, key=lambda t: t[1])[0]
    dark = min(big, key=lambda t: sum(t[0]))[0]
    lm = to_lab(main_c)
    near = [t for t in big if sum((p - q) ** 2 for p, q in zip(to_lab(t[0]), lm)) ** 0.5 < 45]
    light = max(near, key=lambda t: sum(t[0]))[0]
    print(f"主色:{nearest(main_c)} {hexc(main_c)}")
    print(f"暗部:{nearest(dark)} {hexc(dark)}")
    print(f"受光处:{nearest(light)} {hexc(light)}")
    print("各块占比:" + ",".join(f"{hexc(c)} {n / total:.0%}" for c, n in sorted(clusters, key=lambda t: -t[1])))
    l_main = to_lab(main_c)
    spread = max(abs(to_lab(c)[1] - l_main[1]) + abs(to_lab(c)[2] - l_main[2]) for c, _ in big)
    if share > 0.9:
        print("提醒:背景不是白色,取到的颜色可能混进了背景;用 --box 只框住包,或换白底图。")
    if spread > 40:
        print("提醒:包上颜色差得很多(可能有花纹、拼色或背景),这几个颜色只作参考,按眼睛看的核一遍。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
