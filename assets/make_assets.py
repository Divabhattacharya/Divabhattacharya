"""Generates the SVG artwork for the profile README (header, project cards, extra stack icons).

    python3 assets/make_assets.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
BG0, BG1, BORDER = "#0d1117", "#161b22", "#30363d"
TEXT, MUTED = "#e6edf3", "#8b949e"
GREEN, BLUE, PURPLE, KAGGLE, SILVER = "#76b900", "#58a6ff", "#bc8cff", "#20beff", "#c0c0c0"


def header():
    lanes = []
    x0, y0, s, gap = 800, 70, 34, 10
    for lane in range(32):
        r, c = divmod(lane, 8)
        x, y = x0 + c * (s + gap), y0 + r * (s + gap)
        delay = (c + r) * 0.09
        lanes.append(
            f'<rect class="lane" x="{x}" y="{y}" width="{s}" height="{s}" rx="7" style="animation-delay:{delay:.2f}s"/>'
            f'<text x="{x + s / 2}" y="{y + s / 2 + 4}" class="lid">{lane}</text>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG0}"/></linearGradient>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#ffffff" stroke-opacity="0.035"/></pattern>
  <radialGradient id="glow" cx="0.78" cy="0.45" r="0.45"><stop offset="0" stop-color="{GREEN}" stop-opacity="0.16"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>
</defs>
<style>
  .lane {{ fill: {GREEN}; fill-opacity: .12; stroke: {GREEN}; stroke-opacity: .35; animation: wave 2.6s ease-in-out infinite; }}
  .lid {{ font: 600 11px {MONO}; fill: {TEXT}; fill-opacity: .55; text-anchor: middle; }}
  .cursor {{ animation: blink 1.1s step-end infinite; }}
  @keyframes wave {{ 0%, 100% {{ fill-opacity: .10; }} 35% {{ fill-opacity: .95; }} 60% {{ fill-opacity: .25; }} }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
</style>
<rect x="1" y="1" width="1198" height="298" rx="20" fill="url(#bg)" stroke="{BORDER}"/>
<rect x="1" y="1" width="1198" height="298" rx="20" fill="url(#grid)"/>
<rect x="1" y="1" width="1198" height="298" rx="20" fill="url(#glow)"/>
<text x="64" y="88" style="font: 500 17px {MONO}; fill: {GREEN};">$ whoami</text>
<text x="62" y="150" style="font: 700 54px {SANS}; fill: {TEXT}; letter-spacing: -0.5px;">Diva Bhattacharya</text>
<text x="64" y="192" style="font: 400 22px {SANS}; fill: {MUTED};">GPU compilers · CUDA · Machine learning</text>
<text x="64" y="244" style="font: 400 16px {MONO}; fill: {GREEN}; fill-opacity: .85;">shfl.sync.bfly.b32  %r1, %r0, 16, 31, -1;</text>
<rect class="cursor" x="462" y="230" width="10" height="18" fill="{GREEN}"/>
{''.join(lanes)}
<text x="1141" y="262" style="font: 400 13px {MONO}; fill: {MUTED}; text-anchor: end;">warp 0 · lanes 0–31</text>
</svg>
"""


