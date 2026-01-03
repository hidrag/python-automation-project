def categorize_user(age):
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teen"
    elif 19 <= age <= 60:
        return "Working Age"
    else:
        return "Senior"


def normalize_is_active(value):
    return value.lower() in ["true", "yes", "1"]


def normalize_phone(phone, country):
    digits = "".join(filter(str.isdigit, phone))
    country = country.upper()
    remark = "OK"

    if country == "INDIA":
        normalized = f"+91{digits}"
    elif country == "USA":
        normalized = f"+1{digits}"
    else:
        normalized = digits
        remark = "Country-phone mismatch"

    return normalized, remark


def process_user(user):
    age = int(user["age"])
    country = user["country"].upper()

    phone_normalized, phone_remark = normalize_phone(
        user["phone"], country
    )

    user["category"] = categorize_user(age)
    user["country"] = country
    user["is_active"] = normalize_is_active(user["is_active"])
    user["phone"] = phone_normalized
    user["remark"] = phone_remark

    return user
