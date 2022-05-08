import re

from bs4 import BeautifulSoup

from .classes import Difficulty, ProblemInfo


def parse_problems(res_text: str) -> list[ProblemInfo]:
    soup = BeautifulSoup(res_text, features="html.parser")
    pattern = re.compile(r"https://leetcode.com/problems/(?P<SUBPATH>[a-z0-9\-]+)")
    selected = soup.find_all("div", attrs={"class": "flex", "role": "listitem"})
    res = []
    for idx, item in enumerate(selected, 1):
        anchor_ele = item.find("a", href=pattern)
        title = anchor_ele.string
        subpath = pattern.match(anchor_ele["href"])["SUBPATH"]
        difficulty_str = item.find("div", class_="flex space-x-2").find("span").string
        res.append(ProblemInfo(idx, title, subpath, Difficulty(difficulty_str)))
    return res
