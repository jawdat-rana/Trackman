import json
import os
from treelib import Node, Tree


def read_files(path):
    """
    read all configuration files from source directory and pass json data to process individual file

    :param path: string for source directory
    :return None
    """
    files = os.listdir(path)

    for file in files:
        try:
            with open(os.path.join(path + file)) as file_handle:
                data = json.loads(file_handle.read())
            file_handle.close()
            process_file(data)
        except Exception as e:
            print(e)


def process_file(data):
    """
    find dependencies from provided query data and append to storage model

    :param data: configuration file object
    :return None
    """
    try:
        # checking the right key for "from clause"
        if 'L' in data['query']:
            from_clause = data['query']['L'][0]['M']['from']['S']
        else:
            from_clause = data['query']['M']['from']['S']

        # generating tokens
        tokens = from_clause.split(" ")
        if tokens[0] == "":
            del tokens[0]

        table_names = set()

        # searching for table names in from clause
        get_next = True
        for tok in tokens:
            if get_next:
                if tok != "":
                    table_names.add(tok)
                get_next = False
            if tok.lower() == "join":
                get_next = True

        # schema and table name as provided in configuration file
        table_name = "{}.{}".format(data['schema']['S'], data['table']['S'])

        temp = []

        # tables names used in the query
        for items in table_names:
            temp.append(items)

        add_node(table_name, temp)

    except Exception as e:
        print(e)


def add_node(table, vals):
    """
    
    :param table: table name
    :param vals: dependent tables
    :return None
    """

    try:
        # adding table, dependent tables to root if not in tree
        if not relationship.contains(table):
            relationship.create_node(table, table, "root")
            for i in vals:
                if not relationship.contains(i):
                    relationship.create_node(i, i, table)
        # adding dependent tables if table already in tree
        else:
            for i in vals:
                if not relationship.contains(i):
                    relationship.create_node(i, i, table)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # initializing tree structure for storing relationships / dependencies
    relationship = Tree()
    relationship.create_node("root", "root")

    # read all files
    read_files(path="tables//")

    # print tables names and their dependencies in ascii
    relationship.show()
