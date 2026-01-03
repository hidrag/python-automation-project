import re

def validate_user(user):
    errors = []

    # Name
    name = user.get("name", "").strip()
    if not name:
        errors.append("Missing name")
    elif len(name) < 3:
        errors.append("Name too short")

    # Age
    try:
        age = int(user.get("age", -1))
        if age < 0:
            errors.append("Age must be non-negative")
    except ValueError:
        errors.append("Age is not a number")

    # Email
    email = user.get("email", "").strip()
    if not email or "@" not in email:
        errors.append("Invalid email")

    # Country
    country = user.get("country", "").strip()
    if not country:
        errors.append("Missing country")

    # is_active
    is_active = user.get("is_active", "").lower()
    if is_active not in ["true", "false", "yes", "no", "1", "0"]:
        errors.append("Invalid is_active value")

    # Phone
    phone_digits = re.sub(r"\D", "", user.get("phone", ""))
    if not phone_digits:
        errors.append("Missing phone")
    elif len(phone_digits) != 10:
        errors.append("Phone must be exactly 10 digits")

    return errors
