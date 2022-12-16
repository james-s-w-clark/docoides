import os
from pathlib import Path

path = './docs'
all_files = list(Path(path).glob('**/*.md'))

for i, file in enumerate(all_files):
    new_name = file.name + ".doco"
    new_filename = os.path.join(str(file.parent), new_name)

    with open(file, "rt") as old_file:
        with open(new_filename, 'w+') as new_file:
            for line in old_file:
                if "``[An example of a failing Python pytest test](../test/test_sample.py)" in line:
                    with open('./test/test_sample.py') as src:
                        [new_file.write(line) for line in src.readlines()]
                elif "``6:7[An example of a failing Python pytest test](../test/test_sample.py)" in line:
                    with open('./test/test_sample.py') as src:
                        lines = src.readlines()
                        [new_file.write(line) for line in lines[5:7]]
                else:
                    new_file.write(line)