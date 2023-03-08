import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priorityQueueInstance = PriorityQueue()
    priorityQueueInstance.enqueue({"qtd_linhas": 9})
    priorityQueueInstance.enqueue({"qtd_linhas": 4})
    priorityQueueInstance.enqueue({"qtd_linhas": 2})
    priorityQueueInstance.enqueue({"qtd_linhas": 5})
    priorityQueueInstance.enqueue({"qtd_linhas": 7})
    priorityQueueInstance.enqueue({"qtd_linhas": 11})
    priorityQueueInstance.enqueue({"qtd_linhas": 3})

    # assert priorityQueueInstance.is_priority(9) is False
    assert len(priorityQueueInstance) == 7
    with pytest.raises(IndexError):
        priorityQueueInstance.search(10)
    assert priorityQueueInstance.dequeue() == {"qtd_linhas": 4}
    assert priorityQueueInstance.search(0) == {"qtd_linhas": 2}
