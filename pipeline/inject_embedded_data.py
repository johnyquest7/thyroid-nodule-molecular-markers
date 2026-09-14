"""
Injects data/thyroid_mutations.json into index.html as EMBEDDED_MUTATIONS
to ensure 100% functionality both under HTTP (GitHub Pages) and local file:// protocols.
"""

import json
import re

with open("data/thyroid_mutations.json", "r", encoding="utf-8") as f:
    mutations = json.load(f)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

embedded_js = f"const EMBEDDED_MUTATIONS = {json.dumps(mutations)};\n    const EMBEDDED_METADATA ="

html_updated = html.replace("const EMBEDDED_METADATA =", embedded_js)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_updated)

print("Injected EMBEDDED_MUTATIONS into index.html successfully.")
