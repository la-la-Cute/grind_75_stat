"""
Log in to your Leetcode account and paste JSON file to source/user_data.json.

API url:
https://leetcode.com/api/problems/algorithms/
"""

from source import run

if __name__ == "__main__":
    completion_stat = run()
    print(completion_stat.text)
    print(completion_stat.category_stat)
