def generate_summary(users):
    summary = {
        "total_users": len(users),
        "active_users": 0,
        "inactive_users": 0,
        "child": 0,
        "teen": 0,
        "working_age": 0,
        "seniors": 0,
        "phone_mismatches": 0
    }

    for user in users:
        if user["is_active"]:
            summary["active_users"] += 1
        else:
            summary["inactive_users"] += 1

        if user["category"] == "Child":
            summary["child"] += 1
        elif user["category"] == "Teen":
            summary["teen"] += 1
        elif user["category"] == "Working Age":
            summary["working_age"] += 1
        else:
            summary["seniors"] += 1

        if user["remark"] != "OK":
            summary["phone_mismatches"] += 1

    return summary
