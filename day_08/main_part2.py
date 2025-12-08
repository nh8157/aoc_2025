def comp_and_sort_coord_dists(coords):
    def euclidean_dist(coord_1, coord_2):
        return sum([abs(coord_1[i] - coord_2[i]) ** 2 for i in range(len(coord_1))])

    coords_dists = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            coords_dists.append((i, j, euclidean_dist(coords[i], coords[j])))

    return sorted(coords_dists, key=lambda x: x[2])


def coords_before_one(coords_dists, coord_num):
    clusters = {}
    coord_cluster = {}
    curr_cluster = 0

    for i in range(len(coords_dists)):
        (coord_1, coord_2, _) = coords_dists[i]
        if coord_1 not in coord_cluster and coord_2 not in coord_cluster:
            # create new cluster
            clusters[curr_cluster] = [coord_1, coord_2]
            coord_cluster[coord_1] = curr_cluster
            coord_cluster[coord_2] = curr_cluster
            curr_cluster += 1
        elif coord_1 not in coord_cluster and coord_2 in coord_cluster:
            cluster = coord_cluster[coord_2]
            clusters[cluster].append(coord_1)
            coord_cluster[coord_1] = cluster
        elif coord_2 not in coord_cluster and coord_1 in coord_cluster:
            cluster = coord_cluster[coord_1]
            clusters[cluster].append(coord_2)
            coord_cluster[coord_2] = cluster
        elif coord_cluster[coord_1] != coord_cluster[coord_2]:
            old_cluster = coord_cluster[coord_1]
            new_cluster = coord_cluster[coord_2]
            for coord in clusters[old_cluster]:
                coord_cluster[coord] = new_cluster
                clusters[new_cluster].append(coord)
            clusters.pop(old_cluster)
        if len(clusters) == 1 and len(list(clusters.values())[0]) == coord_num:
            return (coord_1, coord_2)

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.readlines()

    coords = [[int(c) for c in coord.rstrip("\n").split(",")] for coord in content]
    sorted_dists = comp_and_sort_coord_dists(coords)
    (c_1, c_2) = coords_before_one(sorted_dists, len(coords))
    print(coords[c_1][0] * coords[c_2][0])
    # for (i, j, _) in sorted_dist:
    #     print(coords[i], coords[j])
