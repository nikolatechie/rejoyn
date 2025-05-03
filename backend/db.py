import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123123123",
        database="rejoyn",
    )


# print(get_connection())


def get_user_ids_for_group(group_id: int) -> list[int]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM groups_users WHERE group_id = %s", (group_id,))
    user_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return user_ids


def get_user_preferences(user_ids: list[int]) -> list[dict]:
    if not user_ids:
        return []

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    format_strings = ",".join(["%s"] * len(user_ids))
    query = f"""
        SELECT user_id, feature_name, value
        FROM users_preferences
        WHERE user_id IN ({format_strings})
    """
    cursor.execute(query, tuple(user_ids))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Transform into list of user preference dicts
    user_prefs = {}
    for row in rows:
        uid = row["user_id"]
        if uid not in user_prefs:
            user_prefs[uid] = {}
        user_prefs[uid][row["feature_name"]] = row["value"]

    return list(user_prefs.values())
