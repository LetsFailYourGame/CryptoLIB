import logical_operations.logic as logic
from AES.utils.functions import convert_4bytes_to_bin_string_matrix, mix_col

input_bytes = [
    0x23, 0x24, 0x34, 0xF8
]

b_matrix = convert_4bytes_to_bin_string_matrix(input_bytes)
tmp = mix_col(b_matrix)

for i in range(0, 15, 4):
    x1 = logic.xor_binString(tmp[i], tmp[i + 1])
    x2 = logic.xor_binString(tmp[i + 2], tmp[i + 3])
    print(logic.xor_binString(x1, x2))
