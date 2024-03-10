class OrderedStream:

    def __init__(self, n: int):
        self.dict = {}
        self.indexes = [i for i in range(1, n + 1)]

    def insert(self, idKey: int, value: str) -> list[str]:
        if idKey == min(self.indexes):
            self.indexes.remove(idKey)
            if idKey + 1 in self.dict:
                result = [value]
                for key in sorted(self.dict):
                    idKey += 1
                    if key == idKey:
                        self.indexes.remove(key)
                        result.append(self.dict.pop(key))
                    else:
                        break
                return result
            else:
                return [value]
        else:
            self.dict[idKey] = value
        return []


data = [[9], [9, "nghbm"], [7, "hgeob"], [6, "mwlrz"], [4, "oalee"], [2, "bouhq"], [1, "mnknb"], [5, "qkxbj"],
        [8, "iydkk"], [3, "oqdnf"]]


def run():
    order = OrderedStream(data[0][0])
    result = []
    for i in range(1, len(data)):
        result.append(order.insert(data[i][0], data[i][1]))
        print(order.dict)
    print(result)


run()
print([[], [], [], [], [], ["mnknb", "bouhq"], [], [], ["oqdnf", "oalee", "qkxbj", "mwlrz", "hgeob", "iydkk", "nghbm"]])
