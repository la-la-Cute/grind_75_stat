from dataclasses import dataclass
from enum import Enum


class Difficulty(Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


class Progress(Enum):
    ACCEPTED = "ac"
    ATTEMPTED = "notac"
    UNATTEMPTED = None


@dataclass
class ProblemInfo:
    idx: int
    title: str
    subpath: str
    difficulty: Difficulty


@dataclass
class ProblemStatus:
    question_id: str
    question_title: str
    question_path: str
    progress: Progress
