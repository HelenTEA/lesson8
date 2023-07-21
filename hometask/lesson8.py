def toggle_hat(hats, cat):
    if hats[cat]:
        hats[cat] = False
    else:
        hats[cat] = True


def circle(num_cats, rounds):
    hats = [False] * (num_cats + 1)

    for round_num in range(1, rounds + 1):
        for cat in range(round_num, num_cats + 1, round_num):
            toggle_hat(hats, cat)
    return hats


def main():
    num_cats = 100
    rounds = 100
    hats = circle(num_cats, rounds)

    # Print the final state of the cats' hats
    print("Cats with hats on:")
    for cat in range(1, num_cats + 1):
        if hats[cat]:
            print(f"Cat #{cat}")

if __name__ == "__main__":
    main()


