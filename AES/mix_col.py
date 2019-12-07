import logical_operations.logic as logic

mix_col_matrix = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

b = [0x23, 0x24, 0x34, 0xF8]

bc_matrix = [
    logic.convert_hex_to_bin_string(b[0]),
    logic.convert_hex_to_bin_string(b[1]),
    logic.convert_hex_to_bin_string(b[2]),
    logic.convert_hex_to_bin_string(b[3])
]


def calc_mix_col(bin_matrix):
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


tmp = calc_mix_col(bc_matrix)

for i in range(0, 15, 4):
    x1 = logic.xor_binString(tmp[i], tmp[i + 1])
    x2 = logic.xor_binString(tmp[i + 2], tmp[i + 3])
    print(logic.xor_binString(x1, x2))
