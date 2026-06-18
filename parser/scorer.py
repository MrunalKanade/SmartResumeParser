def calculate_score(data):

    score = 0

    if data["email"] != "Not Found":
        score += 20

    if data["phone"] != "Not Found":
        score += 20

    if len(data["skills"]) > 3:
        score += 30

    if len(data["education"]) > 0:
        score += 15

    if int(data["experience"]) > 0:
        score += 15

    return score