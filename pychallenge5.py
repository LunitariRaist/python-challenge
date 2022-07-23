import pickle


def get_data():
    file = open('pychallenge5.txt', 'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data


data = get_data()


def print_tuples():
   for i in data:
      print(i)


def make_picture():
   for i in data:
      new_line = ''
      for e in i:
         i = 0
         while e[1] > i:
            new_line += e[0]
            i += 1
      print(new_line)


print_tuples()
make_picture()
