input_line_1 = input()
input_line_2 = input()
input_line_3 = input()

input_str_1 = input_line_1.split(" ")
input_str_2 = input_line_2.split(" ")
input_str_3 = input_line_3.split(" ")

winner = ""

for i in range(3):
    for k in range(3):
        for m in range(3):
            if input_str_1[0] == "1" and input_str_1[1] == "1" and input_str_1[2] == "1":
                winner = "1"
            elif input_str_1[0] == "2" and input_str_1[1] == "2" and input_str_1[2] == "2":
                winner = "2"
            elif input_str_2[0] == "1" and input_str_2[1] == "1" and input_str_2[2] == "1":
                winner = "1"
            elif input_str_2[0] == "2" and input_str_2[1] == "2" and input_str_2[2] == "2":
                winner = "2"
            elif input_str_3[0] == "1" and input_str_3[1] == "1" and input_str_3[2] == "1":
                winner = "1"
            elif input_str_3[0] == "2" and input_str_3[1] == "2" and input_str_3[2] == "2":
                winner = "2"

            elif input_str_1[0] == "1" and input_str_2[1] == "1" and input_str_3[2] == "1":
                winner = "1"
            elif input_str_1[0] == "2" and input_str_2[1] == "2" and input_str_3[2] == "2":
                winner = "2"
            elif input_str_1[2] == "1" and input_str_2[1] == "1" and input_str_3[0] == "1":
                winner = "1"
            elif input_str_1[2] == "2" and input_str_2[1] == "2" and input_str_3[0] == "2":
                winner = "2"

            elif input_str_1[0] == "1" and input_str_2[0] == "1" and input_str_3[0] == "1":
                winner = "1"
            elif input_str_1[0] == "2" and input_str_2[0] == "2" and input_str_3[0] == "2":
                winner = "2"
            elif input_str_1[1] == "1" and input_str_2[1] == "1" and input_str_3[1] == "1":
                winner = "1"
            elif input_str_1[1] == "2" and input_str_2[1] == "2" and input_str_3[1] == "2":
                winner = "2"
            elif input_str_1[2] == "1" and input_str_2[2] == "1" and input_str_3[2] == "1":
                winner = "1"
            elif input_str_1[2] == "2" and input_str_2[2] == "2" and input_str_3[2] == "2":
                winner = "2"

            else:
                winner = "0"

if winner == "1":
    print(f"First player won")
elif winner == "2":
    print(f"Second player won")
else:
    print(f"Draw!")
