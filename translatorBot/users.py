from dataclasses import dataclass

@dataclass
class User:
     id: int
     name: str
     user_id: int
     translateDate: str
     directionOfTranslation: str
     original: str
     translation: str
     inputType: str
    
     def __init__(self, name, user_id,translateDate,directionOfTranslation,original,translation,inputType):
        self.name = name
        self.user_id = user_id
        self.translateDate = translateDate
        self.directionOfTranslation = directionOfTranslation
        self.original = original
        self.translation = translation
        self.inputType = inputType


