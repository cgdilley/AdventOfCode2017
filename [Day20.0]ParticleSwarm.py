
particles = []
with open("inputs/[Day20]input.txt", "r") as f:
    num = 0
    for line in f.readlines():
        part = {"name": str(num)}

        s_split = line.strip().split(", ")

        part["pos"] = [int(x) for x in s_split[0][3:-1].split(",")]
        part["vel"] = [int(x) for x in s_split[1][3:-1].split(",")]
        part["acc"] = [int(x) for x in s_split[2][3:-1].split(",")]

        particles.append(part)

        num += 1


def calc_after_delay(particle, delay):
    p = {"name": particle["name"], "acc": particle["acc"]}

    # V = V° + AT
    # D = V°T + AT²

    v0_t = [delay * x for x in particle["vel"]]
    at = [delay * x for x in particle["acc"]]
    at2 = [(delay ** 2) * x for x in particle["acc"]]
    d = [a + b for a, b in zip(v0_t, at2)]

    p["pos"] = [a + b for a, b in zip(particle["pos"], d)]
    p["vel"] = [a + b for a, b in zip(at, particle["vel"])]

    return p


def pythag(coord):
    x, y, z = coord
    return ((x * x) + (y * y) + (z * z)) ** 0.5


def closest_to_origin(p):
    return min(p, key=lambda x: pythag(x["pos"]))


STEP = 1000
ITER = 0

while ITER < 10 ** 6:
    ITER += STEP
    particles = [calc_after_delay(part, STEP) for part in particles]
    closest = closest_to_origin(particles)
    print("CLOSEST = " + closest["name"])




