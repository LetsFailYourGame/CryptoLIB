def xor_bin_string(bin_string: str, bin_string_: str, bit_size=8) -> str:
    tmp = []
    for bit in range(0, bit_size):
        sbits = int(bin_string[bit])
        sbits_ = int(bin_string_[bit])
        if sbits == 1 and sbits_ == 1:
            tmp.append(str(0))
        elif sbits == 1 and sbits_ == 0 or sbits == 0 and sbits_ == 1:
            tmp.append(str(1))
        elif sbits == 0 and sbits_ == 0:
            tmp.append(str(0))
    tmp = "".join(tmp)
    return tmp


def convert_hex_to_bin_string(hex_val: hex, out_len=8) -> str:
    return f"{hex_val:0>{out_len}b}"


def shift_bit(bin_string: str, direction: str, val_to_shift: int) -> str:
    """
    @param bin_string: (str) takes str list as input
    @param direction: (str) { Leftshift: "<<" | Rightshift: ">>" }
    @param val_to_shift: (int) times to shift
    @return:
    """
    tmp = []
    if direction == "<<":  # L_Shift
        tmp.append(bin_string[val_to_shift:])
        [tmp.append("0") for i in range(0, val_to_shift)]
    elif direction == ">>":  # R_Shift
        x = bin_string[:(bin_string.__len__() - val_to_shift)]
        [tmp.append("0") for i in range(0, val_to_shift)]
        tmp.append(x)
    tmp = ''.join(tmp)
    return tmp
