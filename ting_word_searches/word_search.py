def exists_word(word, instance):
    response = []

    for index in range(len(instance)):
        data = instance.search(index)

        new_dict = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for index in range(len(data["linhas_do_arquivo"])):
            if word.lower() in data["linhas_do_arquivo"][index].lower():
                new_dict["ocorrencias"].append({"linha": index + 1})

        if len(new_dict["ocorrencias"]) != 0:
            response.append(new_dict)

    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# {
#    "nome_do_arquivo": "arquivo_teste.txt",
#    "qtd_linhas": 3,
#    "linhas_do_arquivo": [...]
# }


# [
#    {
#        "palavra": "de",
#        "arquivo": "arquivo_teste.txt",
#        "ocorrencias": [{"linha": 2}, {"linha": 7}],
#    }
# ]
