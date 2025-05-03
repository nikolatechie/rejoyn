# Scores are 1-5, least to most important

# Likes art, culture, museums, food, etc.
user1 = {
    "art_and_culture": 4,
    "beach": 3,
    "outdoor_adventures": 4,
    "nightlife_and_entertainment": 2,
    "great_food": 4,
    "underrated_destinations": 2,
    "safety": 4,
    "weather": 4,
}
# Likes going out, beach, and food
user2 = {
    "art_and_culture": 2,
    "beach": 5,
    "outdoor_adventures": 4,
    "nightlife_and_entertainment": 5,
    "great_food": 4,
    "underrated_destinations": 1,
    "safety": 3,
    "weather": 5,
}
# Likes weather and extreme outdoor sports
user3 = {
    "art_and_culture": 1,
    "beach": 3,
    "outdoor_adventures": 5,
    "nightlife_and_entertainment": 1,
    "great_food": 3,
    "underrated_destinations": 1,
    "safety": 2,
    "weather": 5,
}


def get_mock_user_prefs():
    mock_user_prefs = [user1, user2, user3]
    return mock_user_prefs
