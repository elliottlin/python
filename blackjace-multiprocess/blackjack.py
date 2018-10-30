import random
import multiprocessing
import math
import time

simulations = 100 * 1000
num_decks = 4
shffle_prec = 75

def simulate(queue, batch_size):
    deck = []

    def new_deck():
        std_deck = [
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
        ]

        std_deck = std_deck * num_decks

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
            return -1

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
            return 1

        if d_sum == p_sum:
            return 0

        if d_sum > p_sum:
            return -1

        if d_sum < p_sum:
            return 1

    deck = new_deck()

    win, draw, lose = 0, 0, 0
    for i in range(0, batch_size):
        if (float(len(deck))/(52*num_decks)) * 100 < shffle_prec:
            deck = new_deck()

        result = play_hand()

        if result == 1:
            win += 1

        if result == 0:
            draw += 1

        if result == -1:
            lose += 1

    queue.put([win, draw, lose])
if __name__ == '__main__':
    # freeze_support()
    start_time = time.time()

    # simulate
    cpus = multiprocessing.cpu_count()
    batch_size = int(math.ceil(simulations/ float(cpus)))

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

    anchor = 15
    print("{0: >20}  {1}".format("cores", cpus))
    print("{0: >20}  {1}".format("total simulations", simulations))
    print("{0: >20}  {1}".format("sim/s", (float(simulations)/finish_time)))
    print("{0: >20}  {1}".format("time", finish_time))
    print("{0: >20}  {1}".format("win", (win/float(simulations) * 100)))
    print("{0: >20}  {1}".format("draw", (draw/float(simulations) * 100)))
    print("{0: >20}  {1}".format("lose", (lose/float(simulations) * 100)))
