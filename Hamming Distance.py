bio_str_1 = "@Samuel"
bio_str_2 = "@OluwoyoSamuel"

def h_d_loop(str_1, str_2):
    h_distance = 0
    for position in range (len(str_1)):
        if str_1[position] != str_2[position]:
            h_distance +=1
    return h_distance


def h_d_set(str_1, str_2):
    bio_str_1 = set([(x, y) for x, y in enumerate(str_1)])
    bio_str_2 = set([(x, y) for x, y in enumerate(str_2)])

    return len(bio_str_1.difference(bio_str_2))


print("Loop Hamming Distance: ", end='')
print(h_d_loop(bio_str_1, bio_str_2))

print("Set Hamming Distance: ",end='')
print(h_d_set(bio_str_1, bio_str_2))