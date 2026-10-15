#!/usr/bin/env python3
"""Draw the small pictures for the memory aids (flat SVG, own parchment
panel so they read in light and dark pages).

    python3 tools/make_aid_images.py images/aids
"""
import sys
from pathlib import Path

BG, INK, MUTED, TEAL, ACC = "#fffdf8", "#2a2118", "#7a6c5a", "#2f6f6a", "#a4400f"
FONT = "'Noto Sans Devanagari','Mukta','Nirmala UI','Mangal',sans-serif"
W, H = 360, 200


def svg(body, title, height=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} '
            f'{height}" role="img"><title>{title}</title>'
            f'<rect width="{W}" height="{height}" rx="14" fill="{BG}" '
            f'stroke="#e4d9c6"/>' + body + '</svg>')


def text(x, y, s, size=13, fill=INK, anchor="middle", weight=500):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">'
            f'{s}</text>')


def arrow(x1, y1, x2, y2, color=TEAL):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="2.5" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {x2 - 8},{y2 - 5} {x2 - 8},{y2 + 5}" '
            f'fill="{color}"/>')


def quote():
    return svg(
        f'<text x="180" y="150" font-family="Georgia,serif" font-size="150" '
        f'fill="{ACC}" text-anchor="middle">&#8221;</text>'
        + text(180, 30, "इति = उद्धरण बन्द", 15, TEAL, weight=700)
        + text(180, 182, "ऊपर की सारी बात आत्रेय की", 13, MUTED),
        "closing quotation mark")


def rope_vajra_umbrella():
    rope = (f'<path d="M30 115 C50 65 70 165 90 105 S120 65 110 125 '
            f'S70 145 55 95" fill="none" stroke="{ACC}" stroke-width="5" '
            f'stroke-linecap="round"/>')
    bolt = (f'<polygon points="190,50 165,105 183,105 170,150 210,92 191,92 '
            f'206,50" fill="{TEAL}"/>')
    umb = (f'<path d="M262 100 A45 45 0 0 1 352 100 Z" fill="{ACC}"/>'
           f'<line x1="307" y1="100" x2="307" y2="150" stroke="{INK}" '
           f'stroke-width="3"/>'
           f'<path d="M307 150 q0 12 -10 10" fill="none" stroke="{INK}" '
           f'stroke-width="3" stroke-linecap="round"/>')
    return svg(rope + bolt + umb
               + text(70, 185, "दीर्घ (लम्बी रस्सी)", 12)
               + text(188, 185, "इन्द्र (वज्र)", 12)
               + text(307, 185, "शरण्य (छतरी)", 12)
               + text(180, 28, "दीर्घ → इन्द्र → शरण्य", 14, TEAL, weight=700),
               "a long rope, a thunderbolt and an umbrella")


def baton():
    xs = [60, 180, 300]
    names = ["ब्रह्मा", "प्रजापति", "अश्विनौ"]
    body = ""
    for x, n in zip(xs, names):
        body += (f'<circle cx="{x}" cy="95" r="30" fill="{BG}" '
                 f'stroke="{TEAL}" stroke-width="3"/>' + text(x, 100, n, 13)
                 )
    for a, b in ((92, 148), (212, 268)):
        body += arrow(a, 95, b, 95)
        body += (f'<rect x="{(a + b) // 2 - 14}" y="86" width="28" height="9" '
                 f'rx="4" fill="{ACC}"/>')
    body += text(180, 28, "रिले-दौड़: बैटन आगे बढ़ती है", 14, TEAL, weight=700)
    body += text(180, 165, "कहा → ग्रहण किया → उनसे लिया", 13, MUTED)
    return svg(body, "a relay baton passed along three runners")


def stairs():
    names = ["ब्रह्मा", "प्रजापति", "अश्विनौ", "शक्र", "भरद्वाज"]
    body = ""
    for i, n in enumerate(names):
        x, y = 18 + i * 64, 50 + i * 24
        body += (f'<rect x="{x}" y="{y}" width="62" height="{150 - y + 24}" '
                 f'fill="{TEAL if i < 4 else ACC}" opacity="{1 - i * 0.12}"/>'
                 + text(x + 31, y + 20, n, 12, BG, weight=700))
    body += text(180, 28, "ज्ञान सीढ़ी से उतरा", 14, TEAL, weight=700)
    return svg(body, "five steps going down from Brahma to Bharadvaja")


