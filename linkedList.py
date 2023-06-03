class Node :
    def __init__(self, value, prev = None) :
        self.prev = prev
        self.value = value
        self.next = None

class BrowserHistory :
    def __init__(self, value) :
        self.head = self.current = Node(value)
    
    def visit(self, url ) :
        self.current = self.current.next = Node(url, self.current)
        
    def back(self, steps) :
        while self.prev != None and 0 < steps :
            steps -= 1
            self.current = self.current.prev
        
        return self.current.value;

    def forward(self, steps) :
        while self.next != None and 0 < steps :
            steps -= 1
            self.current = self.current.next
        
        return self.current.value;
        