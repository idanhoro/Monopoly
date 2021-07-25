import se as se


class CommunityChest():
    def __init__(self):
        deck = [AdvanceToGo(), LifeInsurance(), BeautyContest(), BankError(), SaleOfStock(), TaxRefund(), Services(),
                Inherit(), XmasFund(), GrandOpera(), DoctorFee(), HospitalTax(), SchoolTax(), StreetRepairs(),
                GoToJail(), GetOutOfJail()
                ]


class AdvanceToGo:
    def __init__(self):
        self.card_text = 'Advance to go (collect 200$)'

    def active(self, player):
        player.balance += 200


class LifeInsurance:
    def __init__(self):
        self.card_text = 'Life insurance matures collect 100$'

    def active(self, player):
        player.balance += 100


class BeautyContest:
    def __init__(self):
        self.card_text = 'You have won second prize in an beauty contest collect 10$'

    def active(self, player):
        player.balance += 10


class BankError:
    def __init__(self):
        self.card_text = 'Bank error in your favor collect 200$'

    def active(self, player):
        player.balance += 200


class SaleOfStock:
    def __init__(self):
        self.card_text = 'From sale of stock you get 45$'

    def active(self, player):
        player.balance += 45


class TaxRefund:
    def __init__(self):
        self.card_text = 'Income tax refund collect 20$'

    def active(self, player):
        player.balance += 20


class Services:
    def __init__(self):
        self.card_text = 'Receive for services 25$'

    def active(self, player):
        player.balance += 25


class Inherit:
    def __init__(self):
        self.card_text = 'You inherit 100$'

    def active(self, player):
        player.balance += 100


class XmasFund:
    def __init__(self):
        self.card_text = 'Xmas fund matures collect 100$'

    def active(self, player):
        player.balance += 100


class GrandOpera:
    def __init__(self):
        self.card_text = 'Grand opera Opening collect 50$ from every player for opening night seats'

    def active(self, player):
        pass  # TODO: function to collect money from every player


class DoctorFee:
    def __init__(self):
        self.card_text = "Doctor's fee pay 50"

    def active(self, player):
        player.balance -= 50


class HospitalTax:
    def __init__(self):
        self.card_text = 'Pay Hospital 100$'

    def active(self, player):
        player.balance -= 100


class SchoolTax:
    def __init__(self):
        self.card_text = 'Pay school tax of 150$'

    def active(self, player):
        player.balance -= 150


class StreetRepairs:
    def __init__(self):
        self.card_text = 'You are assessed for street repairs, 40$ per house, 115$ per hotel'

    def active(self, player):
        pass  # TODO: function to calculate the repairs costs


class GoToJail:
    def __init__(self):
        self.card_text = 'Go to jail, go directly to jail, do not pass GO, do not collect 200$'

    def active(self, player):
        player.is_in_jail = True
        player.location = 10  # jail block


class GetOutOfJail:
    def __init__(self):
        self.card_ = 'Get out of jail free (This card may be kept until needed, or sold'

    def active(self, player):
        player.is_in_jail = False
