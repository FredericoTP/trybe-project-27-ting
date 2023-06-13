import sys
from .file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    for index in range(len(instance)):
        element = instance.search(index)
        if element == new_dict:
            return

    instance.enqueue(new_dict)
    print(new_dict, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    file_removed = instance.dequeue()

    print(
        f"Arquivo {file_removed['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout,
    )
    return


def file_metadata(instance, position):
    if position < 0 or position > len(instance):
        print("Posição inválida", file=sys.stderr)
        return

    searched_file = instance.search(position)
    print(searched_file, file=sys.stdout)
