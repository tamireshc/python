from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data_list = read(path)
    max_salary_list = []
    for obj in data_list:
        if (
            obj["max_salary"] not in max_salary_list
            and obj["max_salary"].isdigit()
        ):
            max_salary_list.append(int(obj["max_salary"]))
    # print(max(max_salary_list))
    return max(max_salary_list)


# get_max_salary("data/jobs.csv")


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data_list = read(path)
    min_salary_list = []
    for obj in data_list:
        if (
            obj["min_salary"] not in min_salary_list
            and obj["min_salary"].isdigit()
        ):
            min_salary_list.append(int(obj["min_salary"]))
    print(min(min_salary_list))
    return min(min_salary_list)


# get_min_salary("data/jobs.csv")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    try:
        if (
            type(job["max_salary"]) not in [str, int]
            or type(job["min_salary"]) not in [str, int]
            or type(salary) not in [str, int]
            or (
                type(job["max_salary"]) == str
                and job["max_salary"].isdigit() is False
            )
            or (
                type(job["min_salary"]) == str
                and job["min_salary"].isdigit() is False
            )
            or (type(salary) == str and salary.isdigit() is False)
            or int(job["min_salary"]) > int(job["max_salary"])
        ):

            raise ValueError

        elif int(salary) >= int(job["min_salary"]) and int(salary) <= int(
            job["max_salary"]
        ):
            return True
        else:
            return False
    except KeyError:
        raise ValueError


# matches_salary_range({"max_salary": "7", "min_salary": "9"}, "5")
# matches_salary_range({"min_salary": 5}, "5")
# matches_salary_range({"max_salary": "7", "min_salary": "9"}, "5")
# matches_salary_range({"max_salary": "7", "min_salary": "4"}, 11)
# matches_salary_range({"max_salary": "7", "min_salary": "4"}, 5)
# matches_salary_range({"max_salary": "7", "min_salary": []}, 1)

# None, "", "aloha", [], {}, lambda: 1


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # print(salary)
    # if type(salary) == str and not salary.isdigit() and salary != "":
    #     raise ValueError
    selected_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                selected_jobs.append(job)
        except ValueError:
            pass
    return selected_jobs


# jobs = [
#     {"max_salary": 0, "min_salary": 10},  # 0
#     {"max_salary": 10, "min_salary": 100},  # 1
#     {"max_salary": 10000, "min_salary": 200},  # 2
#     {"max_salary": 15000, "min_salary": 0},  # 3
#     {"max_salary": 1500, "min_salary": 0},  # 4
#     {"max_salary": -1, "min_salary": 10},  # 5
# ]


# filter_by_salary_range(jobs, None)

#  salaries = [0, 1, 5, 1000, 2000, -1, -2, None, "", [], {}, lambda: 1]
