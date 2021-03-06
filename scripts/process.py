import json
import os
import sys
from glob import glob

def render_link_page(el):
    md = """---
layout: nav
title: %(title)s
questions:
""" % el

    for link in el["links"]:
        link = str(link)
        subel = graph[link] 
        if "page" in subel:
            href = subel["page"]
        else:
            href = "%s.html" % link

        ctx = {
            "href" : href,
            "title" : subel["title"],
            "text" : subel.get("text", "")
        }
        md += """ - title: <a href="%(href)s">%(title)s</a>
   text: "%(text)s"
""" % ctx

    if "decisionbox" in el:
        md += """links:
  qno: %(no)s
  qyes: %(yes)s
  qdontknow: %(dontknow)s
""" % el["decisionbox"]

    if "topics" in el:
        md += """topics:
"""
        for topic in el["topics"]:
            md += " - %s\n" % topic["title"]

    if "resources" in el:
        md += """resources:
"""
        for resource in el["resources"]:
            md += " - %s\n" % resource["title"]

    md += "---"
    return md

def render_terminal_page(el):
    md = """---
layout: dummy_terminal
question: %(title)s
---
""" % el
    return md

for html in glob("*.html"):
    os.remove(html)
    
graph = json.load(open(sys.argv[1]))
stack = ["0"]

for idx in graph.keys():
    el = graph[idx]

    filename = "%s.html" % idx
    if idx == "0": filename= "index.html"
    if os.path.exists(filename):
        continue

    render_link_page(el)

    if el["links"]:
        md = render_link_page(el)
    else:
        md = render_terminal_page(el)

    fp = open(filename, "w")
    fp.write(md)
    fp.close()

