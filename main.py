import argparse

def read_file(filename) -> list[str]:
    original_file_contents: list[str] = None

    with open(filename, "r") as f:
        original_file_contents = f.readlines()

    return original_file_contents

def convert_js_to_text(filename) -> None:
    original_file_contents: list[str] = read_file(filename)
    formatted_file_contents: list[str] = []

    for line in original_file_contents:
        curr_line = line
        curr_line = curr_line.replace("    ", "\\t").replace("\n", '\\n"\n')
        formatted_file_contents.append(f'"{curr_line}')

    with open("output.txt", "w") as f:
        for i, line in enumerate(formatted_file_contents):
            if i == len(formatted_file_contents) - 1:
                f.write(line.replace("}", '}"'))
            else:
                f.write(line)

def convert_text_to_js(filename) -> None:
    original_file_contents: list[str] = read_file(filename)
    formatted_file_contents: list[str] = []

    for line in original_file_contents:
        curr_line = line
        curr_line = curr_line.replace("\\t", "    ").replace('\\n"\n', "\n").replace('}"', "}").replace(";", "")
        formatted_file_contents.append(f'"{curr_line}')

    with open("output.js", "w") as f:
        for line in formatted_file_contents:
            # File still contains 2 quotation marks at the beginning of each line
            # so slice it up
            f.write(line[2:])

def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
                    prog='JSTranscriber',
                    description='Hellos your world',
                    epilog='Beans')
    
    parser.add_argument("filename")
    parser.add_argument("-js", action="store_true")
    parser.add_argument("-txt", action="store_true")

    return parser

def do_not_convert(args) -> bool:
    filename = args.filename

    bad_filetype = False
    no_conversion_option = False
    both_conversion_options = False

    allowed_filetypes = ["txt", "js"]

    if not any(["js" in filename, "txt" in filename]):
        print("The filetype must be either .js or .txt!")
        bad_filetype = True
    
    if not args.js and not args.txt:
        print("Enter one of the following conversion options: -txt, -js")
        no_conversion_option = True

    if args.js and args.txt:
        print("Pick only one of the following conversion options: -txt, -js")
        both_conversion_options = True

    if any([bad_filetype, no_conversion_option, both_conversion_options]):
        return True
    
    return False

def main():
    parser = init_parser()
    args = parser.parse_args()

    filename = args.filename

    if do_not_convert(args):
        return

    if args.js:
        convert_text_to_js(filename)

    if args.txt:
        convert_js_to_text(filename)

if __name__ == "__main__":
    main()