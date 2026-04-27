#!/usr/bin/env python3
"""
Scratch for Kids — Simple Local Server
Run: python serve.py
Then open: http://localhost:8000
"""

import http.server
import os
import webbrowser

PORT = 8000
DIR = os.path.dirname(os.path.abspath(__file__))

CLASSES = [
    ("Class 1: Meet Scratch", "class-1-meet-scratch/class-1.html", "🐱", "Introduction to Scratch and Programming"),
    ("Class 2: Motion & Looks", "class-2-motion-and-looks/class-2.html", "🏃", "Controlling sprite movement and appearance"),
    ("Class 3: Events & Sound", "class-3-events-and-sound/class-3.html", "🎵", "Making interactive projects with events and sound"),
    ("Class 4: Loops & Conditions", "class-4-loops-and-conditions/class-4.html", "🔄", "Repeating actions and making decisions"),
    ("Class 5: Variables & Score", "class-5-variables-and-score/class-5.html", "📊", "Using variables to track score, lives, and timers"),
    ("Class 6: Cloning & Advanced", "class-6-cloning-and-advanced/class-6.html", "🧬", "Creating clones and combining all concepts"),
    ("Class 7: Final Project", "class-7-final-project/class-7.html", "🎓", "Independent project building and presentation"),
]

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Scratch Programming for Kids</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f4ff; color: #333; min-height: 100vh; }
  .hero { background: linear-gradient(135deg, #4C97FF, #855CD6); color: white; padding: 60px 20px; text-align: center; }
  .hero h1 { font-size: 2.8em; margin-bottom: 12px; }
  .hero p { font-size: 1.2em; opacity: 0.9; max-width: 600px; margin: 0 auto; }
  .meta-bar { display: flex; justify-content: center; gap: 20px; margin-top: 20px; flex-wrap: wrap; }
</style>
</head>
<body>
<div class="hero">
  <h1>🐱 Scratch Programming for Kids</h1>
  <p>A 7-class course teaching kids ages 7–12 to code with Scratch</p>
  <div class="meta-bar">
"""

def build_index():
    html = INDEX_HTML
    badges = ["⏱ 7 Hours Total", "👶 Ages 7–12", "📋 No Prerequisites", "💻 Scratch 3.0"]
    for b in badges:
        html += f'    <span style="background:rgba(255,255,255,0.2);padding:6px 16px;border-radius:20px;font-size:0.9em">{b}</span>\n'
    html += """  </div>
</div>
<div style="max-width:900px;margin:30px auto;padding:0 20px">
  <div style="display:grid;gap:20px">
"""
    colors = ["#4C97FF","#855CD6","#CF63CF","#FFAB19","#FF8C1A","#5CB1D6","#4CAF50"]
    for i, (name, path, icon, desc) in enumerate(CLASSES):
        c = colors[i]
        html += f"""    <a href="/{path}" style="text-decoration:none;color:inherit">
      <div style="background:white;border-radius:12px;padding:24px;display:flex;align-items:center;gap:20px;box-shadow:0 2px 12px rgba(0,0,0,0.06);border-left:5px solid {c};transition:transform 0.15s,box-shadow 0.15s" onmouseover="this.style.transform='translateX(6px)';this.style.boxShadow='0 4px 20px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='none';this.style.boxShadow='0 2px 12px rgba(0,0,0,0.06)'">
        <div style="font-size:2.4em;width:60px;text-align:center">{icon}</div>
        <div>
          <div style="font-size:1.2em;font-weight:bold;color:{c}">Class {i+1}</div>
          <div style="font-size:1.1em;font-weight:600;margin:2px 0">{name.split(": ")[1]}</div>
          <div style="font-size:0.9em;color:#777">{desc}</div>
        </div>
        <div style="margin-left:auto;font-size:1.5em;color:#ccc">→</div>
      </div>
    </a>
"""
    html += """  </div>
  <div style="text-align:center;padding:30px;color:#999;font-size:0.9em">
    <p>Open any class to see the full lesson with SVG diagrams, projects, and solutions.</p>
    <p style="margin-top:8px">Press <kbd style="background:#eee;padding:2px 8px;border-radius:4px;border:1px solid #ddd">Ctrl+C</kbd> in the terminal to stop the server.</p>
  </div>
</div>
</body>
</html>"""
    return html


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            content = build_index().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            super().do_GET()


if __name__ == "__main__":
    os.chdir(DIR)
    with http.server.HTTPServer(("", PORT), Handler) as server:
        url = f"http://localhost:{PORT}"
        print(f"\n  🐱 Scratch for Kids server running!")
        print(f"  📖 Open in browser: {url}")
        print(f"  🛑 Press Ctrl+C to stop\n")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n  👋 Server stopped. Bye!")
