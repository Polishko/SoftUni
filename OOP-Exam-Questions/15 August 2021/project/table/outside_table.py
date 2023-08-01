from project.table.table import Table


class OutsideTable(Table):
    TYPE = "Outside"
    MIN_NUMBER = 51
    MAX_NUMBER = 100

    @property
    def min_number(self):
        return self.MIN_NUMBER

    @property
    def max_number(self):
        return self.MAX_NUMBER

    @property
    def table_type(self):
        return self.TYPE
