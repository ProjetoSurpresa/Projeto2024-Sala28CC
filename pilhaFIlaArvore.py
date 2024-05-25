import tkinter as tk
from tkinter import messagebox
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = self.Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = self.Node(value)
            else:
                self._insert_recursive(current.right, value)
        else:
            # Value already exists
            pass

    def inorder_traversal(self):
        nodes = []
        self._inorder_traversal_recursive(self.root, nodes)
        return nodes

    def _inorder_traversal_recursive(self, node, nodes):
        if node:
            self._inorder_traversal_recursive(node.left, nodes)
            nodes.append(node.value)
            self._inorder_traversal_recursive(node.right, nodes)

class StackQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Pilhas, Filas e Árvore Binária")

        self.stack = Stack()
        self.queue = Queue()
        self.binary_tree = BinaryTree()

        self.label_stack = tk.Label(root, text="Pilha:")
        self.label_stack.pack()

        self.text_stack = tk.Text(root, height=5, width=30)
        self.text_stack.pack()

        self.label_queue = tk.Label(root, text="Fila:")
        self.label_queue.pack()

        self.text_queue = tk.Text(root, height=5, width=30)
        self.text_queue.pack()

        self.label_binary_tree = tk.Label(root, text="Árvore Binária (inorder):")
        self.label_binary_tree.pack()

        self.text_binary_tree = tk.Text(root, height=5, width=30)
        self.text_binary_tree.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.push_button = tk.Button(root, text="Empilhar", command=self.push_item)
        self.push_button.pack()

        self.pop_button = tk.Button(root, text="Desempilhar", command=self.pop_item)
        self.pop_button.pack()

        self.enqueue_button = tk.Button(root, text="Enfileirar", command=self.enqueue_item)
        self.enqueue_button.pack()

        self.dequeue_button = tk.Button(root, text="Desenfileirar", command=self.dequeue_item)
        self.dequeue_button.pack()

        self.insert_button = tk.Button(root, text="Inserir na Árvore Binária", command=self.insert_item)
        self.insert_button.pack()

        self.dequeue_button = tk.Button(root, text="Clean", command=restart_program)
        self.dequeue_button.pack()

    def push_item(self):
        try:
            item = int(self.entry.get())
            self.stack.push(item)
            self.update_stack_text()
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor inteiro válido.")

    def pop_item(self):
        item = self.stack.pop()
        if item is not None:
            messagebox.showinfo("Desempilhado", f"Item desempilhado: {item}")
        else:
            messagebox.showwarning("Pilha Vazia", "A pilha está vazia.")
        self.update_stack_text()

    def enqueue_item(self):
        try:
            item = int(self.entry.get())
            self.queue.enqueue(item)
            self.update_queue_text()
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor inteiro válido.")

    def dequeue_item(self):
        item = self.queue.dequeue()
        if item is not None:
            messagebox.showinfo("Desenfileirado", f"Item desenfileirado: {item}")
        else:
            messagebox.showwarning("Fila Vazia", "A fila está vazia.")
        self.update_queue_text()

    def insert_item(self):
        try:
            item = int(self.entry.get())
            self.binary_tree.insert(item)
            self.update_binary_tree_text()
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor inteiro válido.")

    def update_stack_text(self):
        self.text_stack.delete(1.0, tk.END)
        for item in reversed(self.stack.items):
            self.text_stack.insert(tk.END, f"{item}\n")

    def update_queue_text(self):
        self.text_queue.delete(1.0, tk.END)
        for item in self.queue.items:
            self.text_queue.insert(tk.END, f"{item}\n")

    def update_binary_tree_text(self):
        self.text_binary_tree.delete(1.0, tk.END)
        nodes = self.binary_tree.inorder_traversal()
        for node in nodes:
            self.text_binary_tree.insert(tk.END, f"{node}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = StackQueueApp(root)
    root.mainloop()
