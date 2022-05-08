from collections import defaultdict

from .parse import parse_problems
from .scrape import Scraper
from .classes import Difficulty, ProblemStatus, Progress

TARGET_URL = r"https://www.techinterviewhandbook.org/grind75"

res_text = Scraper(TARGET_URL).text
grind_lst = parse_problems(res_text)


class CompletionStat:
    def __init__(self, status_dict: dict[str, ProblemStatus]) -> None:
        self.status_dict = status_dict

    def summarize(self) -> None:
        line_dict = {}
        categories = defaultdict(lambda: [0, 0])
        for problem_info in grind_lst:
            stat_item = self.status_dict[problem_info.subpath]
            line_num = problem_info.idx
            line_text = f"{problem_info.difficulty.value:>8}   #{line_num:>2}  -  {problem_info.title:<60}  {stat_item.progress.name.capitalize()}"
            line_dict[line_num] = line_text
            if stat_item.progress == Progress.ACCEPTED:
                categories[problem_info.difficulty][0] += 1
            categories[problem_info.difficulty][1] += 1
        category_dict = {}
        for difficulty, (curr_cnt, total_cnt) in categories.items():
            line = f"{difficulty.value:>8}: {curr_cnt:>2} / {total_cnt:>2}  ({curr_cnt / total_cnt:.0%})"
            category_dict[difficulty] = line
        self.category_stat = "\n".join(category_dict[difficulty] for difficulty in Difficulty.__members__.values())
        self.text = "\n".join(line_dict[line_num] for line_num in sorted(line_dict.keys()))
