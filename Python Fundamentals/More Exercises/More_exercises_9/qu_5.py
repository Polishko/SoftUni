import re
line = input()

title, body = "", ""
matches_title = re.findall(r"(?<=<title>)(.*)(?=</title>)", line)
matches_body = re.findall(r"(?<=<body>)(.*)(?=</body>)", line)

if matches_title:
    title = matches_title[0]
if matches_body:
    body = matches_body[0]

inter_tag_new_line = r"(?<=>)(\\n)"
title = re.sub(inter_tag_new_line, "", title)
body = re.sub(inter_tag_new_line, "", body)

remove_tags = r"<[^<>]*>"
title = re.sub(remove_tags, " ", title)
body = re.sub(remove_tags, " ", body)

inter_text_new_line = r"\\n "
title = re.sub(inter_text_new_line, " ", title)
body = re.sub(inter_text_new_line, " ", body)

extra_spaces = r"\s{2,}"
title = re.sub(extra_spaces, " ", title)
body = re.sub(extra_spaces, " ", body)

print(f"Title: {title.strip()}") if title else print("Title:")
print(f"Content: {body.strip()}") if body else print("Content:")
