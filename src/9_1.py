answer = input("あなたの好きな色は？?")
with open("fav_color.txt", "w") as f:
    f.write(answer)