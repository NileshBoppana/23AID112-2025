class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item


class FileSystemNode:
    def __init__(self, name, is_file):
        self.name = name
        self.is_file = is_file
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def get_full_path(node):
    parts = []
    while node is not None:
        parts.append(node.name)
        node = node.parent

    path = ""
    i = len(parts) - 1
    while i >= 0:
        path += "/" + parts[i]
        i -= 1
    return path


def bfs_search(root, target_file):
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        current = queue.dequeue()

        if current.is_file and current.name == target_file:
            return current

        i = 0
        while i < len(current.children):
            queue.enqueue(current.children[i])
            i += 1

    return None


# Creating directory and file hierarchy
root = FileSystemNode("root", False)

docs = FileSystemNode("Documents", False)
pics = FileSystemNode("Pictures", False)
music = FileSystemNode("Music", False)

root.add_child(docs)
root.add_child(pics)
root.add_child(music)

file1 = FileSystemNode("resume.pdf", True)
file2 = FileSystemNode("notes.txt", True)
docs.add_child(file1)
docs.add_child(file2)

vacation = FileSystemNode("Vacation", False)
pics.add_child(vacation)

file3 = FileSystemNode("photo1.jpg", True)
file4 = FileSystemNode("photo2.jpg", True)
vacation.add_child(file3)
vacation.add_child(file4)

songs = FileSystemNode("Songs", False)
music.add_child(songs)

file5 = FileSystemNode("song1.mp3", True)
file6 = FileSystemNode("song2.mp3", True)
songs.add_child(file5)
songs.add_child(file6)

# Search for a file
target = input("Enter file name to search: ")
result = bfs_search(root, target)

if result is not None:
    print("File found")
    print("Path:", get_full_path(result))
else:
    print("File not found")
