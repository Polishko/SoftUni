# value by key
side_by_player = {} # Nalan: Dark, Genc: Light: kontrol amaclı sozluk bu, listede kullanıcı aramak daha zor, burada kolay
player_by_side = {} # Dark: Nalan, Light: Genc: bu her zaman asıl sozluk

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")

        if force_side not in player_by_side:
            player_by_side[force_side] = [] # burada kullanıcıyı eklemiyor cunku baska field@da olabilir

        if force_user not in side_by_player: # yani kullanici baska fiel'da da degilse
            side_by_player[force_user] = force_side # kontrol sozlugune ekledi - artik var
            player_by_side[force_side].append(force_user) # ve field'a ekledi

    else:
        force_user, force_side = command.split(" -> ")

        if force_side not in player_by_side:
            player_by_side[force_side] = []

        player_by_side[force_side].append(force_user) # yukaridakinin aksine bunu burada yapabilir
                                                        # cunku oyuncunun bu field'da olmasi isteniyor
        if force_user in side_by_player:   # hali hazirda baska field'da varsa da siliyoruz oradan
            old_side = side_by_player[force_user] # yardimci sozlukten kolayca hangi fiel'da buluyor
            player_by_side[old_side].remove(force_user) # ve asil sozlukteki field'tan kaldiriyor ki o field bir liste
            side_by_player[force_user] = force_side # kontrol sozlugunde fiel'ini guncelliyor
        else:
            side_by_player[force_user] = force_side  # hali hazirda oyuncu yoksa da kontrol sozlugune ekliyor

        print(f"{force_user} joins the {force_side} side!")

for side, members in player_by_side.items(): # artik burada yazdirma asil sozlukte devam ediyor
    if len(members) == 0:
        continue

    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")
