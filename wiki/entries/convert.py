import markdown2

titles = ["CSS.md", "Django.md", "Git.md", "HTML.md", "Python.md"]


with open(f"entries/{titles}.md", 'r') as f:
            text = f.read()
            html = markdown2.markdown(text)

with open(f"entries/{titles}.md", 'w') as f:
    f.write(html)
    print(html)


