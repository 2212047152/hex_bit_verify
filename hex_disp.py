import sys

def output_init(file_name):
    file = open("./"+file_name+".txt", "w")
    sys.stdout = file
    return file

def output_destory(file_p):
    file_p.close()

def hex_disp(hex_string,reverse=1):
    print("----------------------------->")
    print("Print hex:", hex_string.upper())
    re_bin_string = ""
    binary_string = ''.join(['{:04b}'.format(int(hex_string[i], 16)) for i in range(0, len(hex_string))])
    if(reverse):
        re_bin_string = reverse_binary(binary_string)
    else:
        re_bin_string = binary_string
    bin_disp(re_bin_string)

def bin_disp(bin_string,base = 0):
    print("Print binary", bin_string)
    print("\nByte:%d" % ((len(bin_string)+1)/8 - 1))
    for i in range(len(bin_string)):
        print("\t[",len(bin_string) - i - 1 + base,"\t]:",bin_string[i], end='')
        if((i+1)%8==0 and i != len(bin_string) - 1):
            print("\nByte:%d" % ((len(bin_string)+1)/8 - (i+1)/8 - 1))
    print(" ")
        

    
def subhex_disp(hex_string, start_bit, end_bit):
    print("\n\n----------------------------->")
    binary_string = ''.join(['{:04b}'.format(int(hex_string[i], 16)) for i in range(0, len(hex_string))])
    re_bin_string = reverse_binary(binary_string)
    sub_binary_string = re_bin_string[start_bit:end_bit+1]
    re_sub_binary_string = reverse_binary(sub_binary_string)
    subhex = hex(int(re_sub_binary_string, 2))[2:]
    print("Subhex:",subhex,"h ,start",start_bit, ", end", end_bit)
    bin_disp(re_sub_binary_string, base=start_bit)


def reverse_hex(hex_string):
    bytes_list = [hex_string[i] for i in range(0, len(hex_string))]
    bytes_list.reverse()
    return ''.join(bytes_list)

def reverse_binary(bin_string):
    bytes_list = [bin_string[i] for i in range(0, len(bin_string))]
    bytes_list.reverse()
    return ''.join(bytes_list)

if __name__ == "__main__":
    hex_string = "20000080000001ff0000000000000200"
    file = output_init("log_for_"+hex_string)
    hex_disp(hex_string,reverse=0)
    subhex_disp(hex_string,63,64)
    output_destory(file)
