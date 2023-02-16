from typing import Union, List, Dict
from .jobs import read


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
    data = read(path)
    max_salary = 0
    for max_salaries in data:
        # isnumeric()
        # https://www.w3schools.com/python/ref_string_isnumeric.asp
        if (
            max_salaries["max_salary"] != ""
            and max_salaries["max_salary"].isnumeric()
        ):
            salary = int(max_salaries["max_salary"])
            if salary > max_salary:
                max_salary = salary
    return max_salary


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
    data = read(path)
    min_salary = 999999999
    for min_salaries in data:
        if (
            min_salaries["min_salary"] != ""
            and min_salaries["min_salary"].isnumeric()
        ):
            salary = int(min_salaries["min_salary"])
            if salary < min_salary:
                min_salary = salary
    return min_salary


def make_value_int(value):
    # isinstance
    # https://www.w3schools.com/python/ref_func_isinstance.asp
    if isinstance(value, str):
        return int(value)
    if not isinstance(value, int):
        raise ValueError
    return value


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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    min_salary = make_value_int(job["min_salary"])
    max_salary = make_value_int(job["max_salary"])
    salary = make_value_int(salary)

    if min_salary > max_salary:
        raise ValueError

    return min_salary <= salary <= max_salary


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
    raise NotImplementedError
