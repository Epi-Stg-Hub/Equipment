##
## EPITECH PROJECT, 2024
## Hub
## File description:
## readme.py
##

class equipment:
    def __init__(self, equipment_content):
        self._equipment_name = equipment_content["equipement"]
        self._id = equipment_content["id"]
        self._rented = 0
        self._available = 0
        
        dispos = equipment_content["diponibilite"]
        for dispo in dispos:
            if dispo["status"] == "available":
                self._available = int(dispo["quantity"])
            elif dispo["status"] == "on loan":
                self._rented = int(dispo["quantity"])
        return

    def __str__(self) -> str:
        return ""

class category:
    def __init__(self, category_name: str, content):
        self._name = category_name
        self._equipments = []

    def __str__(self) -> str:
        return ""        

class inventory:
    def __init__(self, data):
        self._header = ""
        self._footer = ""
        self._categories = []
        self._rawData = data
        self._parse_data()
    
    def _parse_data(self):
        self._header = self._rawData["header"]
        for cate in self._rawData["sections"]:
            self._categories.append(category(cate, self._rawData["sections"][cate]))
        self._footer = self._rawData["footer"]
    
    def __str__(self) -> str:
        return ""

    