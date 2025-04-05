class Teams:
    def __init__(self, division):
        self.division = division
        self.teams = {}

    def add_coach(self, coach, poke_list):
        for poke in poke_list:
            if self.teams.get(poke, -1) != -1:
                return False

        for poke in poke_list:
            self.teams[poke] = coach

        return True

    def add_poke(self, coach, poke):
        if self.teams.get(poke, -1) != -1:
            return False

        self.teams[poke] = coach

    def remove_coach(self, the_coach):
        for poke, coach in self.teams.items():
            if coach == the_coach:
                self.teams.pop(poke)

        return True

    def remove_poke(self, poke):
        if self.teams.get(poke, -1) == -1:
            return False

        self.teams.pop(poke)
        return True

    def get_coach(self, poke_list):
        possible_coaches = {}
        for poke in poke_list:
            if self.teams.get(poke, -1) == -1:
                continue
            possible_coaches[self.teams.get(poke)] = possible_coaches.get(self.teams.get(poke), 0) + 1

        coach = None
        likelihood = -1

        if len(possible_coaches) == 0:
            return coach

        for poss_coach, possibility in possible_coaches.items():
            if possibility > likelihood:
                coach = poss_coach

        return coach
