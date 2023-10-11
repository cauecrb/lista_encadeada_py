#!/usr/bin/python
# -*- coding: utf-8 -*

class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
        """
        self._head = None  # Apontador para o nó cabeça (primeiro)
        self._tail = None  # Apontador para o nó filho (ultimo)
        self._len = 0  # contador

    def __len__(self):
        return self._len

    @property
    def head(self):
        """
        Esta propriedade deve retornar o valor do primeiro nó da lista ligada
        """
        if self._head is not None:
            return self._head._value
        else:
            return None

    @property
    def tail(self):
        """
        Esta propriedade deve retornar o valor do último nó da lista ligada
        """
        if self._tail is not None:
            return self._tail._value
        else:
            return None

    def append(self, value):
        """
        Esta função deve inserir um novo nó no FINAL da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - append(0) - [1, 2, 3, 0]
        """
        pointer = self._head
        if self._head:
            # inserindo no final da lista
            while(pointer._next):
                pointer = pointer.next
            pointer.next = LinkedListNode(value)
        else:
            pointer = LinkedListNode(value)
            pointer._next = self._head
            self._head = pointer
        self._tail = LinkedListNode(value)
        self._len = self._len + 1

        #pass

    def insert(self, value):
        """
        Esta função deve inserir um novo nó no INICIO da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - insert(0) - [0, 1, 2, 3]
        """

        LinkedHead = LinkedListNode(value)
        LinkedHead._next = self._head
        self._head = LinkedHead
        self._len = self._len + 1
        return self


    def removeFirst(self):
        """
        Esta função deve remover o primeiro elemento da lista e retornar o seu valor.
        Apos a execução, a lista ligada deve ter um elemento a menos.
        """
        LinkedHead = self
        ValueDel = LinkedHead._head.value
        self._head = LinkedHead._head.next
        self._len = self._len - 1
        return ValueDel

    def getValueAt(self, index):
        """
        Esta função deve retornar o valor de um nó na posição definida por INDEX.
        Se o index for maior do que o tamanho da lista, retornar OutOfBoundsException
        """
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise "OutOfBoundsException"
        if pointer:
            return pointer._value
        else:
            raise "OutOfBoundsException"
        pass

    def toList(self):
        """
        Esta função retornar uma representação em forma de vetor ([1, 2, 3....])
        da lista ligada
        """
        array = []
        if self._head:
            pointer = self._head
            while(pointer):
                array.append(pointer._value)
                pointer = pointer.next
            print(array)
            return array
        else:
            print(array)
            return array


if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    ll = LinkedList()
    assert(ll.head is None)
    assert(ll.tail is None)
    assert(ll.toList() == [])
    ll.append(1)
    assert(ll.head == 1)
    assert(ll.tail == 1)
    assert(len(ll) == 1)
    assert(ll.toList() == [1])
    ll.append(2)
    assert(ll.head == 1)
    assert(ll.tail == 2)
    assert(len(ll) == 2)
    assert(ll.toList() == [1, 2])
    ll.append(3)
    assert(ll.head == 1)
    assert(ll.tail == 3)
    assert(len(ll) == 3)
    assert(ll.toList() == [1, 2, 3])
    ll.insert(0)
    assert(ll.head == 0)
    assert(ll.tail == 3)
    assert(len(ll) == 4)
    assert(ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert(ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == -1)
    assert(ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == 0)
    assert(ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert(v == 1)
    assert(ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert(v == 2)
    assert(ll.toList() == [3])
    v = ll.removeFirst()
    assert(v == 3)
    assert(ll.toList() == [])
    assert(len(ll) == 0)
    print("100%")