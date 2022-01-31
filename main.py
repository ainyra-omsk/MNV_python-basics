import math


def distance(point_1, point_2):
    return math.sqrt(((point_2 [0] - point_1[0])**2) + ((point_2 [1] - point_1[1])**2))


def find_path(point_current, list_next_points):
    result = [] #(строка пути, последняя точка, суммарное расстояние)
    if len(list_next_points) == 1:
        dist = distance(point_current, list_next_points[0])
        path_string = "->(" + str(list_next_points[0][0]) + "," + str(list_next_points[0][1]) + ")[" + str(dist) + "]"
        result.append((path_string, list_next_points[0], dist))
        return result
    for point_next in list_next_points:
        nex_list_points = []
        nex_list_points.extend(list_next_points)
        nex_list_points.remove(point_next)
        result_of_next = find_path(point_next, nex_list_points)
        dist = distance(point_current, point_next)
        for item_res in result_of_next:
            summary_dist = item_res[2] + dist
            path_string = "->(" + str(point_next[0]) + "," + str(point_next[1]) + ")[" + str(dist) + "]" + item_res[0]
            result.append((path_string, item_res[1], summary_dist))
    return result


def go_to_home(home_point, list_of_ways):
    result = []
    for way in list_of_ways:
        distance_to_home = distance(way[1], home_point)
        path_string = "(" + str(home_point[0]) + "," + str(home_point[1]) + ")" + way[0] + "->(" + str(home_point[0]) + "," + str(home_point[1]) + ")[" + str(distance_to_home) + "]"
        summary_distance = way[2] + distance_to_home
        result.append((path_string,summary_distance))
    return result

def sort_by_dist(item):
    return item[1]

pochta = (0, 2)
list_of_adreses = [(2, 5), (5, 2), (6, 6), (8, 3)]
ways_for_all_adreses = find_path(pochta, list_of_adreses)
ways_pochta_all_adreses_pochta = go_to_home(pochta, ways_for_all_adreses)
ways_pochta_all_adreses_pochta.sort(key=sort_by_dist)
print(ways_pochta_all_adreses_pochta[0][0], "=", ways_pochta_all_adreses_pochta[0][1])
print(ways_pochta_all_adreses_pochta[1][0], "=", ways_pochta_all_adreses_pochta[1][1])
