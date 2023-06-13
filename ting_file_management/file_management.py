import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        print("Formato inválido", file=sys.stderr)
        return

    try:
        with open(path_file) as file:
            lines = []
            for line in file:
                new_line = line.replace("\n", "")
                lines.append(new_line)

        return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
