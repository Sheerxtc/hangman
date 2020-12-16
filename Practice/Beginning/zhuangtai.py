rock = []
county = []

def collect_songs():
    song = "Enter a song."
    ask = "Type r or c. q to quit\n"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre == "c":
            cy = input(song)
            county.append(cy)

        else:
            print("Invalid.")
    print(rock)
    print(county)

collect_songs()
