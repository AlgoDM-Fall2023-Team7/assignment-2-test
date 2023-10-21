# read query file
def read_query(query_file_path) -> str:
    with open(query_file_path, 'r') as file:
        query: str = file.read()
    return query