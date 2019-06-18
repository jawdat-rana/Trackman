# Trackman

This coding challenge required reading query from provided configuration files and creating an output containing table names and their dependent tables in human readable format.

### Approach
I have broken down my solution into three methods: reading files, processing individual files to obtain table names and then appending those table names to final tree structure. I have used treelib (https://treelib.readthedocs.io/en/latest/) library, which has all the features for storing and printing as per requirements of this exercise.

**read_files** method reads all the configuration files from provided directory path.

**process_files** method use the _"from clause"_ for checking table names used in configuration file, line 34 to 37 checks the key for getting required value string. It then splits the _"from clause"_ into tokens separated by spaces, line 41 checks if the tokens are in standard format (few anomalies were detected with spaces at the beginning of string). Logic that I used for getting table names was the fact that every table name appears right after join keyword and every _"from clause"_ started with a table name. There were some upper and lower case strings for which I used str.lower() to keep it standard and error free. In the last part, this method adds table names to tree data structure using _add_node_.

**add_node** method add the table names to the right level. It takes two parameters: table name and list of dependent table names. It first checks if table name is already present in the tree - if its not then it adds it to level zero and dependent tables under that, else add dependent tables to the already existing table name node.

### Compile and Execute
1. Fork/Clone/Download this repo
`git clone https://github.com/jawdat-rana/Trackman.git`

2. Navigate to the directory
`cd Trackman-master`

3. Install the dependencies
`pip install -r requirements.txt`

4. Run `python trackman.py`

### Notes
There is a little change in the expected output. The library I have used for data structure uses tree and there can only be one root node, I have initialized the structure using "root" as root node which can be seen in the output. 