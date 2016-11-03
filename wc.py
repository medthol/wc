import sys

def main(args):
    flag_c = False
    flag_l = False
    flag_w = False
    read_from_stdin = False
    file_list = []
    

    for arg in args:
        if arg == '-c':
            flag_c = True
        elif arg =='-l':
            flag_l = True
        elif arg == '-w':
            flag_w = True
        elif arg == '-':
            read_from_stdin = True
        else:
            file_list.append(arg) 

    if len(file_list) == 0:
        read_from_stdin = True # read from stdin when no file argument passed

    if not flag_c and not flag_w and not flag_l:
        flag_c, flag_l, flag_w = True, True, True

    total_lines, total_words, total_chars = 0, 0, 0
    total_output =''
    
                                     #Another changes
    for filename in file_list:
        

        line_count, word_count, char_count = 0, 0, 0
        output_str = ''

        with open(filename) as fd:
            for line in fd:
                line_count += 1
                word_count += len(line.split())
                char_count += len(line)

        if flag_l:
            output_str += str(line_count) + "  "
        if flag_w:
            output_str += str(word_count) + "  "
        if flag_c:
            output_str += str(char_count) + "  "
        
        output_str += filename
        print(output_str)

        total_lines += line_count
        total_words += word_count
        total_chars += char_count
        
    if read_from_stdin:
        line_count, word_count, char_count = 0, 0, 0
        output_str =''
        
        for line in sys.stdin:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)
            
        if flag_l:
            output_str += str(line_count) + "  "
        if flag_w:
            output_str += str(word_count) + "  "
        if flag_c:
            output_str += str(char_count) + "  "

        output_str += "-"
        print(output_str)

        total_lines += line_count
        total_words += word_count
        total_chars += char_count
                              

    if flag_l:
        total_output += str(total_lines) + "  "
    if flag_w:
        total_output += str(total_words) + "  "
    if flag_c:
        total_output += str(total_chars) + "  "
    total_output += "total"
    if len(file_list) >1:
        print(total_output)

    


if __name__ == '__main__':
   main(sys.argv[1:])

        




