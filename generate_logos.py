import os

os.makedirs("assets/clients", exist_ok=True)

logos = [
    ("indiatv", "INDIA", "TV", "#e31e24", "#0066b3"),
    ("santnirankari", "SANT", "NIRANKARI", "#1b4d9b", "#d4a017"),
    ("alok", "ALOK", "", "#f15a24", ""),
    ("primus", "PRIMUS", "HOSPITAL", "#0081c6", "#666"),
    ("adhyatm", "ADHYATM", "SADHNA", "#8b2024", "#cc9933"),
    ("godrej", "Godrej", "", "#6d2077", ""),
    ("apex", "APEX", "BUILDTECH", "#1a4c81", "#888"),
    ("industrialfoams", "INDUSTRIAL", "FOAMS", "#f59e0b", "#333"),
    ("conscient", "CONSCIENT", "SPORTS", "#10b981", "#333"),
    ("91springboard", "91", "SPRINGBOARD", "#ef4444", "#333"),
    ("pardesi", "PARDESI", "GROUP", "#d4a017", "#333"),
    ("m3m", "M3M", "", "#0f4c81", ""),
    ("centralpark", "CENTRAL", "PARK", "#2563eb", "#0ea5e9"),
    ("tdi", "TDI", "RISE ABOVE", "#0ea5e9", "#333"),
    ("aaj", "AAJ", "", "#dc2626", ""),
    ("shivnadar", "SHIV NADAR", "SCHOOL", "#0d9488", "#333"),
    ("gmada", "GMADA", "", "#ea580c", ""),
    ("emaar", "EMAAR", "", "#c5a059", ""),
    ("monsoon", "MONSOON", "SALON &amp; SPA", "#db2777", "#666"),
    ("motherson", "motherson", "", "#0f172a", ""),
    ("parkash", "PARKASH", "AMUSEMENTS", "#4f46e5", "#666"),
    ("diviniti", "DIVINITI", "", "#0891b2", ""),
    ("m2k", "M2K", "GROUP", "#0f4c81", "#888"),
    ("cipl", "CIPL", "ISO 9001:2008", "#1e293b", "#888"),
    ("veta", "VETA", "HOTEL &amp; BANQUETS", "#854d0e", "#666"),
    ("karan", "KARAN", "LETEX LTD", "#3b82f6", "#666"),
    ("4s", "4S", "WE BUILD THE BEST", "#10b981", "#666"),
    ("heritage", "THE HERITAGE", "SCHOOL", "#4338ca", "#666"),
    ("hero", "HERO", "", "#ef4444", ""),
    ("jindal", "O P JINDAL", "UNIVERSITY", "#0f4c81", "#888"),
]

for item in logos:
    fname = item[0]
    line1 = item[1]
    line2 = item[2]
    color1 = item[3]
    color2 = item[4]

    if line2:
        # Two-line logo
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 70">
  <rect width="220" height="70" fill="white" rx="6"/>
  <text x="110" y="32" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="900" font-size="22" fill="{color1}" letter-spacing="2">{line1}</text>
  <text x="110" y="52" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="600" font-size="12" fill="{color2}" letter-spacing="3">{line2}</text>
  <line x1="40" y1="60" x2="180" y2="60" stroke="{color1}" stroke-width="1.5" opacity="0.3"/>
</svg>'''
    else:
        # Single-line bold logo
        size = "36" if len(line1) <= 5 else "26" if len(line1) <= 8 else "20"
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 70">
  <rect width="220" height="70" fill="white" rx="6"/>
  <text x="110" y="46" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="{size}" fill="{color1}" letter-spacing="3">{line1}</text>
  <line x1="60" y1="56" x2="160" y2="56" stroke="{color1}" stroke-width="2" opacity="0.25"/>
</svg>'''

    with open(f"assets/clients/{fname}.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Created: assets/clients/{fname}.svg")

print(f"\nDone! Created {len(logos)} logo SVG files.")
