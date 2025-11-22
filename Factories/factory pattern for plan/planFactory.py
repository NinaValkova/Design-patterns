from pydoc import plain
from typing import Optional
from planType import PlanType
from domesticPlan import DomesticPlan
from commercialPlan import CommercialPlan
from institutionalPlan import InstitutionalPlan
from plan import Plan

class PlanFactory:
    def __init__(self) -> None:
        self.planType = {"DOMESTICPLAN": PlanType.DOMESTICPLAN,
                         "COMMERCIALPLAN": PlanType.COMMERCIALPLAN,
                          "INSTITUTIONALPLAN": PlanType.INSTITUTIONALPLAN}

    def getPlan(self, type)-> Optional[Plan]:
        value = self.planType.get(type.upper())
        
        plan = None
        if value ==  PlanType.DOMESTICPLAN:
            plain = DomesticPlan()
        elif value == PlanType.COMMERCIALPLAN:
            plain = CommercialPlan()
        elif value == PlanType.INSTITUTIONALPLAN:
            plain = InstitutionalPlan()
            
        return plain    

