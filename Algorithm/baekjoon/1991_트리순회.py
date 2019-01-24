N = int(input())
dict_tree = {}

for n in range(N):
    msg = input().split()
    dict_tree[msg[0]] = [msg[1],msg[2]]

def preorder(node):
    if node == '.':
        return ''
    else:
        li = dict_tree.get(node)
        left = li[0]
        right = li[1]
        return node+preorder(left)+preorder(right)

def inorder(node):
    if node == '.':
        return ''
    else:
        li = dict_tree.get(node)
        left = li[0]
        right = li[1]
        return inorder(left)+node+inorder(right)

def postorder(node):
    if node == '.':
        return ''
    else:
        li = dict_tree.get(node)
        left = li[0]
        right = li[1]
        return postorder(left)+postorder(right)+node
    
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))