from .json_util import load_data
from .report_stat import CompletionStat


def run():
    completion_stat = CompletionStat(load_data())
    completion_stat.summarize()
    return completion_stat
