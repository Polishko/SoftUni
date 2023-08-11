exam_results = {}
submissions = {}

while True:
    command = input()

    if command == "exam finished":
        break

    entry = command.split("-")

    if entry[1] == "banned":
        username = entry[0]
        if username in exam_results:
            del exam_results[username]
            continue

    username, language, points = entry[0], entry[1], int(entry[2])

    if username not in exam_results:
        exam_results[username] = {}

    if language not in exam_results[username].keys():
        exam_results[username][language] = 0

    exam_results[username][language] = max(exam_results[username][language], points)

    if language not in submissions:
        submissions[language] = 0

    submissions[language] += 1

print("Results:")

for key, value in exam_results.items():
    for sub_key, sub_value in value.items():
        print(f"{key} | {sub_value}")

print("Submissions:")

for key, value in submissions.items():
    print(f"{key} - {value}")
