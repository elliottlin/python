import random
import multiprocessing
import math
import time

SIMLULATIONS = 100 * 1000
NUM_DECKS = 4
SHUFFLE_PERC = 75

WIN = 1
DRAW = 0
LOSE = -1

def simulate(queue, batch_size):
    deck = []

    def new_deck():
        std_deck = [
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        ]
        std_deck = std_deck * NUM_DECKS
        random.shuffle(std_deck)
        return std_deck[:]

    def play_hand():
        dealer_cards = []
        player_cards = []

        # init cards
        player_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))
        player_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))

        # deal player to 12 or higher
        while sum(player_cards) < 12:
            player_cards.append(deck.pop(0))

        p_sum = sum(player_cards)
        if p_sum > 21:
            return LOSE

        # deal dealer on soft 17
        while sum(dealer_cards) < 18:
            leave = False
            # check for soft 17
            if sum(dealer_cards) == 17:
                leave = True

                for i, card in enumerate(dealer_cards):
                    if card == 11:
                        leave = False
                        dealer_cards[i] = 1
                        break
            if leave:
                break
            dealer_cards.append(deck.pop(0))

        d_sum = sum(dealer_cards)

        if d_sum > 21:
            return WIN

        if d_sum == p_sum:
            return DRAW

        if d_sum > p_sum:
            return LOSE

        if d_sum < p_sum:
            return WIN

    deck = new_deck()
    win, draw, lose = 0, 0, 0
    for _ in range(0, batch_size):
        if (float(len(deck))/(52*NUM_DECKS)) * 100 < SHUFFLE_PERC:
            deck = new_deck()
        result = play_hand()

        if result == WIN:
            win += 1
        elif result == DRAW:
            draw += 1
        elif result == LOSE:
            lose += 1

    queue.put([win, draw, lose])


if __name__ == '__main__':
    start_time = time.time()

    # simulate
    cpus = multiprocessing.cpu_count()
    batch_size = int(math.ceil(SIMLULATIONS/ float(cpus)))

    queue = multiprocessing.Queue()

    processes = []

    for i in range(0, cpus):
        process = multiprocessing.Process(
            target=simulate,
            args=(queue, batch_size)
        )
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()

    finish_time = time.time() - start_time

    win, draw, lose = 0, 0, 0

    for i in range(0, cpus):
        results = queue.get()
        win += results[0]
        draw += results[1]
        lose += results[2]

    print("{0: >20}  {1}".format("cores", cpus))
    print("{0: >20}  {1}".format("total simulations", SIMLULATIONS))
    print("{0: >20}  {1}".format("sim/s", (float(SIMLULATIONS)/finish_time)))
    print("{0: >20}  {1}".format("time", finish_time))
    print("{0: >20}  {1}".format("win", (win/float(SIMLULATIONS) * 100)))
    print("{0: >20}  {1}".format("draw", (draw/float(SIMLULATIONS) * 100)))
    print("{0: >20}  {1}".format("lose", (lose/float(SIMLULATIONS) * 100)))
