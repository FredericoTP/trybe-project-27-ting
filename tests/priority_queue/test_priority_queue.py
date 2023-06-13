import pytest
from ting_file_management.priority_queue import PriorityQueue


is_priority = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...],
}

not_priority = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 7,
    "linhas_do_arquivo": [...],
}


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue(not_priority)
    queue.enqueue(not_priority)
    queue.enqueue(is_priority)
    queue.enqueue(not_priority)
    queue.enqueue(is_priority)

    assert len(queue) == 5

    returned_value = queue.dequeue()

    assert returned_value == is_priority
    assert queue.search(0) == is_priority
    assert queue.search(3) == not_priority

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(10)
