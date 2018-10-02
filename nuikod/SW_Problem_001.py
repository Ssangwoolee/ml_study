class FileHandler() :
    NoOfCase = 0
    InputStrings = []
    F = None

    def read_input_case(self, file_path):
        self.F = open(file_path, 'r')
        self.NoOfCase = int(self.F.readline())
        for i in range(self.NoOfCase):
            self.InputStrings.append(self.F.readline())


class NumberHandler():
    OutputFigureBook = []

    def add_figurebook(self):
        self.OutputFigureBook.append({'0': False, '1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False, '9': False})
        return self.OutputFigureBook[-1]

    def input_number(self, figurebook, figure):
        figurebook[figure] = not figurebook[figure]

    def current_count(self):
        for idx, figurebook in enumerate(self.OutputFigureBook):
            count = 0
            for key in figurebook:
                if figurebook[key]:
                    count += 1
            print("#{} {}".format(idx+1, count))


def calc_jinsoo(path):
    hdl_file = FileHandler()
    hdl_file.read_input_case(path)
    hdlNumber = NumberHandler()

    for str in hdl_file.InputStrings:
        figurebook = hdlNumber.add_figurebook()
        index = 0
        while index < len(str) - 1:
            hdlNumber.input_number(figurebook, str[index])
            index += 1

    hdlNumber.current_count()
    hdl_file.F.close()
    hdl_file.InputStrings.clear()
    hdlNumber.OutputFigureBook.clear()


calc_jinsoo("D:\GitRepo\ml_study\sangwoo\input.txt")
