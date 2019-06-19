# Trackman

This coding challenge required reading query from provided configuration files and creating an output containing table names and their dependent tables in human readable format.

### Approach
I have used treelib (https://treelib.readthedocs.io/en/latest/) library for storing data into tree structure and printing in ascii format.

Main program loops through all configuration files in the provided directory and pass data to **process_files** method which is a recursive function. It uses the _"from clause"_ for checking table names used in configuration file for getting required value string. It then splits the _"from clause"_ into tokens separated by spaces and checks if the tokens are in standard format (few anomalies were detected with spaces at the beginning of string). Logic that I used for getting table names is the fact that every table name appears right after join keyword and every _"from clause"_ starts with a table name. There were some upper and lower case strings for which I used str.lower() to keep it standard and error free.

**Note**
Needs to work on adding a node to tree if it already contains that node but for a different parent. For that, a new tree can be created and added to the relevant position. (I have to read the documentation of library that I have used, apparently it is not letting me add any duplicate nodes)

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