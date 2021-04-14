from index import CowsAndBulls


def start_game():
    game_window = CowsAndBulls()
    game_window.setup()


if __name__ == '__main__':
    start_game()


#     for turn in range(10):
#         guess = input('Enter number: ')
#         guess_list = list(str(guess))
#         # duplicates = duplicates_checker(guess_list)
#         result = play(guess_list, code)
#         print(result)
#         if result == 'Correct!':
#             break
#
#     print(f'You ran out of tries. The correct code is {code}')