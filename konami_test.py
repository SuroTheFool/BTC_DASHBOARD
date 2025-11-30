class KonamiDetector:

    def __init__(self):
        self.key_sequence = []
        self.target = ["up","down","right"]
    def feed(self,key):
        self.key_sequence.append(key)
        self.key_sequence = self.key_sequence[-len(self.target):]
        return self.key_sequence == self.target

if __name__ == "__main__":
    kd = KonamiDetector()
    for key in ["up","down","right"]:
        unlock = kd.feed(key)
        print(key, unlock)