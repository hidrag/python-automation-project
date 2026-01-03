def generate_summary(users):
    summary = {
        "total_users": len(users),
        "minors": 0,
        "working_age": 0,
        "seniors": 0
    }

    for user in users:
        if user["category"] == "Minor":
            summary["minors"] += 1
        elif user["category"] == "Working Age":
            summary["working_age"] += 1
        else:
            summary["seniors"] += 1

    return summary
