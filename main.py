import os
from pathlib import Path

path = './docs'
all_files = list(Path(path).glob('**/*.md'))

language_ext_map = {
    ".py": "python"
}


def prettify(src, description, file_extension):
    lines = []
    language = language_ext_map[file_extension]

    lines.append(f"{description}:\n")
    lines.append(f"```{language}\n")
    [lines.append(src_line) for src_line in src]
    lines.append(f"\n```")
    return lines


for i, file in enumerate(all_files):
    new_name = file.name + ".doco"
    new_filename = os.path.join(str(file.parent), new_name)

    with open(file, "rt") as old_file:
        with open(new_filename, 'w+') as new_file:
            for line in old_file:
                if "``[An example of a failing Python pytest test](../test/test_sample.py)" in line:
                    with open('./test/test_sample.py', "r") as src:
                        desc = "An example of a failing Python pytest test"
                        filename, file_extension = os.path.splitext('../test/test_sample.py')
                        src_lines = src.readlines()
                        prettied = prettify(src_lines, desc, file_extension)
                        [new_file.write(line) for line in prettied]

                elif "``6:7[An example of a failing Python pytest test](../test/test_sample.py)" in line:
                    with open('./test/test_sample.py') as src:
                        lines = src.readlines()
                        [new_file.write(line) for line in lines[5:7]]

                else:
                    new_file.write(line)
