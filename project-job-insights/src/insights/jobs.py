from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, mode="r") as file:
        result = []

        data_reader = csv.reader(file)
        header, *data = data_reader
        # print(header)
        # print(data)
        for row in data:
            report = {}
            # print(row)
            for i, head in enumerate(header):
                report[head] = row[i]
            result.append(report)

        # print(result)
        return result


# read("data/jobs.csv")


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    data_list = read(path)
    result = []
    for obj in data_list:
        if obj["job_type"] not in result:
            result.append(obj["job_type"])
    # print(result)
    return result


# get_unique_job_types("data/jobs.csv")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    # print(result)
    return result
