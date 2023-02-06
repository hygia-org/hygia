def remove_lines_with_less_than_50_commas(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.count(',') >= 50:
                lines.append(line)
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)

file_path = './data/final.csv'
remove_lines_with_less_than_50_commas(file_path)