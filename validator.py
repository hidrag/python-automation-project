def validate_user(user):
    errors = []

    if not user.get("name") or not user["name"].strip():
        errors.append("Missing name")

    try:
        age = int(user.get("age", -1))
        if age < 0:
            errors.append("Age must be non-negative")
    except ValueError:
        errors.append("Age is not a valid number")

    return errors
