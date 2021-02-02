# Write a function named "bitmap" that takes a string of CSV data and returns an object with methods decribed below:
#
# get_map: takes two arguments, a column name and a value and returns a string of 1's and 0's denoting the rows that have the value in that column.
# matching_rows: takes a dict where the keys are column names and the values are values to be matched. Returns a binary string like get_map.
# get_matching_rows: takes a dict like matching_rows, but returns a CSV string (like that given to bitmap) of the rows that match the dict.

class bitmap:
    def __init__(self, map):
        self.map = map

    def get_map(self, col_name, value):
        map_str = self.map.partition('\n')

        # Get the header line
        first_line = map_str[0].split(',')
        idx = 0

        res = ""

        # Get index of column name
        for col in first_line:
            if col == col_name:
                break
            else:
                idx += 1

        # Cut out header line and split csv by lines
        map_str = map_str[2:]
        map_str = map_str[0].split('\n')

        # Go through each line, splitting by comma, and comparing at index
        for line in map_str:
            line = line.split(',')

            if line[idx] == value:
                res = res + "1"
            else:
                res = res + "0"

        return res

    def matching_rows(self, dictionary):
        map_str = self.map.partition('\n')

        # Get the header line
        first_line = map_str[0].split(',')
        idx_dict = dict()
        idx = 0

        res = ""

        # Get indicies for columns to match
        for k, v in dictionary.items():
            idx = 0
            for col in first_line:
                if col == k:
                    idx_dict[k] = idx
                    break
                else:
                    idx += 1

        # Cut out header line and split csv by lines
        map_str = map_str[2:]
        map_str = map_str[0].split('\n')

        # Go through each line of csv and find matching rows
        for line in map_str:
            line = line.split(',')

            matching_flag = False

            for k, v in dictionary.items():
                if line[idx_dict[k]] == v:
                    matching_flag = True
                else:
                    matching_flag = False
                    break

            # Check if all the rows matched
            if matching_flag:
                res = res + "1"
            else:
                res = res + "0"

        return res

    def get_matching_rows(self, dictionary):
        map_str = self.map.partition('\n')

        # Get the header line
        header = map_str[0]
        first_line = map_str[0].split(',')
        idx_dict = dict()
        idx = 0

        res = ""

        # Get indicies for columns to match
        for k, v in dictionary.items():
            idx = 0
            for col in first_line:
                if col == k:
                    idx_dict[k] = idx
                    break
                else:
                    idx += 1

        # Cut out header line and split csv by lines
        map_str = map_str[2:]
        map_str = map_str[0].split('\n')

        # Go through each line of csv and find matching rows
        for line in map_str:
            line = line.split(',')

            matching_flag = False

            for k, v in dictionary.items():
                if line[idx_dict[k]] == v:
                    matching_flag = True
                else:
                    matching_flag = False
                    break

            # Check if all the rows matched
            if matching_flag:
                res = res + "1"
            else:
                res = res + "0"

        final_str = header + '\n'

        for i in range(len(res)):
            if res[i] == "1":
                final_str = final_str + map_str[i] + '\n'

        return final_str