import json
import os
from glob import glob


for html in glob("*.html"):
    os.remove(html)
    
graph = json.load(open("map.json"))
stack = ["0"]

while len(stack) > 0:
    idx = stack.pop()
    el = graph[idx]

    filename = "%s.html" % idx
    if os.path.exists(filename):
        continue

    el["base_page"] = "nav" if el["links"] else "terminal"
    md = """---
layout: %(base_page)s
title: %(title)s
questions:
""" % el

    for link in el["links"]:
        link = str(link)
        stack.append(link)
        subel = graph[link] 
        ctx = {
            "href" : ("%s.html" % link),
            "title" : subel["title"],
            "text" : subel.get("text", "")
        }
        md += """ - title: <a href="%(href)s">%(title)s</a>
   text: "%(text)s"
""" % ctx

    md += "---"
    fp = open(filename, "w")
    fp.write(md)
    fp.close()

