import logical_operations.logic as logic

mix_col_matrix = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]


def mix_col_get_keys(mix_col_list: list):
    k = []
    for i in range(0, 15, 4):
        x1 = logic.xor_binString(mix_col_list[i], mix_col_list[i + 1])
        x2 = logic.xor_binString(mix_col_list[i + 2], mix_col_list[i + 3])
        k.append(logic.xor_binString(x1, x2))
    return k


def mix_col(hex_input_list: list) -> list:
    y = []
    px = "00011011"
    tmp_matrix = [
        logic.convert_hex_to_bin_string(hex_input_list[0]),
        logic.convert_hex_to_bin_string(hex_input_list[1]),
        logic.convert_hex_to_bin_string(hex_input_list[2]),
        logic.convert_hex_to_bin_string(hex_input_list[3])
    ]
    for row in range(0, mix_col_matrix.__len__()):
        for column in range(0, mix_col_matrix.__len__()):
            shift = logic.shift_bit(tmp_matrix[column], "<<", 1)
            xo = logic.xor_binString(shift, tmp_matrix[column])
            if mix_col_matrix[row][column] == 1:
                y.append(tmp_matrix[column])
            elif mix_col_matrix[row][column] == 2:
                if tmp_matrix[column][0] == "1":
                    y.append(logic.xor_binString(shift, px))
                else:
                    y.append(shift)
            elif mix_col_matrix[row][column] == 3:
                if tmp_matrix[column][0] == "1":
                    red = logic.xor_binString(xo, px)
                    y.append(red)
                else:
                    y.append(xo)
    return y
