dict = {
    "businessCategories_id": 1,
    "products_name": "ماركة بديلة - طقم تيل الفرامل أمامي مصري لادا جرانتا (2015 - 2021)",
    "description": "طقم تيل فرامل  ( قطع غيار--->الفرامل--->تيل الفرامل )",
    "brand_name": "ماركة بديلة",
    "address": None,
    "products_img": "https://yourparts-staging-v2.s3.amazonaws.com/P2022/1F.png",
    "madeIn": "Egypt",
    "price": 465,
    "type": "After Market",
    "assembly_kit": True,
    "frontOrRear": "FRONT",
    "created_at": "2024-04-08T02:32:17.664Z",
    "enabled": True,
    "is_offer": False
}
class replacement_part:
    def __init__(self, product_name, description,  products_img, madeIn ,price, type, assembly_kit, frontOrRear=None, enabled = True, is_offer=False ,address = None,) -> None:
        self.product_name = product_name
        self.description = description
        self.products_img = products_img
        self.madeIn = madeIn
        self.price = price
        self.type = type
        self.assembly_kit = assembly_kit
        self.frontOrRear = frontOrRear
        self.enabled = enabled
        self.is_offer = is_offer
        self.address = address
    