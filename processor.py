def categorize_user(age):
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teen"
    elif 19 <= age <= 60:
        return "Working Age"
    else:
        return "Senior"


def process_user(user):
    age = int(user["age"])
    user["category"] = categorize_user(age)
    return user
