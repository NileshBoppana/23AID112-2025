## Binary Tree vs B-Tree

| Aspect | Binary Tree | B-Tree |
|--------|------------|--------|
| Definition | A hierarchical data structure where each node has at most 2 children | A self-balancing multi-way tree where each node can have multiple children |
| Maximum Children per Node | 2 (left and right) | Up to m children (depends on order of B-Tree) |
| Minimum Children per Node | 0 (leaf node) | At least ceil(m/2) children (except root) |
| Height of Tree | Can be large (unbalanced) | Always kept small (balanced) |
| Balance Property | Not necessarily balanced | Always balanced |
| Search Complexity | O(n) worst case | O(log n) |
| Insertion | Simple, no strict rules | Complex (node splitting required) |
| Deletion | Simple | Complex (merging/redistribution required) |
| Data Storage | Data stored in all nodes | Data stored in sorted order within nodes |
| Number of Keys per Node | 1 key per node | Multiple keys per node |
| Traversal Methods | Inorder, Preorder, Postorder | Mostly level-order or sequential access |
| Memory Usage | Less efficient for large datasets | Efficient for large datasets |
| Disk Access Optimization | Not optimized for disk | Optimized for disk access (minimizes I/O operations) |
| Applications | Expression trees, recursion, simple structures | Databases, file systems, indexing |
| Example Use | Binary Search Tree (BST) | Database indexing (like MySQL, Oracle) |
| Structure Type | Simple tree | Multi-level indexed structure |
| Performance on Large Data | Slower | Faster and efficient |


# Difference Between Stack and Queue

| Feature | Stack | Queue |
|---|---|---|
| Full Form / Rule | LIFO (Last In, First Out) | FIFO (First In, First Out) |
| Meaning | The last inserted element is removed first | The first inserted element is removed first |
| Insertion Operation | Push | Enqueue |
| Deletion Operation | Pop | Dequeue |
| Access Operation | Peek / Top | Front / Peek |
| End Used for Insertion | One end called **top** | Rear end |
| End Used for Deletion | Same end (**top**) | Front end |
| Working Style | Insert and delete from the same side | Insert at rear and delete from front |
| Example Input | 10, 20, 30 | 10, 20, 30 |
| First Element Removed | 30 | 10 |
| Real-Life Example | Pile of plates | People standing in a line |
| Order Followed | Reverse order of insertion | Same order of insertion |
| Main Use | Function calls, undo operation, expression evaluation | Scheduling, buffering, printer queue |
| Structure Type | Linear data structure | Linear data structure |
