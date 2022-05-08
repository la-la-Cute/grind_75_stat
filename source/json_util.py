from operator import itemgetter
from pathlib import Path

import json

from .classes import Progress, ProblemStatus


JSON_PATH = Path(__file__).parent / "user_data.json"
stat_getter = itemgetter("frontend_question_id", "question__title", "question__title_slug")

def load_data(path: Path = JSON_PATH) -> dict[str, ProblemStatus]:
    with open(path) as file:
        user_data = {}
        for problem_stat in json.load(file)["stat_status_pairs"]:
            status = ProblemStatus(*stat_getter(problem_stat["stat"]), Progress(problem_stat["status"]))
            user_data[status.question_path] = status
        return user_data
