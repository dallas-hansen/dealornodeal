from classes.banker import Banker
from setup import create_cases, load_settings

def play_game(settings):
    cases = create_cases(settings)
    banker = Banker(settings)
    
    print("Welcome to Deal or No Deal!")
    chosen_case = int(input(f"Choose your case (1-{len(cases)}): "))
    
    player_case = cases[chosen_case - 1]
    remaining_cases = [c for c in cases if c != player_case]
    
    for round in range(settings['game_structure']['num_rounds']):
        print(f"\nRound {round + 1}")
        print("Remaining cases:")
        unopened = [c for c in remaining_cases if not c.opened]
        for case in unopened:
            print(f"Case {case.case_number}")
        
        # Player opens a case
        case_to_open = int(input("Select a case to open: "))
        case = next(c for c in unopened if c.case_number == case_to_open)
        print(f"Case {case.case_number} contains: ${case.open()}")
        
        # Banker makes an offer
        offer = banker.calculate_offer(unopened)
        print(f"Banker's offer: ${offer}")
        deal = input("Deal or No Deal? (deal/no): ")
        if deal.lower() == 'deal':
            print(f"You walk away with ${offer}!")
            return
    
    print(f"\nYour case contained: ${player_case.open()}")
    
if __name__ == "__main__":
    settings = load_settings()
    play_game(settings)
