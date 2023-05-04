from typing import Union, List, Dict

from src.insights.jobs import read


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
    salaries = [
        int(data["max_salary"])
        for data in data_list
        if data["max_salary"].isnumeric()
    ]
    return max(salaries)


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
    salaries = [
        int(data["min_salary"])
        for data in data_list
        if data["min_salary"].isnumeric()
    ]
    return min(salaries)


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
            str(job["min_salary"]).isalpha()
            or str(job["max_salary"]).isalpha()
            or int(job["min_salary"]) > int(job["max_salary"])
            or str(salary).isalpha()
        ):
            raise TypeError
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except KeyError:
        raise ValueError("Valores ausentes ou não numéricos")
    except TypeError:
        raise ValueError("Error")


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
    filter_salary_range = []
    try:
        for job in jobs:
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            if min_salary <= int(salary) <= max_salary:
                filter_salary_range.append(job)
    except TypeError:
        raise ValueError("Não representa número válido")
    finally:
        return filter_salary_range
