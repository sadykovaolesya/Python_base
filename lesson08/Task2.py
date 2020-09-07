from collections import Counter


a = 'beep boop beer!'
letter_count = Counter(a)


class Character:
    def __init__(self, string):
        self.string = string

    def create_list(self):
        my_list = []
        letter_count = Counter(self.string)
        revdict = {k: v for k, v in sorted(letter_count.items(), key=lambda item: item[1])}
        for val, key in revdict.items():
            my_list.append({key : val})

        return my_list




class Tree:
    
    def __init__(self, string):
        self.string = string
        self.my_list = Character(self.string)
        self.dict_code = {}

    def create_dict_code(self, let, code):
        self.dict_code[let]=code
        return self.dict_code

    def left_right(self, list_n, n_str = ''):
        for n, i in enumerate(list_n):
            if n == 0:

                n_str += str(n)
                if isinstance(i, list):
                    self.left_right(i, n_str)
                else:
                    self.create_dict_code(i, n_str)
                    n_str = n_str[:-1]
            else:
                if isinstance(list_n[0], str):
                    n_str += str(n)
                    if isinstance(i, list):
                        self.left_right(i, n_str)
                    else:
                        self.create_dict_code(i, n_str)
                        n_str = n_str[:-1]
                else:
                    n_str = n_str[:-1]
                    n_str += str(n)

                    if isinstance(i, list):
                        self.left_right(i, n_str)
                    else:
                        self.create_dict_code(i, n_str)
                        n_str = n_str[:-1]

    def new_node(self):
        list_chr= self.my_list.create_list()
        lentt= len(list_chr)
        list_node =[]

        i = 0
        while True:
            if i > len(list_chr) - 2:
                break
            for key, val in  list_chr[i].items():
                l = val
                count = key
            for key, val in  list_chr[i + 1].items():
                r = val
                count += key

            for j, el in enumerate(list_chr):

                for key, val in list_chr[j].items():
                    if count <= key:
                        list_chr.insert(j, {count: [l, r]})
                        break
                    elif count > key and j > lentt:
                        list_chr.append({count: [l, r]})
                        break
                else:
                    continue
                break
            list_node.append([l, r])
            i += 2

        list_node.reverse()
        self.left_right(list_node[0])




    def print_code(self):
        self.new_node()
        str_code =''
        for i in self.string:
            for key, val in self.dict_code.items():
                if i == key:
                    for j in val:
                        if (len(str_code) + 1) % 5 == 0:
                            str_code += ' '
                            str_code += j
                        else:
                            str_code += j
                    break
        return str_code

    def __str__(self):

        return f'{self.print_code()}'

c = Tree(a)
print(c)



