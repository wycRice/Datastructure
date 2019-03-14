class LNode:
    def __init__(self, x=None):
        self.data=x
        self.next=None

def add(h1,h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h1
    c=0
    sums=0
    p1=h1.next
    p2=h2.next
    tmp=None
    resultHead=LNode()
    resultHead.next=None
    p=resultHead
    while p1 is not None and p2 is not None:
        tmp=LNode()
        tmp.next=None
        sums=p1.data+p2.data+c
        tmp.data=sums%10
        c=sums//10
        p.next=tmp
        p=tmp
        p1=p1.next
        p2=p2.next
    if p1 is None:
        while p2 is not None:
            tmp=LNode()
            tmp.next=None
            sums=p2.data+c
            tmp.data=sums%10
            c=sums//10
            p.next=tmp
            p=tmp
            p2=p2.next
    if p2 is None:
        while p1 is not None:
            tmp=LNode()
            tmp.next=None
            sums=p1.data+c
            tmp.data=sums%10
            c=sums//10
            p.next=tmp
            p=tmp
            p1=p1.next
    if c==1:
        tmp=LNode()
        tmp.next=None
        tmp.data=1
        p.next=tmp
    return resultHead

if __name__=="__main__":
    i=1
    head1=LNode()
    head1.next=None
    head2=LNode()
    head2.next=None
    tmp=None
    cur=head1
    addResult=None
    while i < 7:
        tmp=LNode()
        tmp.data=i+2
        tmp.next=None
        cur.next=tmp
        i+=1
    cur=head2
    i=9
    while i>4:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i-=1
    print('\nhead1:', end=' ')
    cur=head1.next
    while cur is not None:
        print(cur.data, end=' ')
        cur=cur.next
    print('\nhead2:', end=' ')
    cur=head2.next
    while cur is not None:
        print(cur.data, end=' ')
        cur=cur.next
    addResult=add(head1,head2)
    print('\n相加后：', end=' ')
    cur=addResult.next
    while cur is not None:
        print(cur.data, end=' ')
        cur=cur.next