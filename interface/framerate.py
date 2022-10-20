# ╔═════════════════════════════════════════════╗
# ║  Parte Programada Por: JOSE DANIEL C. GOMES ║
# ║                                             ║ 
# ╚═════════════════════════════════════════════╝

class Framerate:

    def __init__(self):
        self.total_time = 0
        self.chronometer = 0.5 #segundos
        self.total_frames = 1
        self.frame_rate = 1.0

    def get_text(self, delta_time):
        self.total_frames += 1
        self.total_time += delta_time

        if self.total_time >= self.chronometer:
            self.frame_rate = self.total_frames/self.chronometer
            self.total_time = 0
            self.total_frames = 0
        
        return "{:10.2f} fps {:10.2f} ms ".format(
            self.frame_rate, 1000/self.frame_rate if self.frame_rate != 0 else "??")
