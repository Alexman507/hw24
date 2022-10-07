import functions

CMD_TO_FUNCTION = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'uniques': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query,
    'regex': functions.regex_query,
}
FILE_NAME = 'data/apache_logs.txt'


def build_query(cmd, param, data):
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
