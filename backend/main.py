from fastapi import FastAPI, Query
from typing import List
import pandas as pd
import json
from datasets.mock_user_preferences import (
    mock_user_prefs,
)  # You can later map group_id to prefs

# from datasets.locations_with_vibes_utils import (
#     load_csv_values,
#     apply_parse_vibes,
#     create_single_group_weight_vector,
#     score_destination,
# )
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/top-destinations")
def get_top_destinations(group_id: int = Query(..., description="Group ID")):
    print(group_id)
    return {"top_destinations": {"Belgrade": "Test"}}


# RUN APP: uvicorn main:app --reload
