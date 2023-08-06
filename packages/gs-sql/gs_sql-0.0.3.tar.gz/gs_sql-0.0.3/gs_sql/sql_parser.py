import re
from googleapiclient.errors import HttpError

from .dataclasses import QueryType


class SQLParser():
    def __init__(self, data_difinition, data_manipulation=None):
        self.data_difinition = data_difinition
        self.data_manipulation = data_manipulation

    def execute(self, sql_query):
        if not self.data_difinition.table_id and not re.search("CREATE DATABASE (\w+)", sql_query):
            raise ConnectionError()

        if sql_query[-1] != ";":
            sql_query += ";"

        sql_type = self.__get_query_type(sql_query)

        #DDL
        if sql_type is QueryType.CREATE:
            return self.__execute_create(sql_query)

        if sql_type is QueryType.ALTER:
            return self.__execute_alert(sql_query)

        if sql_type is QueryType.DROP:
            return self.__execute_drop(sql_query)

        #DML
        if sql_type is QueryType.SELECT:
            #TODO: Трабл
            a = self.__execute_select(sql_query)
            return a

        if sql_type is QueryType.INSERT:
            return self.__execute_inset(sql_query)

        if sql_type is QueryType.UPDATE:
            return self.__execute_update(sql_query)

        if sql_type.DELETE is QueryType.DELETE:
            return self.__execute_delete(sql_query)

    def __get_query_type(self, sql_query):
        if re.search(r'^\s*CREATE', sql_query, re.IGNORECASE):
            query_type = QueryType.CREATE

        elif re.search(r'^\s*SELECT', sql_query, re.IGNORECASE):
            query_type = QueryType.SELECT

        elif re.search(r'^\s*INSERT', sql_query, re.IGNORECASE):
            query_type = QueryType.INSERT

        elif re.search(r'^\s*UPDATE', sql_query, re.IGNORECASE):
            query_type = QueryType.UPDATE

        elif re.search(r'^\s*ALTER', sql_query, re.IGNORECASE):
            query_type = QueryType.ALTER

        elif re.search(r'^\s*DELETE', sql_query, re.IGNORECASE):
            query_type = QueryType.DELETE

        elif re.search(r'^\s*DROP', sql_query, re.IGNORECASE):
            query_type = QueryType.DROP

        else:
            query_type = QueryType.UNKNOWN

        return query_type

    def __execute_create(self, sql_query):

        table_pattern = r'CREATE TABLE IF NOT EXISTS (\w+)'
        table_match = re.search(table_pattern, sql_query)
        if table_match:
            table_name = table_match.group(1)

            column_pattern = r'\((.*?)\)'
            column_match = re.search(column_pattern, sql_query)
            if column_match:
                columns = column_match.group(1).split(',')

                columns = [column.strip().strip('"') for column in columns]

                try:
                    result = self.data_difinition.create_table(table_name, columns)
                    return result

                except HttpError:
                    return None




        table_pattern = r'CREATE TABLE (\w+)'
        table_match = re.search(table_pattern, sql_query)
        if table_match:
            table_name = table_match.group(1)

            column_pattern = r'\((.*?)\)'
            column_match = re.search(column_pattern, sql_query)
            if column_match:
                columns = column_match.group(1).split(',')

                columns = [column.strip().strip('"') for column in columns]

                result = self.data_difinition.create_table(table_name, columns)

                return result

        base_pattern = r'CREATE DATABASE (\w+)'
        table_match = re.search(base_pattern, sql_query)
        if table_match:
            base_name = table_match.group(1)

            result = self.data_difinition.create_database(base_name)

            return result




    def __execute_alert(self, sql_query):
        table_pattern = r'ALTER TABLE (\w+)'
        table_match = re.search(table_pattern, sql_query)
        if table_match:
            table_name = table_match.group(1)

            columns_pattern = r'ALTER COLUMN (.*?);'
            columns_match = re.search(columns_pattern, sql_query)
            if columns_match:
                columns = columns_match.group(1).split(',')

                columns = [column.strip() for column in columns]

                result = self.data_difinition.alert_column(table_name, columns)

                return result

            rename_pattern = r'RENAME COLUMN (\w+) TO (\w+);'
            rename_match = re.search(rename_pattern, sql_query)
            if rename_match:
                old_name = rename_match.group(1)
                new_name = rename_match.group(2)


                result = self.data_difinition.rename_column(table_name, old_name, new_name)

                return result

            delete_pattern = r'ALTER TABLE (\w+)'
            delete_match = re.search(delete_pattern, sql_query)
            if delete_match:
                delete_name = delete_match.group(1)

                column_pattern = r'DROP COLUMN (\w+);'
                column_match = re.search(column_pattern, sql_query)
                if column_match:
                    column_name = column_match.group(1)

                    result = self.data_difinition.delete_column(delete_name, column_name)

                    return result

    def __execute_drop(self, sql_query):
        table_pattern = r'DROP TABLE (\w+);'
        table_match = re.search(table_pattern, sql_query)
        if table_match:
            table_name = table_match.group(1)

            result = self.data_difinition.drop_table(table_name)

        return result

    def __execute_select(self, sql_query):
        table_pattern = r'FROM (\w+)'
        table_match = re.search(table_pattern, sql_query)
        if table_match:
            table_name = table_match.group(1)
            if re.search(r"\bINNER\s+JOIN\b", sql_query, re.IGNORECASE):
                dependent_tables = re.findall(r"\bINNER\s+JOIN\s+(\w+)\b", sql_query, re.IGNORECASE)

                if dependent_tables:
                    print(table_name)
                    print(dependent_tables)
                    result = self.data_manipulation.select_join_data(sql_query, table_name, dependent_tables)
                    return result

            else:
                result = self.data_manipulation.select_data(table_name, sql_query)
                return result

    def __execute_inset(self, sql_query):
        table_pattern = r'INSERT INTO (\w+)'
        table_match = re.search(table_pattern, sql_query)
        columns = values = table_name = None
        if table_match:
            table_name = table_match.group(1)

            values_pattern = r'VALUES \((.*?)\)'
            values_match = re.search(values_pattern, sql_query)
            if values_match:
                values = values_match.group(1).split(',')

                values = [value.strip() for value in values]

            column_pattern = rf'{table_name} \((.*?)\)'
            column_match = re.search(column_pattern, sql_query)
            if column_match:
                columns = column_match.group(1).split(',')

                columns = [column.strip() for column in columns]

            result = self.data_manipulation.insert_data(table_name, values, columns)

            return result
    def __execute_update(self, sql_query):
        table_name = re.search(r'UPDATE\s+(\w+)', sql_query).group(1)

        column_values = re.findall(r'SET\s+(.*?)\s+WHERE', sql_query, re.DOTALL)[0]
        columns = re.findall(r'(\w+)\s*=\s*(\w+)', column_values)
        column_dict = {column: value for column, value in columns}

        new_query = re.sub(r'.*?(?=WHERE)', f'SELECT * FROM {table_name} ', sql_query, count=1)
        result = self.data_manipulation.update_rows(table_name, new_query, column_dict)

        return result



    def __execute_delete(self, sql_query):
        table_pattern = r'DELETE FROM (\w+)'
        table_match = re.search(table_pattern, sql_query)
        if table_match:
            table_name = table_match.group(1)
            new_query = sql_query.replace("DELETE ", "SELECT * ")

            result = self.data_manipulation.delete_rows(table_name, new_query)

            return result