def get_terms_for_table():
    terms = []
    with open("./data/info.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            user_name, email, balls, added_by = line.split(";")
            terms.append([cnt, user_name, email, balls])
            cnt += 1
    return terms


def get_wishes_for_table():
    terms = []
    with open("./data/wishes.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            user_name, email, wish = line.split(";")
            terms.append([cnt, user_name, email, wish])
            cnt += 1
    return terms


def write_info(name, email, balls):
    new_info_line = f"{name};{email};{balls};user"
    with open("./data/info.csv", "r", encoding="utf-8") as f:
        existing_info = [l.strip("\n") for l in f.readlines()]
        title = existing_info[0]
        old_info = existing_info[1:]
    info_sorted = old_info + [new_info_line]
    info_sorted.sort()
    new_info = [title] + info_sorted
    with open("./data/info.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_info))


def write_wish(name, email, wish):
    new_wish_line = f"{name};{email};{wish}"
    with open("./data/wishes.csv", "r", encoding="utf-8") as f:
        existing_wish = [l.strip("\n") for l in f.readlines()]
        title = existing_wish[0]
        old_wishes = existing_wish[1:]
    wish_sorted = old_wishes + [new_wish_line]
    wish_sorted.sort()
    new_wishes = [title] + wish_sorted
    with open("./data/wishes.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_wishes))


def get_info_stats():
    users = 0
    balls_kol = 0
    with open("./data/info.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            user_name, email, balls, added_by = line.split(";")
            balls_kol += int(balls)
            if "user" in added_by:
                users += 1
    stats = {
        "users_amount": users,
        "average_score": round(balls_kol / users,2),
    }
    return stats
