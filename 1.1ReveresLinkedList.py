class LNode:
    def __init__(self, x=None):
        self.data=x
        self.next=None

# 方法一：就地逆序
def Reverse1(head):
    if head==None or head.next == None:
        return
    pre = None #前驱节点
    cur = None # 当前节点
    next = None # 后继节点
    # 把链表首节点变为尾节点
    cur = head.next
    next = cur.next
    cur.next = None
    pre=cur
    cur=next
    #使当前遍历到的节点cur指向其前驱节点
    while cur.next != None:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=next
    #链表最后一个节点指向倒数第二个节点
    cur.next=pre
    #链表头节点指向原来链表尾节点
    head.next=cur

# 方法二：递归
def RecursiveReverse(head):
    # 方法功能：对不带头节点对单链表进行逆序
    # 输入参数：firstRef：链表头节点
    if head is None or head.next is None:
        return head
    else:
        # 反转后面节点
        newhead=RecursiveReverse(head.next)
        head.next.next=head
        head.next=None
    return newhead

def Reverse2(head):
    # 方法功能：对带头节点的单链表进行逆序
    # 输入参数：head：链表头节点
    if head is None:
        return
    firstNode=head.next
    newhead=RecursiveReverse(firstNode)
    head.next=newhead
    return newhead

# 方法三：插入法
def Reverse3(head):
    if head is None or head.next is None:
        return
    cur=None
    next=None
    cur=head.next.next
    head.next.next=None
    while cur is not None:
        next=cur.next
        cur.next=head.next
        head.next=cur
        cur=next

if __name__=="__main__":
    i=1
    #链表头节点
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    #构造单链表
    while i<8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print("逆序前：",)
    cur=head.next
    while cur!=None:
        print(cur.data, end=' ')
        cur=cur.next
    print("\n逆序后：",)
    Reverse3(head)
    cur=head.next
    while cur!=None:
        print(cur.data, end=' ')
        cur=cur.next
