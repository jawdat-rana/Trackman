import json
import os
from treelib import Node, Tree


def read_config_file(dir_path, file_name):
    """
    read file and return contents

    :param dir_path: string directory path
    :param file_name: string file name
    :return config_data: json data from configuration file
    """
    try:
        with open(os.path.join(dir_path + file_name)) as file_handle:
            config_data = json.loads(file_handle.read())
        file_handle.close()

    except Exception as e:
        print(e)

    return config_data


def process_file(data, tree, parent):
    """
    find dependencies from provided query data and append to storage model

    :param data: json data from configuration file
    :param tree: tree node
    :param parent: string parent
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
        table = "{}.{}".format(data['schema']['S'], data['table']['S'])

        if not tree.contains(table):
            tree.create_node(table, table, parent)

        for items in table_names:
            # base case
            if os.path.exists(os.path.join(path + items + ".json")):
                d = read_config_file(path, items + ".json")
                process_file(d, tree, table)
            elif not tree.contains(items):
                tree.create_node(items, items, table)
            else:
                pass
                # need to implement if an item is already in tree but for a different parent
                # temp = Tree()
                # temp.create_node(items, items)
                # tree.paste(table, temp)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    path = "tables//"
    files = os.listdir(path)

    for file in files:
        relationship = Tree()

        data = read_config_file(path, file)

        table_name = "{}.{}".format(data['schema']['S'], data['table']['S'])
        relationship.create_node(table_name, table_name)

        process_file(data, relationship, table_name)

        relationship.show()