def stone():
    body = (f'<path d="M20 160 C100 110 130 190 200 140 S300 90 345 120" '
            f'fill="none" stroke="{MUTED}" stroke-width="22" '
            f'stroke-linecap="round" opacity="0.35"/>'
            f'<path d="M165 150 q-10 -45 25 -52 q35 -6 42 30 q4 22 -20 26 z" '
            f'fill="{ACC}"/>'
            + text(198, 90, "रोग = विघ्न", 13, ACC, weight=700)
            + text(180, 28, "रास्ते का पत्थर", 15, TEAL, weight=700)
            + text(180, 182, "तप · उपवास · अध्ययन · ब्रह्मचर्य · व्रत · आयु", 12,
                   MUTED))
    return svg(body, "a stone blocking a winding path")


def torch_slope():
    body = (f'<polygon points="30,170 190,45 340,170" fill="{TEAL}" '
            f'opacity="0.25"/>'
            f'<polygon points="95,170 190,100 280,170" fill="{TEAL}" '
            f'opacity="0.35"/>')
    for x, y in ((130, 150), (160, 150), (215, 150), (245, 150)):
        body += f'<circle cx="{x}" cy="{y}" r="6" fill="{INK}"/>'
    body += (f'<rect x="60" y="120" width="6" height="40" fill="{INK}"/>'
             f'<path d="M63 90 q-14 20 0 32 q14 -12 0 -32z" fill="{ACC}"/>'
             + text(80, 182, "करुणा (आगे)", 12, ACC, weight=700)
             + text(190, 38, "हिमालय का शुभ पार्श्व", 13, TEAL, weight=700)
             + text(190, 190, "महर्षि एकत्र हुए", 12, MUTED))
    return svg(body, "a torch held ahead of figures gathering on a slope")


def wrap(s, limit):
    out, line = [], ""
    for word in s.split(" "):
        if line and len(line) + 1 + len(word) > limit:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    out.append(line)
    return out


def mountain(top, bottom, title):
    tl = wrap(" · ".join(top), 30)
    bl = wrap(" · ".join(bottom), 40)
    height = 120 + 18 * (len(tl) + len(bl))
    body = (f'<polygon points="20,{height - 15} 180,24 340,{height - 15}" '
            f'fill="{TEAL}" opacity="0.18"/>')
    y = 66
    h1 = 18 * len(tl) + 10
    body += (f'<rect x="80" y="{y - 18}" width="200" height="{h1}" rx="8" '
             f'fill="{BG}" stroke="{TEAL}"/>')
    for line in tl:
        body += text(180, y, line, 12.5)
        y += 18
    y += 22
    h2 = 18 * len(bl) + 10
    body += (f'<rect x="34" y="{y - 18}" width="292" height="{h2}" rx="8" '
             f'fill="{BG}" stroke="{ACC}"/>')
    for line in bl:
        body += text(180, y, line, 12.5)
        y += 18
    body += text(180, 20, title, 13, TEAL, weight=700)
    return svg(body, "sages on two ledges of a mountain", height)


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    files = {
        "quote.svg": quote(), "rope-vajra-umbrella.svg": rope_vajra_umbrella(),
        "baton.svg": baton(), "stairs.svg": stairs(), "stone.svg": stone(),
        "torch-slope.svg": torch_slope(),
        "ledges-8.svg": mountain(
            ["अङ्गिरा", "जमदग्नि", "वसिष्ठ", "कश्यप", "भृगु"],
            ["आत्रेय", "गौतम", "साङ्ख्य", "पुलस्त्य", "नारद", "असित"],
            "श्लोक ८"),
        "ledges-9.svg": mountain(
            ["अगस्त्य", "वामदेव", "मार्कण्डेय–आश्वलायन"],
            ["पारिक्षि", "भिक्षु आत्रेय", "भरद्वाज", "कपिञ्जल"], "श्लोक ९"),
        "ledges-10.svg": mountain(
            ["विश्वामित्र–आश्मरथ्य", "भार्गव च्यवन", "अभिजित्"],
            ["गार्ग्य", "शाण्डिल्य–कौण्डिल्य", "वार्क्षि", "देवल–गालव"],
            "श्लोक १०"),
    }
    for name, markup in files.items():
        (out / name).write_text(markup, encoding="utf8")
    print(len(files), "images in", out)


if __name__ == "__main__":
    main()
