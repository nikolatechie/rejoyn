import hashlib
import hmac
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


def login(user):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        query = """
		SELECT id, password FROM users
		WHERE email = %s
		"""
        cursor.execute(query, (user["email"],))
        result = cursor.fetchone()
        if result:
            stored_hashed_password = result["password"]
            input_hashed_password = hashlib.sha256(
                user["password"].encode()
            ).hexdigest()
            if hmac.compare_digest(stored_hashed_password, input_hashed_password):
                print("Login successful")
                return result["id"]  # Return user ID
            else:
                print("Invalid password")
                return None
        else:
            print("Email not found")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_user_ids_for_group(group_id: int) -> list[int]:
    return []


def get_user_preferences(user_ids: list[int]) -> list[dict]:
    return []
