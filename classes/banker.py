class Banker:
    def __init__(self, settings):
        self.settings = settings
    
    def calculate_offer(self, remaining_cases):
        avg = sum(c.prize for c in remaining_cases) / len(remaining_cases)
        variance = self.settings['banker_settings']['round_offer_variance']
        return round(avg * (self.settings['banker_settings']['offer_percentage'] / 100) + variance)