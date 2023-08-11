messages_sent = int(input())

for lines in range(1, messages_sent + 1): # lines hesapta kullanmadigin icin _ yapabilirsin
    int_num = int(input())

    if int_num == 88:
        print("Hello")
    elif int_num == 86:
        print("How are you?")
    elif int_num < 88:
        print("GREAT!")
    elif int_num > 88:
        print("Bye.")
