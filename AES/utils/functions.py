import logical_operations.logic as logic
from Tables.AES import index, mix_col_matrix, aes_sbox


def mix_col_get_keys(mix_col_list: list):
    k = []
    for i in range(0, 15, 4):
        x1 = logic.xor_bin_string(mix_col_list[i], mix_col_list[i + 1])
        x2 = logic.xor_bin_string(mix_col_list[i + 2], mix_col_list[i + 3])
        k.append(logic.xor_bin_string(x1, x2))
    return k


def generate_mix_col_list(hex_input_list: list) -> list:
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
            xo = logic.xor_bin_string(shift, tmp_matrix[column])
            if mix_col_matrix[row][column] == 1:
                y.append(tmp_matrix[column])
            elif mix_col_matrix[row][column] == 2:
                if tmp_matrix[column][0] == "1":
                    y.append(logic.xor_bin_string(shift, px))
                else:
                    y.append(shift)
            elif mix_col_matrix[row][column] == 3:
                if tmp_matrix[column][0] == "1":
                    red = logic.xor_bin_string(xo, px)
                    y.append(red)
                else:
                    y.append(xo)
    return y


def aes_find_in_sbox(bin_byte: str) -> str:
    x = bin_byte[:4]
    y = bin_byte[4:]
    hstrx = '%0*X' % ((len(x) + 3) // 4, int(x, 2))
    hstry = '%0*X' % ((len(y) + 3) // 4, int(y, 2))
    posx = 0
    posy = 0
    for i in range(0, index.__len__()):  # find hex in sbox
        if str(hstrx) == index[i]:
            posx = i
        if str(hstry) == index[i]:
            posy = i
    # print(f"{hstrx}{hstry} : [{posx}][{posy}]")
    return logic.convert_hex_to_bin_string(aes_sbox[posx][posy])
