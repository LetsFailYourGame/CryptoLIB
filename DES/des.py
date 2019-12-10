from logical_operations.logic import xor_binString

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

P_1 = [9, 17, 23, 31, 13, 28, 2, 18,
       24, 16, 30, 6, 26, 20, 10, 1,
       8, 14, 25, 3, 4, 29, 11, 19,
       32, 12, 22, 7, 5, 27, 15, 21]

S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

SBox_rows_bin = ["000000", "000010", "000100", "000110", "001000", "001010", "001100", "001110", "010000", "010010",
                 "010100", "010110", "011000", "011010", "011100", "011110"]
SBox_columns_bin = ["000000", "000001", "100000", "100001"]


def permutate(binString, permutationArray):
    tmp = []
    print(f"To Permutate: {binString} with: {permutationArray}")
    for bit in permutationArray:
        tmp.append(binString[bit - 1])
    tmp = "".join(tmp)
    print(f"--> {tmp}")
    return tmp


def f_expansion(binString):
    tmp = []
    print(f"Expanding: {binString}")
    for bit in E:
        tmp.append(binString[bit - 1])
    tmp = "".join(tmp)
    print(f"--> {tmp}")
    return tmp


def f_split_32Bit_to_4Bit(binString_32):
    tmp = []
    pos = 0
    print(f"Splitting: {binString_32} into 4x8")
    for val in range(0, 8):
        tmp.insert(val, binString_32[pos:pos + 4])
        pos += 4
    print(f"--> {tmp}")
    return tmp


def f_find_false_positives(binString_4, s_box):
    tmp = []
    tmp2 = []
    print(f"Finding False-Positives: {int(binString_4, 2)} in SBox: {s_box}")
    for column in range(0, 4):
        for row in range(0, 16):
            if S_BOX[s_box - 1][column][row] == int(binString_4, 2):
                tmp.append(row)
    for dec in tmp:
        tmp2.append(SBox_rows_bin[dec])
    tmp.clear()
    tmp.append(xor_binString(tmp2[0], SBox_columns_bin[0], 6))
    tmp.append(xor_binString(tmp2[1], SBox_columns_bin[1], 6))
    tmp.append(xor_binString(tmp2[2], SBox_columns_bin[2], 6))
    tmp.append(xor_binString(tmp2[3], SBox_columns_bin[3], 6))
    print(f"--> {tmp}")
    return tmp


def combine_tuple_in_list(list_to_join, save_to_array):
    pos = 0
    for i in list_to_join:
        save_to_array.insert(pos, ''.join(i))
        pos += 1
    return save_to_array


def find_final_key_combination(element, r0_bin_string):
    tmp = []
    range_s = 0
    range_e = 6
    for j in range(0, 8):
        for i in range(0, 4):
            tmp.append(xor_binString(element[j][i], r0_bin_string[range_s:range_e], 6))
        range_s += 6
        range_e += 6
    return tmp