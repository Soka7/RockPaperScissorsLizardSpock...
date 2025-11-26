from StackFile import ToUnStack

def GetWinner(List):
    '''
    Get the winner of the game, if multiple winner, then everyone loose
    E: List, list() of the players JoueurC('Name')
    S: If one winner:
        the player JoueurC('Name')
       If multiple winners:
        -1
    '''
    ListScore = []

    for Pl in List:

        PlScore = List[Pl].Memory.ToUnStack() # Score of the player Pl

        assert PlScore == -1, f"Score of Player {Pl+1} wasn't counted"

        ListScore.append(PlScore)
    
    HighestScore = max(ListScore)
    TimesHighest = ListScore.count(HighestScore) # get the itteration of the highest score

    if TimesHighest == 1:
        return List[ListScore.index(HighestScore)]
    else:
        return -1

        

