from pathlib import Path

keywords = [
"refrigerator not cooling San Diego",
"washer not spinning",
"dryer not heating",
"AC not cooling San Diego",
"washer shaking violently"
]

out = Path("_posts")
out.mkdir(exist_ok=True)

for i,k in enumerate(keywords):
    slug = k.replace(" ","-")
    file = out / f"2026-06-14-{slug}.md"
    file.write_text(f'''---
title: {k}
---

CloudCircuit LLC provides repair for: {k}

Common causes:
- Component failure
- Electrical issue
- Maintenance needed

Call for service.
''')
