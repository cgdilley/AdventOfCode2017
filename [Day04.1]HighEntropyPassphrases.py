
passwords = []
with open("inputs/[Day4]input.txt", "r") as f:
    for line in f.readlines():
        passwords.append(line.strip().split(" "))


def is_valid_chunk(pw, existing):

    for exist in existing:

        if exist["_len"] != len(pw):
            continue

        matches = 0
        e = dict(exist)
        for letter in pw:
            if letter in e and e[letter] > 0:
                matches += 1
                e[letter] -= 1
            else:
                break
        if matches == len(pw):
            return False

    return True


def add_to_existing(pw, existing):

    obj = {"_len": len(pw)}
    for letter in pw:
        if letter in obj:
            obj[letter] += 1
        else:
            obj[letter] = 1
    existing.append(obj)


def is_valid_password(chunks):

    existing = []
    for chunk in chunks:
        if is_valid_chunk(chunk, existing):
            add_to_existing(chunk, existing)
        else:
            return False

    return True


count = 0
for line in passwords:
    if is_valid_password(line):
        count += 1

print("VALID PASSWORDS = " + str(count))
