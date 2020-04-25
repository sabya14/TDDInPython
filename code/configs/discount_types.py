import enum


class DiscountTypes(enum.Enum):
    Percentage = "percent"
    User = "user"
    BoughtTogether = "bought_together"
