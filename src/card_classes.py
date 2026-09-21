
###base class for a card, featuring attributes that are shared by all cards

class card():
    def __init__(self, id, name, card_type, tags, rule_text):
        self.id = id
        self.name = name
        self.card_type = card_type
        self.tags = tags
        self.rule_text = rule_text

###prints information on the card
    def printinfo(self):
        print("ID: ", self.id)
        print("NAME: ", self.name)
        print("TYPE: ", self.card_type)
        print("TAGS: ", self.tags)
        print("RULE TEXT: ", self.rule_text)

###unit subclass

class unit(card):
    def __init__(self, id, name, card_type, tags, rule_text, ep_cost, atk_power, hit_points):
        super().__init__(id, name, card_type, tags, rule_text)
        self.ep_cost = ep_cost
        self.atk_power = atk_power
        self.hit_points = hit_points
    def printinfo(self):
            print("ID: ", self.id)
            print("NAME: ", self.name)
            print("TYPE: ", self.card_type)
            print("TAGS: ", self.tags)
            print("ENERGY POINT COST: ", self.ep_cost)
            print("ATTACK POWER: ", self.atk_power)
            print("HIT POINTS: ", self.hit_points)
            print("RULE TEXT: ", self.rule_text)

###building subclass 
class building(card):
    def __init__(self, id, name, card_type, tags, rule_text, ep_cost, hit_points):
        super().__init__(id, name, card_type, tags, rule_text)
        self.ep_cost = ep_cost
        self.hit_points = hit_points
    def printinfo(self):
            print("ID: ", self.id)
            print("NAME: ", self.name)
            print("TYPE: ", self.card_type)
            print("TAGS: ", self.tags)
            print("ENERGY POINT COST: ", self.ep_cost)
            print("HIT POINTS: ", self.hit_points)
            print("RULE TEXT: ", self.rule_text)

###ability subclass
class ability(card):
    def __init__(self, id, name, card_type, tags, rule_text, ep_cost):
        super().__init__(id, name, card_type, tags, rule_text)
        self.ep_cost = ep_cost
    def printinfo(self):
            print("ID: ", self.id)
            print("NAME: ", self.name)
            print("TYPE: ", self.card_type)
            print("TAGS: ", self.tags)
            print("ENERGY POINT COST: ", self.ep_cost)
            print("RULE TEXT: ", self.rule_text)

####testing







        