#!/usr/bin/python

class Node:
    def __init__(self, value='', parent=None, left=None, right=None):
        self.value = value
        self.parent = None
        self.left = left
        self.right = right

    def value(self):
        return self.value

    def parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def insert_left(self, node):
        node.set_parent(self)
        self.left = node

    def go_left(self):
        return self.left

    def insert_right(self, node):
        node.set_parent(self)
        self.right = node

    def go_right(self):
        return self.right

def search(root):
    node = root

    while not(node.left is None) or not(node.right is None):
        response = input(f'El Pokemon tiene {node.value}? [s/n] ')
        response = response.lower()

        if response == 's':
            if node.left is None:
                break

            node = node.left
        elif response == 'n':
            if node.right is None:
                break

            node = node.right
    
    return node

def answer(node):
    if node.left is None and node.right is None:
        response = input(f'El Pokemon es {node.value}? [s/n] ')
        response = response.lower()

        if response == 's':
            return True
        else:
            return False
    else:
        raise f'This node is not a leaf {node.value}'
          

def learn(node):
    pokemon = input(f'Que Pokemon es?: ')
    attribute = input(f'Que tiene {pokemon} que NO tenga {node.value}?: ')

    print('Guardando información...')
    parent = node.parent

    p_node = Node(value=pokemon)

    q_node = Node(value=attribute)
    q_node.insert_left(p_node)
    q_node.insert_right(node)

    if parent is None:
        parent = q_node
    else:
        if parent.left.value == node.value:
            parent.insert_left(q_node)
        else:
            parent.insert_right(q_node)

    print('Completado! :)')

    return parent

def get_root(leaf):
    node = leaf
    while not(node.parent is None):
        node = node.parent
    return node

def main():
    root = Node(value='Pikachu')

    keep_alive = True
    while keep_alive:
        response = input('Estas pensando en un Pokemon? [s/N]')
        response = response.lower()

        if response == 's':
            node = search(root)
            is_correct = answer(node)
            
            if is_correct:
                print('Atrapalos a todos!')
            else:
                learn(node)
                root = get_root(node)
        elif response == 'n':
            break

if __name__ == "__main__":
    main()
