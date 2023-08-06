class Table:
    def __init__(
        self,
        array: list,
        first_row_is_header: bool = True,
        header: list = [],
        title: str = "",
        left_pad=1,
        right_pad=1,
        right_align=[int, float],
    ) -> None:
        """creates a text table that can be printed to the consol

        Args:
            array (list): a array of columns.
            first_row_header (bool, optional): If the first row is a header or data. Defaults to True.
            header (list, optional): if you want to specify your own header (MUST be have the same amount of elements as you have columns or length 1). Defaults to [].
            title (string, optional): add a title to the top of your table, "" = no title. Defaults to ""
        """
        self.columns = array
        self.first_row_is_header = first_row_is_header
        self.header = header
        self.title = title
        self.left_pad = left_pad
        self.right_pad = right_pad
        self.right_align = right_align

        self.get_length_of_columns()

    def get_length_of_columns(self):
        lengths = [0] * len(self.columns)

        for idx, column in enumerate(self.columns):
            for element in column:
                element = str(element)
                length = len(element)
                if length > lengths[idx]:
                    lengths[idx] = length

        self.lengths = lengths
        self.number_of_columns = len(self.columns)
        self.number_of_rows = len(self.columns[0])

    def get_spaces(self, row: list or tuple):
        spaces = []

        for idx, item in enumerate(row):
            spaces.append(" " * (self.lengths[idx] - len(str(item))))

        return spaces

    def append(self, row: list):
        if len(row) == len(self.columns):
            for idx, item in enumerate(row):
                self.columns[idx].append(item)

            self.get_length_of_columns()
            return True

        else:
            return False

    def pop(self) -> tuple:
        result = []

        for row in self.columns:
            result.append(row.pop())

        self.get_length_of_columns()

        return tuple(result)

    def print_row(self, row: list or tuple):
        result = ""
        spaces = self.get_spaces(row)
        for idx, item in enumerate(row):
            result += f"|{' '*self.left_pad}"
            if type(item) in self.right_align:
                result += f"{spaces[idx]}{item}"
            else:
                result += f"{item}{spaces[idx]}"

            result += f"{' '*self.right_pad}"

        result += "|"

        print(result)

    def print(self):
        line = ""

        for length in self.lengths:
            line += f"+{'-'*(length+self.left_pad+self.right_pad)}"
        line += "+"

        if self.title != "":
            top_line = f"+{'-'*(sum(self.lengths)+self.number_of_columns*(self.left_pad+self.right_pad)+self.number_of_columns-1)}+"
            print(top_line)

            title_len = len(self.title)

            line_len = len(top_line) // 2
            print(
                f"|{' '*(line_len-(title_len//2)-1)}{self.title}{' '*(line_len-(title_len//2)-1)}|"
            )
        print(line)

        for idx in range(self.number_of_rows):
            row = []

            for c in range(self.number_of_columns):
                row.append(self.columns[c][idx])

            if idx == 0:
                if self.header != [] and self.first_row_is_header:
                    self.print_row(self.header)
                    print(line)
                    continue

                elif self.header != []:
                    self.print_row(self.header)
                    print(line)

                else:
                    if self.first_row_is_header:
                        self.print_row(row)
                        print(line)
                        continue

            self.print_row(row)
        print(line)


if __name__ == "__main__":
    rec = []
    rec.append(["name", "Jack", "Jill"])
    rec.append(["sex", "M", "F"])
    rec.append(["person_id", 234516, 341])
    # rec.append(["test", "hi", "hello"])

    header = ["a", "b", "c", "d"]
    title = "My Table"

    table = Table(rec, True, title=title)

    table.print()
