import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if self.is_empty():
            print("No entries in queue.")
            return None

        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]
        print(f"🎉 Winner is: {winner} 🎉")

        for _ in range(winner_index + 1):
            removed = self.dequeue()
            print(f"Dequeued: {removed}")

        return winner
