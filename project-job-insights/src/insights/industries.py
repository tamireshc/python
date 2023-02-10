from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    data_list = read(path)
    result = []
    for obj in data_list:
        if obj["industry"] not in result and obj["industry"] != "":
            result.append(obj["industry"])
    # print(result)
    return result


# get_unique_industries("data/jobs.csv")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    result = []
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)
    return result
