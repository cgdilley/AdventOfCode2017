
passwords = []
with open("inputs/[Day4]input.txt", "r") as f:
    for line in f.readlines():
        passwords.append(line.strip().split(" "))


def is_valid_chunk(pw, existing):

    return pw not in existing


def add_to_existing(pw, existing):

    existing.add(pw)


def is_valid_password(chunks):

    existing = set()
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
