import random
def simulateTransmission():
    randNum = random.randint(0, 9)
    return randNum < 8

class Frame:
    def __init__(self, seqNum):
        self.seqNum = seqNum
        self.acked = False
        self.transmitted = False

def main():
    frames = [Frame(i) for i in range(FRAME_COUNT)]
    base = 0
    nextSeqNum = 0

    while base < FRAME_COUNT:
        for i in range(base, min(base + WINDOW_SIZE, FRAME_COUNT)):
            if not frames[i].transmitted:
                print("Sending Frame", frames[i].seqNum)
                frames[i].transmitted = True

        for i in range(base, min(base + WINDOW_SIZE, FRAME_COUNT)):
            if frames[i].transmitted and not frames[i].acked:
                if simulateTransmission():
                    print("Received ACK for Frame", frames[i].seqNum)
                    frames[i].acked = True
                    if i == base:
                        while base < FRAME_COUNT and frames[base].acked:
                            base += 1
                            nextSeqNum += 1
                else:
                    print("Frame", frames[i].seqNum, "lost, retransmitting...")
                    frames[i].transmitted = False

    print("All frames have been successfully transmitted!")


if __name__ == '__main__':
    WINDOW_SIZE = int(input("Enter window size: "))
    FRAME_COUNT = int(input("Enter frame count: "))
    random.seed()
    main()
