from hw24 import functions
from typing import Dict, Callable, Optional, List

CMD_TO_FUNCTION: Dict[str, Callable] = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'uniques': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query,
    'regex': functions.regex_query,
}
FILE_NAME: str = 'data/apache_logs.txt'


def build_query(cmd: str, param: str, data: Optional[List[str]]):
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data: list[str] = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
