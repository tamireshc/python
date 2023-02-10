from src.pre_built.sorting import sort_by
import pytest

data_test = [
    {
        "job_title": "Data Engineer/Architect with Security Clearance",
        "min_salary": "74916",
        "max_salary": "128610",
        "date_posted": "2020-04-24",
        "job_type": "FULL_TIME",
        "id": "3319",
    },
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "58824",
        "max_salary": "112227",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3320",
    },
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "91443",
        "max_salary": "155868",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3323",
    },
]

data_test_min_salary_order = [
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "58824",
        "max_salary": "112227",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3320",
    },
    {
        "job_title": "Data Engineer/Architect with Security Clearance",
        "min_salary": "74916",
        "max_salary": "128610",
        "date_posted": "2020-04-24",
        "job_type": "FULL_TIME",
        "id": "3319",
    },
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "91443",
        "max_salary": "155868",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3323",
    },
]

data_test_max_salary_order = [
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "91443",
        "max_salary": "155868",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3323",
    },
    {
        "job_title": "Data Engineer/Architect with Security Clearance",
        "min_salary": "74916",
        "max_salary": "128610",
        "date_posted": "2020-04-24",
        "job_type": "FULL_TIME",
        "id": "3319",
    },
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "58824",
        "max_salary": "112227",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3320",
    },
]

data_test_date_posted_order = [
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "91443",
        "max_salary": "155868",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3323",
    },
    {
        "job_title": "Data Engineer with Security Clearance",
        "min_salary": "58824",
        "max_salary": "112227",
        "date_posted": "2020-05-02",
        "job_type": "FULL_TIME",
        "id": "3320",
    },
    {
        "job_title": "Data Engineer/Architect with Security Clearance",
        "min_salary": "74916",
        "max_salary": "128610",
        "date_posted": "2020-04-24",
        "job_type": "FULL_TIME",
        "id": "3319",
    },
]


def test_sort_by_criteria():
    sort_by(data_test, "min_salary")
    assert data_test == data_test_min_salary_order
    sort_by(data_test, "max_salary")
    assert data_test == data_test_max_salary_order
    sort_by(data_test, "date_posted")
    assert data_test == data_test_date_posted_order
    with pytest.raises(ValueError):
        sort_by(data_test, "xx")
