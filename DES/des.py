from Tables.DES import E, S_BOX, SBox_columns_bin, SBox_rows_bin
from logical_operations.logic import xor_bin_string


def permutate(bin_string, permutation_array):
    tmp = []
    print(f"To Permutate: {bin_string} with: {permutation_array}")
    for bit in permutation_array:
        tmp.append(bin_string[bit - 1])
    tmp = "".join(tmp)
    print(f"--> {tmp}")
    return tmp


def f_expansion(bin_string):
    tmp = []
    print(f"Expanding: {bin_string}")
    for bit in E:
        tmp.append(bin_string[bit - 1])
    tmp = "".join(tmp)
    print(f"--> {tmp}")
    return tmp


def f_split_32_to_4(bin_string_32):
    tmp = []
    pos = 0
    print(f"Splitting: {bin_string_32} into 4x8")
    for val in range(0, 8):
        tmp.insert(val, bin_string_32[pos:pos + 4])
        pos += 4
    print(f"--> {tmp}")
    return tmp


def f_find_false_positives(bin_string_4, s_box):
    tmp = []
    tmp2 = []
    print(f"Finding False-Positives: {int(bin_string_4, 2)} in SBox: {s_box}")
    for column in range(0, 4):
        for row in range(0, 16):
            if S_BOX[s_box - 1][column][row] == int(bin_string_4, 2):
                tmp.append(row)
    for dec in tmp:
        tmp2.append(SBox_rows_bin[dec])
    tmp.clear()
    tmp.append(xor_bin_string(tmp2[0], SBox_columns_bin[0], 6))
    tmp.append(xor_bin_string(tmp2[1], SBox_columns_bin[1], 6))
    tmp.append(xor_bin_string(tmp2[2], SBox_columns_bin[2], 6))
    tmp.append(xor_bin_string(tmp2[3], SBox_columns_bin[3], 6))
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
            tmp.append(xor_bin_string(element[j][i], r0_bin_string[range_s:range_e], 6))
        range_s += 6
        range_e += 6
    return tmp
