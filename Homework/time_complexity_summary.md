# Time Complexity Summary

## Stack

| Operation | Time Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Peek / Top | O(1) |
| Search | O(n) |

---

## Queue

| Operation | Time Complexity |
|---|---|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front / Peek | O(1) |
| Search | O(n) |

---

## Binary Tree

| Operation | Time Complexity |
|---|---|
| Insertion | O(n) |
| Deletion | O(n) |
| Search | O(n) |
| Traversal (Inorder / Preorder / Postorder) | O(n) |

> Note: In a general binary tree, operations may require checking many nodes.

---

## Binary Search Tree (BST)

| Operation | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Search | O(log n) | O(log n) | O(n) |
| Insertion | O(log n) | O(log n) | O(n) |
| Deletion | O(log n) | O(log n) | O(n) |
| Traversal | O(n) | O(n) | O(n) |

---

## Graph

| Operation | Time Complexity |
|---|---|
| Add Vertex | O(1) |
| Add Edge | O(1) |
| Remove Edge | O(1) or O(n) |
| Remove Vertex | O(V + E) |
| BFS Traversal | O(V + E) |
| DFS Traversal | O(V + E) |

> Here,  
> **V** = Number of vertices  
> **E** = Number of edges

---

## Short Summary Table

| Data Structure | Main Operations | Time Complexity |
|---|---|---|
| Stack | Push, Pop, Peek | O(1) |
| Queue | Enqueue, Dequeue, Front | O(1) |
| Binary Tree | Search, Insert, Delete | O(n) |
| BST | Search, Insert, Delete | O(log n) average, O(n) worst |
| Graph | BFS, DFS | O(V + E) |