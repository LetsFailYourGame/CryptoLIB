import logical_operations.logic as logic

mix_col_matrix = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]


def convert_4bytes_to_bin_string_matrix(byte_matrix: hex) -> list:
    tmp_matrix = [
        logic.convert_hex_to_bin_string(byte_matrix[0]),
        logic.convert_hex_to_bin_string(byte_matrix[1]),
        logic.convert_hex_to_bin_string(byte_matrix[2]),
        logic.convert_hex_to_bin_string(byte_matrix[3])
    ]
    return tmp_matrix


def mix_col(bin_matrix: str) -> list:
    y = []
    px = "00011011"
    for row in range(0, mix_col_matrix.__len__()):
        for column in range(0, mix_col_matrix.__len__()):
            shift = logic.shift_bit(bin_matrix[column], "<<", 1)
            xo = logic.xor_binString(shift, bin_matrix[column])
            if mix_col_matrix[row][column] == 1:
                y.append(bin_matrix[column])
            elif mix_col_matrix[row][column] == 2:
                if bin_matrix[column][0] == "1":
                    y.append(logic.xor_binString(shift, px))
                else:
                    y.append(shift)
            elif mix_col_matrix[row][column] == 3:
                if bin_matrix[column][0] == "1":
                    red = logic.xor_binString(xo, px)
                    y.append(red)
                else:
                    y.append(xo)
    return y
