import os
import json
import csv
import pickle


def traverse_directory(path, output_dir):

    file_names = []

    contents = os.listdir(path)
    for item in contents:
        path = os.path.join(path, item)

        if os.path.isdir(path):
            traverse_directory(path, output_dir)
        else:
            file_names.append(item)

    with open(os.path.join(output_dir, 'file_names.json'), 'w') as f:
        json.dump(file_names, f, indent=2)
    with open(os.path.join(output_dir, 'file_names.csv'), 'w') as f:
        writer = csv.writer(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(file_names)
    with open(os.path.join(output_dir, 'file_names.pickle'), 'wb') as f:
        pickle.dump(file_names, f)


if __name__ == '__main__':
    output_dir = '/gb_python_course/main_package/files_package'
    traverse_directory('/gb_python_course/main_package', output_dir)
