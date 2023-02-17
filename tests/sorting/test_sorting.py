from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Web developer",
            "min_salary": "1500",
            "max_salary": "4000",
            "date_posted": "2020-10-12",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "2000",
            "date_posted": "2021-03-16",
        },
        {
            "title": "Back end developer",
            "min_salary": "1600",
            "max_salary": "3000",
            "date_posted": "2022-11-18",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2023-01-31",
        },
    ]

    sort_by(jobs, "max_salary")
    assert jobs[0] == {
        "title": "Full stack end developer",
        "min_salary": "4000",
        "max_salary": "8000",
        "date_posted": "2023-01-31",
    }

    sort_by(jobs, "min_salary")
    assert jobs[0] == {
        "title": "Front end developer",
        "min_salary": "1000",
        "max_salary": "2000",
        "date_posted": "2021-03-16",
    }

    sort_by(jobs, "date_posted")
    assert jobs[0] == {
        "title": "Full stack end developer",
        "min_salary": "4000",
        "max_salary": "8000",
        "date_posted": "2023-01-31",
    }
