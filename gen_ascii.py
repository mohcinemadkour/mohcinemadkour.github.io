from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np

img = Image.open("assets/img/prof_pic.jpg").convert("L")
arr = np.array(img, dtype=np.float32)

# ── Background handling ───────────────────────────────────────────────────────
# The photo has a LIGHT gray background (~200-220 brightness)
# We want the background to map to SPACES (empty), face features to dense chars.
# Strategy: pixels lighter than threshold → clamp to white (255)
BG_THRESHOLD = 210  # pixels above this are background
arr = np.clip(arr, 0, 255)
# Clamp background to pure white
arr[arr > BG_THRESHOLD] = 255

# ── Contrast & sharpening on the face area ───────────────────────────────────
img2 = Image.fromarray(arr.astype(np.uint8))

# Stretch the non-background histogram
img2 = ImageOps.autocontrast(img2, cutoff=0)

# Contrast boost (moderate — not too aggressive)
img2 = ImageEnhance.Contrast(img2).enhance(2.5)

# Sharpen facial details
img2 = img2.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=2))

# ── ASCII grid dimensions ─────────────────────────────────────────────────────
target_cols = 100
# font-size:7px, line-height:1.1 -> h=7.7px, w≈7*0.6=4.2px -> ratio=0.545
CHAR_ASPECT = 0.545
img_aspect = img.height / img.width
target_rows = int(target_cols * img_aspect * CHAR_ASPECT)

img2 = img2.resize((target_cols, target_rows), Image.LANCZOS)

# ── Character mapping ─────────────────────────────────────────────────────────
# Light (bg/skin highlight) → space; Dark (hair/beard/shadow) → dense
chars = "  ..::;;!!||**##$$@@"

lines = []
for y in range(target_rows):
    row = ""
    for x in range(target_cols):
        pixel = img2.getpixel((x, y))
        idx = int(pixel / 255 * (len(chars) - 1))
        row += chars[idx]
    lines.append(row)

with open("_includes/prof_pic_ascii.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Done: {target_cols}x{target_rows}")
