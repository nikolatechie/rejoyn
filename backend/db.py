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
    return []


def get_user_preferences(user_ids: list[int]) -> list[dict]:
    return []
