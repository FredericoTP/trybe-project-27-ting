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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
