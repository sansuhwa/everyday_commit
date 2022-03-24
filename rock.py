"""
Course: Introduction to Python Programming
student Name: suwon Choi
"""
#%% 
import random
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%
def HumanPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''
    while True:
        while True:
            print('Please select rock, sissors, paper. Enter q or quit to quit the game. Enger g ro game to see the GameRecord.')
            choice = input()
            if choice in ['rock', 'paper', 'scissors', 'game', 'quit', 'r', 'p', 's', 'g', 'q']:
                break

        if choice in ['game', 'g']:
            PrintGamerecord(GameRecord=GameRecord)
            continue

        if choice in ['quit', 'q']:
            return 'Q'
        
        if choice in ['r', 'rock']:
            return 'r'

        if choice in ['s', 'scissors']:
            return 's'

        if choice in ['p', 'paper']:
            return 'p'

# %%
def ComputerPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''
    # return random.choice(['r', 's', 'p'])
    # weighted
    human_record = GameRecord[0]
    count_r, count_p, count_s = 0, 0, 0
    count_r = human_record.count('r')
    count_p = human_record.count('p')
    count_s = human_record.count('s')
    print(count_s, count_r, count_p)
    if count_r + count_p + count_s == 0:
        return random.choice(['r', 's', 'p'])

    return random.choices(['r', 's', 'p'], weights=[count_s, count_p, count_r])[0]

# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''
    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
        return 0

    # 컴퓨터 이기는 경우
    '''
    r, s
    s, p
    p, r
    '''
    out = [ChoiceOfComputerPlayer, ChoiceOfHumanPlayer]
    # [r, s]
    if out in [['r', 's'], ['s', 'p'], ['p', 'r']]:
        return 1
    
    # 사람이 이기는 경우
    '''
    s, r
    p, s
    r, p
    '''
    if out in [['s', 'r'], ['p', 's'], ['r', 'p']]:
        return 2


# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''
    result = ''
    if Outcome == 0:
        result = 'Draw'
    if Outcome == 1:
        result = 'Computer wins!'
    if Outcome == 2:
        result = 'Human wins!'

    print(f'''
    Outcome: {result}
    Player:  {ChoiceOfHumanPlayer}
    Computer:  {ChoiceOfComputerPlayer}
    ''')

# %%
def UpdateGamerecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
    # GameRecord => [
      # ['p', 's', 'p', 's'],  # human  -> GameRecord[0]
      # ['s', 'r', 'p'],  # computer
      # [1, 0, 0],  # outcome
    # ]
    # ChoiceOfHumanPlayer => s
    # ChoiceOfComputerPlayer => r, s, p
    human_list = GameRecord[0]
    computer_list = GameRecord[1]
    outcome_list = GameRecord[2]

    human_list.append(ChoiceOfHumanPlayer)
    computer_list.append(ChoiceOfComputerPlayer)
    outcome_list.append(Outcome)
    return GameRecord


# %%
def PrintGamerecord(GameRecord):
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
    human_list, com_list, outcome_list = GameRecord
    print(GameRecord)
    for i in range(len(outcome_list)):
        # 0, 1, 2
        human = human_list[i]
        com = com_list[i]
        outcome = outcome_list[i]

        if human == 'p':
            print('paper', end=' ')
        if human == 's':
            print('scissor', end=' ')
        if human == 'r':
            print('rock', end=' ')

        if com == 'p':
            print('paper', end=' ')
        if com == 's':
            print('scissor', end=' ')
        if com == 'r':
            print('rock', end=' ')

        if outcome == 0:
            print('a draw/tie', end=' ')

        if outcome == 1:
            print('computer wins', end=' ')

        if outcome == 2:
            print('human wins', end=' ')
        
        print('\n')


# %% the game
def PlayGame():
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''
    # 기록지를 생성
    # record = [
      # ['p', 's', 'p'],  # human
      # ['s', 'r', 'p'],  # computer
      # ['1', '1', '0'],  # outcome
    # ]

    # while 반복

    # human_play = Humanplayer를 실행시킨다 (안에서 game인 경우 PrintGamerecord를 실행시키고 다시 받기)
    # human_play -> q, r, s, p
        # hman_play가 quit인 경우
        # print('game over') 이후 함수 종료

    # computer_play = ComputerPlayer를 실행시킨다 (r, s, P) -> weighted from human resulit
    # outcome = Judge(computer_play, human_play)
    # PrintOutcome(outcome, computer_play, human_play)
    # UpdateGamerecord(record, computer_play, human_play, outcome)
    record = [[], [], []]  # human, computer, outcome

    while True:
        # human plays a game
        # will be one of [Q, r, s, P]
        human_play = HumanPlayer(GameRecord=record)
        if human_play == 'Q':
            break

        # computer plays a game
        # one of [r, s, P]
        computer_play = ComputerPlayer(GameRecord=record)
        # judge outcome
        outcome = Judge(ChoiceOfComputerPlayer=computer_play, ChoiceOfHumanPlayer=human_play)
        # print outcome
        PrintOutcome(Outcome=outcome, ChoiceOfComputerPlayer=computer_play, ChoiceOfHumanPlayer=human_play)
        # update game record
        record = UpdateGamerecord(GameRecord=record, ChoiceOfComputerPlayer=computer_play, ChoiceOfHumanPlayer=human_play, Outcome=outcome)
    
    print('game over')


# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()
