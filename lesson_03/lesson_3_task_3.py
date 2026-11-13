from address import Address
from mailing import Mailing

address1 = Address(614031, "Пермь", "Костычева", 16, 88)
address2 = Address(156000, "Кострома", "Советская", 104, 27)

mailing = (Mailing(to_address=address1,
                   from_address=address2, cost=712, track="igGYwi983257"))

print(mailing)
