def dict_value(word, data, new_dict, content):
    for index in range(len(data["linhas_do_arquivo"])):
        if word.lower() in data["linhas_do_arquivo"][index].lower():
            if content:
                new_dict["ocorrencias"].append(
                    {
                        "linha": index + 1,
                        "conteudo": data["linhas_do_arquivo"][index],
                    }
                )
            else:
                new_dict["ocorrencias"].append({"linha": index + 1})


def response_value(word, instance, content):
    response = []

    for index in range(len(instance)):
        data = instance.search(index)

        new_dict = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": [],
        }

        dict_value(word, data, new_dict, content)

        if new_dict["ocorrencias"]:
            response.append(new_dict)

    return response


def exists_word(word, instance):
    return response_value(word, instance, False)


def search_by_word(word, instance):
    return response_value(word, instance, True)
