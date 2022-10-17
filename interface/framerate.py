class Framerate:
    def __init__(self):
        self.averageFrameTime = 0.0
        self.lastFrameTime = 0.0

    def get_text(self, delta_time):
        #calcula o intervalo entre frames
        self.lastFrameTime = delta_time
        self.averageFrameTime = (self.averageFrameTime + self.lastFrameTime)/2.0  
        return " {:10.2f} ms ".format(self.averageFrameTime*1000)