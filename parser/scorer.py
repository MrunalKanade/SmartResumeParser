def calculate_score(data):

    score = 0

    if data["name"] != "Not Found":
        score += 10

    if data["email"] != "Not Found":
        score += 15

    if data["phone"] != "Not Found":
        score += 15

    if len(data["skills"]) >= 5:
        score += 30

    if len(data["education"]) > 0:
        score += 15

    if int(data["experience"]) > 0:
        score += 15

    return score