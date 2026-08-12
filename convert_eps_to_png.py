#!/usr/bin/env python3
"""
Convert EPS screenshots to PNG format.
"""

import os
from PIL import Image
import subprocess

screenshots_dir = "screenshots"

# List of EPS files to convert
eps_files = [
    "01-start-screen.eps",
    "02-gameplay.eps",
    "03-intense-moment.eps"
]

print("🖼️  Converting EPS to PNG...\n")

for eps_file in eps_files:
    eps_path = os.path.join(screenshots_dir, eps_file)
    png_path = eps_path.replace(".eps", ".png")

    if not os.path.exists(eps_path):
        print(f"⚠ Skipping {eps_file} (not found)")
        continue

    try:
        # Try using PIL with Ghostscript (fallback)
        print(f"Converting {eps_file}...", end=" ")

        # Open EPS and convert to PNG
        try:
            img = Image.open(eps_path)
            # Convert RGBA if needed
            if img.mode == 'RGBA':
                # Create white background
                background = Image.new('RGB', img.size, (0, 0, 0))
                background.paste(img, mask=img.split()[3])
                img = background
            else:
                img = img.convert('RGB')

            # Save as PNG with good quality
            img.save(png_path, 'PNG', quality=95)
            print(f"✓ Saved {os.path.basename(png_path)}")
        except Exception as e:
            print(f"\n  PIL conversion failed: {e}")
            print(f"  Trying alternative method...")

            # Try using Pillow's internal EPS support
            # This requires Ghostscript system package
            try:
                img = Image.open(eps_path)
                img.load()
                img.save(png_path, 'PNG')
                print(f"  ✓ Converted via alternative method")
            except Exception as e2:
                print(f"  ✗ Failed: {e2}")
                print(f"  EPS file saved at: {eps_path}")
                print(f"  You can convert manually using:")
                print(f"    brew install ghostscript")
                print(f"    gs -q -dNOPAUSE -dBATCH -sDEVICE=png16m -r150 -sOutputFile={png_path} {eps_path}")

    except Exception as e:
        print(f"✗ Error converting {eps_file}: {e}")

print("\n✅ Conversion complete!")
print(f"📁 Check {screenshots_dir}/ for images")
