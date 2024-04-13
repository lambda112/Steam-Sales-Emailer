def update_count():
    with open("count.txt", "r") as f:
        count = f.read()

    with open("count.txt", "w") as f:
        num = str(int(count) + 1)
        f.write(num)

    return num