class day2:
    data = open('input.txt')
    def part1(self, data):
        thresholds = {"red": 12, "green": 13, "blue": 14}
        possibles = 0

        for line in data:
            game_info, sets = line.split(": ")
            groups = map(str.split, sets.replace(";", ",").split(", "))
            if all(int(cube_nums) <= thresholds[cube_color] for cube_nums, cube_color in groups):
                possibles += int(game_info.split(" ")[1])

        return possibles

    def part2(self, data):
        total_product = 0

        for line in data:
            _, sets = line.split(": ")
            sets = sets.split("; ")

            counts = {"red": 0, "green": 0, "blue": 0}
            for _set in sets:
                _set = {k: int(v) for v, k in map(str.split, _set.split(", "))}
                counts = {k: v + _set.get(k, 0) for k, v in counts.items()}

            product = 1
            for k, v in counts.items():
                product *= v + 1

            total_product += product

        return total_product