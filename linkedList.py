class Node :
    def __init__(self, value, prev = None) :
        self.prev = prev
        self.value = value
        self.next = None
 
class BrowserHistory :
    # 초기 값을 head, current에 맵핑한다.
    def __init__(self, value) :
        self.head = self.current = Node(value)
    
    # 방문하면 현재 값의 nuxt에 값을 넣고, 현재 위치를 새로 들어온 값으로 교체한다.
    def visit(self, url ) :
        self.current = self.current.next = Node(url, self.current)
    
    # 뒤로 이동 할 때 prev가 None 아니면서 steps가 0이 아닐 때까지 이동하고 값을 리턴한다.
    def back(self, steps) :
        while self.prev != None and 0 < steps :
            steps -= 1
            self.current = self.current.prev
        
        return self.current.value;

    # 앞으로 이동할 때 next가 None이 아니면서 steps가 0이 될 때까지 이동하고 값을 리턴한다.
    def forward(self, steps) :
        while self.next != None and 0 < steps :
            steps -= 1
            self.current = self.current.next
        
        return self.current.value;
        