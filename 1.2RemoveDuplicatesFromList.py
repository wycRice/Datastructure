class LNode:
    def __init__(self,x=None):
        self.data=x
        self.next=None
# 顺序删除
def removeDup1(head):
    if head==None or head.next==None:
        return
    outerCur=head.next # 用于外层循环，指向链表第一个节点
    innerCur=None # 内层循环，遍历outerCur后面的节点
    innerPre=None
    while outerCur!=None:
        innerCur=outerCur.next
        innerPre=outerCur
        while innerCur!=None:
            # 找到重复节点并删除
            if outerCur.data == innerCur.data:
                innerPre.next=innerCur.next
                innerCur=innerCur.next
            else:
                innerPre=innerCur
                innerCur=innerCur.next
        outerCur=outerCur.next

#递归法
def removeDupResursion(head):
    if head.next is None:
        return head
    pointer=None
    cur=head
    #对以head.next为首的子链表删除重复节点
    head.next=removeDupResursion(head.next)
    pointer=head.next
    #找出以head.next为首的子链表中与head节点相同的节点并删除
    while pointer is not None:
        if head.data==pointer.data:
            cur.next=pointer.next
            pointer=cur.next
        else:
            pointer=pointer.next
            cur=cur.next
    return head

def removeDup(head):
    if head is None:
        return
    head.next=removeDupResursion(head.next)

if __name__=="__main__":
    i=1
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    while i<7:
        tmp=LNode()
        if i%2 ==0:
            tmp.data=i+1
        elif i%3==0:
            tmp.data=i-2
        else:
            tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1

    print('删除重复节点前:', end=' ')
    cur=head.next
    while cur!=None:
        print(cur.data, end=' ')
        cur=cur.next
    print('begining...')
    removeDup(head)
    print('\n删除重复节点后:', end=' ')
    cur=head.next
    while cur!=None:
        print(cur.data, end=' ')
        cur=cur.next


