import hashlib
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123123123",
        database="rejoyn",
    )


# print(get_connection())


def register_user(user):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query = """
		INSERT INTO users (full_name, email, password, dob, gender)
		VALUES (%s, %s, %s, %s, %s)
		"""
        hashed_password = hashlib.sha256(user["password"].encode()).hexdigest()
        cursor.execute(
            query,
            (
                user["full_name"],
                user["email"],
                hashed_password,
                user["dob"],
                user["gender"][0],
            ),
        )
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def get_user_ids_for_group(group_id: int) -> list[int]:
    return []


def get_user_preferences(user_ids: list[int]) -> list[dict]:
    return []
