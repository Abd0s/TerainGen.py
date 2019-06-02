import time
import random

def setup():
    size(1000, 1000)
    background(0, 0, 0)
    

def draw():
    time.sleep(1)
    container.container_list = [random.randint(0, 9) for x in container.container_list]
    container.display()


    
class Container():
    
    def __init__(self, container_size, square_size):
        #container
        self.container_size = container_size
        self.square_size = square_size
        
        #internals
        self.container_list = []
        for i in range(self.container_size**2):
            self.container_list.append(i)
        
        
    def display(self):
        '''
        Takes a list of values of the container, draws these to the screen
        '''
        
        self.itterater_count = 0
        self.row_count = 0
            
        for i in self.container_list:
            #spacer
            if self.itterater_count == self.container_size:
                self.itterater_count = 0
                self.row_count = self.row_count + 1
            
            fill(150, 255-(i*(255/max(self.container_list))), 255-(i*(255/max(self.container_list))))
            rect(self.itterater_count*self.square_size, self.row_count*self.square_size, self.square_size, self.square_size)
            fill(0, 102, 153)
            textSize(1.2/float(len(str(i)))*15)
            text(str(i), (self.itterater_count*self.square_size)+self.square_size/2-5, ((self.row_count*self.square_size)+self.square_size)-self.square_size/2+5)
            self.itterater_count = self.itterater_count + 1
            

    
container = Container(50, 20)

    
