from project.table.table import Table


class InsideTable(Table):
    TYPE = "Inside"
    MIN_NUMBER = 1
    MAX_NUMBER = 50

    @property
    def min_number(self):
        return self.MIN_NUMBER

    @property
    def max_number(self):
        return self.MAX_NUMBER

    @property
    def table_type(self):
        return self.TYPE
