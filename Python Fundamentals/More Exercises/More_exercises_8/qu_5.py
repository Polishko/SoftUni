title = input()
content = input()
indent = "    "
print(f"<h1>\n{indent}{title}\n</h1>")
print(f"<article>\n{indent}{content}\n</article>")

while True:
    line = input()

    if line == "end of comments":
        break

    print(f"<div>\n{indent}{line}\n</div>")
