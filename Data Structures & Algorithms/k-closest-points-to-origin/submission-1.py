class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        for point in points :
            eucd = math.sqrt((0-point[0]) ** 2 + (0-point[1]) ** 2)
            dic[tuple(point)] = eucd
        toreturn = []
        print(dic, sorted(dic.items(), key=lambda item: item[1]))
        for key,v in sorted(dic.items(), key=lambda item: item[1]) :
            toreturn.append(list(key))

        return toreturn[:k]

        