def card(path, kicker, title, lines, tags, accent, badge=None):
    tag_svg, x = [], 28
    for t in tags:
        w = 16 + 7.6 * len(t)
        tag_svg.append(f'<rect x="{x}" y="160" width="{w:.0f}" height="26" rx="13" fill="{accent}" fill-opacity=".12" stroke="{accent}" stroke-opacity=".45"/>'
                       f'<text x="{x + w / 2:.0f}" y="177.5" style="font: 600 12.5px {SANS}; fill: {accent}; text-anchor: middle;">{escape(t)}</text>')
        x += w + 8
    body = "".join(f'<text x="28" y="{108 + 22 * i}" style="font: 400 15px {SANS}; fill: {MUTED};">{escape(l)}</text>'
                   for i, l in enumerate(lines))
    extra = ""
    if badge:
        w = 18 + 7.4 * len(badge)
        extra = (f'<rect x="{572 - w:.0f}" y="26" width="{w:.0f}" height="24" rx="12" fill="{badge_color(badge)}" fill-opacity=".14" stroke="{badge_color(badge)}" stroke-opacity=".6"/>'
                 f'<text x="{572 - w / 2:.0f}" y="42.5" style="font: 700 12px {SANS}; fill: {badge_color(badge)}; text-anchor: middle;">{escape(badge)}</text>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 210" width="600" height="210">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG0}"/></linearGradient></defs>
<rect x="1" y="1" width="598" height="208" rx="16" fill="url(#g)" stroke="{BORDER}"/>
<rect x="1" y="22" width="4" height="56" rx="2" fill="{accent}"/>
<text x="28" y="42" style="font: 700 12px {SANS}; fill: {accent}; letter-spacing: 1.6px;">{escape(kicker)}</text>
<text x="28" y="76" style="font: 700 25px {SANS}; fill: {TEXT};">{escape(title)}</text>
{body}
{''.join(tag_svg)}
{extra}
</svg>
"""
    (OUT / path).write_text(svg)


def badge_color(text):
    return SILVER if "SILVER" in text else MUTED


def icon(path, label, color, size=15):
    (OUT / path).write_text(f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="48" height="48">
<rect width="256" height="256" rx="60" fill="#242938"/>
<text x="128" y="{148 if size < 20 else 150}" style="font: 800 {size * 4}px {SANS}; fill: {color}; text-anchor: middle; letter-spacing: -2px;">{label}</text>
</svg>
""")


if __name__ == "__main__":
    (OUT / "header.svg").write_text(header())
    card("card-ptxsim.svg", "GPU · COMPILERS", "ptxsim",
         ["A PTX interpreter in C++ that drives differential fuzzing", "and Z3 translation validation of LLVM's NVPTX backend."],
         ["C++17", "LLVM", "Z3", "Fuzzing"], GREEN)
    card("card-cuda-compiler-verify.svg", "GPU · COMPILERS", "cuda-compiler-verify",
         ["CUDA test suite: 6 programs across 10 nvcc / ptxas", "configurations, checked against documented ULP bounds."],
         ["CUDA", "PTX", "Python", "A100"], GREEN)
    card("card-csiro.svg", "KAGGLE · COMPUTER VISION", "CSIRO Image2Biomass",
         ["Dual-stream DINOv3 with gated depthwise convolutions", "and auxiliary metadata for pasture biomass regression."],
         ["PyTorch", "DINOv3", "Regression"], KAGGLE, badge="SILVER MEDAL")
    card("card-protossm.svg", "ML · BIOACOUSTICS", "Pantanal ProtoSSM",
         ["Bird-call detection over 234 taxa for BirdCLEF+ 2026:", "Perch embeddings, ProtoSSM temporal model, OOF stacking."],
         ["TensorFlow", "PyTorch", "SSM"], PURPLE)
    card("card-neuroafrica.svg", "ML · MEDICAL IMAGING", "NeuroAfrica-3D",
         ["3D MRI glioma segmentation (WT / TC / ET) with", "Dice, NSD and HD95 tracking and fold-based training."],
         ["MONAI", "nnU-Net", "PyTorch"], BLUE)
    card("card-gossipppo.svg", "ML · DISTRIBUTED RL", "GossipPPO",
         ["Decentralized multi-agent RL with peer-to-peer gossip", "averaging and Byzantine-robust update filtering."],
         ["Ray", "PPO", "NetworkX"], BLUE)
    icon("icon-cuda.svg", "CUDA", GREEN, size=14)
    icon("icon-llvm.svg", "LLVM", "#e6edf3", size=14)
    icon("icon-ptx.svg", "PTX", GREEN, size=17)
    print("assets written")
