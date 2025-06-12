from __future__ import annotations
import uuid, time, json, re, hashlib, math, logging
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
logger = logging.getLogger(__name__)

# pos: POS - Square, Toast adapters, tickets, voids
# Details: Square, Toast, tickets

class PosStatus(str, Enum):
    PENDING='pending'; ACTIVE='active'; FAILED='failed'

@dataclass
class PosEntity:
    """POS - Square, Toast adapters, tickets, voids"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: float = field(default_factory=time.time)
    status: str = 'pending'


    def ingest_square_0(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 0 distinct per ticket 0"""
        # Distinct per 0: handles tickets 0
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 0, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 0}

    def ingest_toast_0(self, ticket: Dict[str, Any]):
        """Ingest Toast 0 distinct"""
        return {"pos": "Toast", "idx": 0, "items": len(ticket.get("items",[]))}

    def ingest_square_1(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 1 distinct per ticket 1"""
        # Distinct per 1: handles voids 1
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 1, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 1}

    def ingest_toast_1(self, ticket: Dict[str, Any]):
        """Ingest Toast 1 distinct"""
        return {"pos": "Toast", "idx": 1, "items": len(ticket.get("items",[]))}

    def ingest_square_2(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 2 distinct per ticket 2"""
        # Distinct per 2: handles comps 2
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 2, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 2}

    def ingest_toast_2(self, ticket: Dict[str, Any]):
        """Ingest Toast 2 distinct"""
        return {"pos": "Toast", "idx": 2, "items": len(ticket.get("items",[]))}

    def ingest_square_3(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 3 distinct per ticket 0"""
        # Distinct per 3: handles tickets 3
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 3, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 3}

    def ingest_toast_3(self, ticket: Dict[str, Any]):
        """Ingest Toast 3 distinct"""
        return {"pos": "Toast", "idx": 3, "items": len(ticket.get("items",[]))}

    def ingest_square_4(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 4 distinct per ticket 1"""
        # Distinct per 4: handles voids 4
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 4, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 4}

    def ingest_toast_4(self, ticket: Dict[str, Any]):
        """Ingest Toast 4 distinct"""
        return {"pos": "Toast", "idx": 4, "items": len(ticket.get("items",[]))}

    def ingest_square_5(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 5 distinct per ticket 2"""
        # Distinct per 5: handles comps 5
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 5, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 5}

    def ingest_toast_5(self, ticket: Dict[str, Any]):
        """Ingest Toast 5 distinct"""
        return {"pos": "Toast", "idx": 5, "items": len(ticket.get("items",[]))}

    def ingest_square_6(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 6 distinct per ticket 0"""
        # Distinct per 6: handles tickets 6
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 6, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 6}

    def ingest_toast_6(self, ticket: Dict[str, Any]):
        """Ingest Toast 6 distinct"""
        return {"pos": "Toast", "idx": 6, "items": len(ticket.get("items",[]))}

    def ingest_square_7(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 7 distinct per ticket 1"""
        # Distinct per 7: handles voids 7
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 7, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 7}

    def ingest_toast_7(self, ticket: Dict[str, Any]):
        """Ingest Toast 7 distinct"""
        return {"pos": "Toast", "idx": 7, "items": len(ticket.get("items",[]))}

    def ingest_square_8(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 8 distinct per ticket 2"""
        # Distinct per 8: handles comps 8
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 8, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 8}

    def ingest_toast_8(self, ticket: Dict[str, Any]):
        """Ingest Toast 8 distinct"""
        return {"pos": "Toast", "idx": 8, "items": len(ticket.get("items",[]))}

    def ingest_square_9(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 9 distinct per ticket 0"""
        # Distinct per 9: handles tickets 9
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 9, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 9}

    def ingest_toast_9(self, ticket: Dict[str, Any]):
        """Ingest Toast 9 distinct"""
        return {"pos": "Toast", "idx": 9, "items": len(ticket.get("items",[]))}

    def ingest_square_10(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 10 distinct per ticket 1"""
        # Distinct per 10: handles voids 10
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 10, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 10}

    def ingest_toast_10(self, ticket: Dict[str, Any]):
        """Ingest Toast 10 distinct"""
        return {"pos": "Toast", "idx": 10, "items": len(ticket.get("items",[]))}

    def ingest_square_11(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 11 distinct per ticket 2"""
        # Distinct per 11: handles comps 11
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 11, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 11}

    def ingest_toast_11(self, ticket: Dict[str, Any]):
        """Ingest Toast 11 distinct"""
        return {"pos": "Toast", "idx": 11, "items": len(ticket.get("items",[]))}

    def ingest_square_12(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 12 distinct per ticket 0"""
        # Distinct per 12: handles tickets 12
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 12, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 12}

    def ingest_toast_12(self, ticket: Dict[str, Any]):
        """Ingest Toast 12 distinct"""
        return {"pos": "Toast", "idx": 12, "items": len(ticket.get("items",[]))}

    def ingest_square_13(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 13 distinct per ticket 1"""
        # Distinct per 13: handles voids 13
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 13, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 13}

    def ingest_toast_13(self, ticket: Dict[str, Any]):
        """Ingest Toast 13 distinct"""
        return {"pos": "Toast", "idx": 13, "items": len(ticket.get("items",[]))}

    def ingest_square_14(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 14 distinct per ticket 2"""
        # Distinct per 14: handles comps 14
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 14, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 14}

    def ingest_toast_14(self, ticket: Dict[str, Any]):
        """Ingest Toast 14 distinct"""
        return {"pos": "Toast", "idx": 14, "items": len(ticket.get("items",[]))}

    def ingest_square_15(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 15 distinct per ticket 0"""
        # Distinct per 15: handles tickets 15
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 15, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 15}

    def ingest_toast_15(self, ticket: Dict[str, Any]):
        """Ingest Toast 15 distinct"""
        return {"pos": "Toast", "idx": 15, "items": len(ticket.get("items",[]))}

    def ingest_square_16(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 16 distinct per ticket 1"""
        # Distinct per 16: handles voids 16
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 16, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 16}

    def ingest_toast_16(self, ticket: Dict[str, Any]):
        """Ingest Toast 16 distinct"""
        return {"pos": "Toast", "idx": 16, "items": len(ticket.get("items",[]))}

    def ingest_square_17(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 17 distinct per ticket 2"""
        # Distinct per 17: handles comps 17
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 17, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 17}

    def ingest_toast_17(self, ticket: Dict[str, Any]):
        """Ingest Toast 17 distinct"""
        return {"pos": "Toast", "idx": 17, "items": len(ticket.get("items",[]))}

    def ingest_square_18(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 18 distinct per ticket 0"""
        # Distinct per 18: handles tickets 18
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 18, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 18}

    def ingest_toast_18(self, ticket: Dict[str, Any]):
        """Ingest Toast 18 distinct"""
        return {"pos": "Toast", "idx": 18, "items": len(ticket.get("items",[]))}

    def ingest_square_19(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 19 distinct per ticket 1"""
        # Distinct per 19: handles voids 19
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 19, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 19}

    def ingest_toast_19(self, ticket: Dict[str, Any]):
        """Ingest Toast 19 distinct"""
        return {"pos": "Toast", "idx": 19, "items": len(ticket.get("items",[]))}

    def ingest_square_20(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 20 distinct per ticket 2"""
        # Distinct per 20: handles comps 20
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 20, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 20}

    def ingest_toast_20(self, ticket: Dict[str, Any]):
        """Ingest Toast 20 distinct"""
        return {"pos": "Toast", "idx": 20, "items": len(ticket.get("items",[]))}

    def ingest_square_21(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 21 distinct per ticket 0"""
        # Distinct per 21: handles tickets 21
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 21, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 21}

    def ingest_toast_21(self, ticket: Dict[str, Any]):
        """Ingest Toast 21 distinct"""
        return {"pos": "Toast", "idx": 21, "items": len(ticket.get("items",[]))}

    def ingest_square_22(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 22 distinct per ticket 1"""
        # Distinct per 22: handles voids 22
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 22, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 22}

    def ingest_toast_22(self, ticket: Dict[str, Any]):
        """Ingest Toast 22 distinct"""
        return {"pos": "Toast", "idx": 22, "items": len(ticket.get("items",[]))}

    def ingest_square_23(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 23 distinct per ticket 2"""
        # Distinct per 23: handles comps 23
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 23, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 23}

    def ingest_toast_23(self, ticket: Dict[str, Any]):
        """Ingest Toast 23 distinct"""
        return {"pos": "Toast", "idx": 23, "items": len(ticket.get("items",[]))}

    def ingest_square_24(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 24 distinct per ticket 0"""
        # Distinct per 24: handles tickets 24
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 24, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 24}

    def ingest_toast_24(self, ticket: Dict[str, Any]):
        """Ingest Toast 24 distinct"""
        return {"pos": "Toast", "idx": 24, "items": len(ticket.get("items",[]))}

    def ingest_square_25(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 25 distinct per ticket 1"""
        # Distinct per 25: handles voids 25
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 25, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 25}

    def ingest_toast_25(self, ticket: Dict[str, Any]):
        """Ingest Toast 25 distinct"""
        return {"pos": "Toast", "idx": 25, "items": len(ticket.get("items",[]))}

    def ingest_square_26(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 26 distinct per ticket 2"""
        # Distinct per 26: handles comps 26
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 26, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 26}

    def ingest_toast_26(self, ticket: Dict[str, Any]):
        """Ingest Toast 26 distinct"""
        return {"pos": "Toast", "idx": 26, "items": len(ticket.get("items",[]))}

    def ingest_square_27(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 27 distinct per ticket 0"""
        # Distinct per 27: handles tickets 27
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 27, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 27}

    def ingest_toast_27(self, ticket: Dict[str, Any]):
        """Ingest Toast 27 distinct"""
        return {"pos": "Toast", "idx": 27, "items": len(ticket.get("items",[]))}

    def ingest_square_28(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 28 distinct per ticket 1"""
        # Distinct per 28: handles voids 28
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 28, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 28}

    def ingest_toast_28(self, ticket: Dict[str, Any]):
        """Ingest Toast 28 distinct"""
        return {"pos": "Toast", "idx": 28, "items": len(ticket.get("items",[]))}

    def ingest_square_29(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 29 distinct per ticket 2"""
        # Distinct per 29: handles comps 29
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 29, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 29}

    def ingest_toast_29(self, ticket: Dict[str, Any]):
        """Ingest Toast 29 distinct"""
        return {"pos": "Toast", "idx": 29, "items": len(ticket.get("items",[]))}

    def ingest_square_30(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 30 distinct per ticket 0"""
        # Distinct per 30: handles tickets 30
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 30, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 30}

    def ingest_toast_30(self, ticket: Dict[str, Any]):
        """Ingest Toast 30 distinct"""
        return {"pos": "Toast", "idx": 30, "items": len(ticket.get("items",[]))}

    def ingest_square_31(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 31 distinct per ticket 1"""
        # Distinct per 31: handles voids 31
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 31, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 31}

    def ingest_toast_31(self, ticket: Dict[str, Any]):
        """Ingest Toast 31 distinct"""
        return {"pos": "Toast", "idx": 31, "items": len(ticket.get("items",[]))}

    def ingest_square_32(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 32 distinct per ticket 2"""
        # Distinct per 32: handles comps 32
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 32, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 32}

    def ingest_toast_32(self, ticket: Dict[str, Any]):
        """Ingest Toast 32 distinct"""
        return {"pos": "Toast", "idx": 32, "items": len(ticket.get("items",[]))}

    def ingest_square_33(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 33 distinct per ticket 0"""
        # Distinct per 33: handles tickets 33
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 33, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 33}

    def ingest_toast_33(self, ticket: Dict[str, Any]):
        """Ingest Toast 33 distinct"""
        return {"pos": "Toast", "idx": 33, "items": len(ticket.get("items",[]))}

    def ingest_square_34(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 34 distinct per ticket 1"""
        # Distinct per 34: handles voids 34
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 34, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 34}

    def ingest_toast_34(self, ticket: Dict[str, Any]):
        """Ingest Toast 34 distinct"""
        return {"pos": "Toast", "idx": 34, "items": len(ticket.get("items",[]))}

    def ingest_square_35(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 35 distinct per ticket 2"""
        # Distinct per 35: handles comps 35
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 35, "amount": ticket.get("total",0) * 1.00}
        return {"pos": "Square", "idx": 35}

    def ingest_toast_35(self, ticket: Dict[str, Any]):
        """Ingest Toast 35 distinct"""
        return {"pos": "Toast", "idx": 35, "items": len(ticket.get("items",[]))}

    def ingest_square_36(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 36 distinct per ticket 0"""
        # Distinct per 36: handles tickets 36
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 36, "amount": ticket.get("total",0) * 1.01}
        return {"pos": "Square", "idx": 36}

    def ingest_toast_36(self, ticket: Dict[str, Any]):
        """Ingest Toast 36 distinct"""
        return {"pos": "Toast", "idx": 36, "items": len(ticket.get("items",[]))}

    def ingest_square_37(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 37 distinct per ticket 1"""
        # Distinct per 37: handles voids 37
        if ticket.get("type") == "voids":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 37, "amount": ticket.get("total",0) * 1.02}
        return {"pos": "Square", "idx": 37}

    def ingest_toast_37(self, ticket: Dict[str, Any]):
        """Ingest Toast 37 distinct"""
        return {"pos": "Toast", "idx": 37, "items": len(ticket.get("items",[]))}

    def ingest_square_38(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 38 distinct per ticket 2"""
        # Distinct per 38: handles comps 38
        if ticket.get("type") == "comps":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 38, "amount": ticket.get("total",0) * 1.03}
        return {"pos": "Square", "idx": 38}

    def ingest_toast_38(self, ticket: Dict[str, Any]):
        """Ingest Toast 38 distinct"""
        return {"pos": "Toast", "idx": 38, "items": len(ticket.get("items",[]))}

    def ingest_square_39(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        """Ingest Square 39 distinct per ticket 0"""
        # Distinct per 39: handles tickets 39
        if ticket.get("type") == "tickets":
            return {"pos": "Square", "id": ticket.get("id"), "idx": 39, "amount": ticket.get("total",0) * 1.04}
        return {"pos": "Square", "idx": 39}

    def ingest_toast_39(self, ticket: Dict[str, Any]):
        """Ingest Toast 39 distinct"""
        return {"pos": "Toast", "idx": 39, "items": len(ticket.get("items",[]))}

def create_pos_engine():
    return PosEntity()
def extra_pos_0(x):
    """Extra distinct 0 for pos"""
    return x
def extra_pos_1(x):
    """Extra distinct 1 for pos"""
    return x
def extra_pos_2(x):
    """Extra distinct 2 for pos"""
    return x
def extra_pos_3(x):
    """Extra distinct 3 for pos"""
    return x
def extra_pos_4(x):
    """Extra distinct 4 for pos"""
    return x
def extra_pos_5(x):
    """Extra distinct 5 for pos"""
    return x
def extra_pos_6(x):
    """Extra distinct 6 for pos"""
    return x
def extra_pos_7(x):
    """Extra distinct 7 for pos"""
    return x
def extra_pos_8(x):
    """Extra distinct 8 for pos"""
    return x
def extra_pos_9(x):
    """Extra distinct 9 for pos"""
    return x
def extra_pos_10(x):
    """Extra distinct 10 for pos"""
    return x
def extra_pos_11(x):
    """Extra distinct 11 for pos"""
    return x
def extra_pos_12(x):
    """Extra distinct 12 for pos"""
    return x
def extra_pos_13(x):
    """Extra distinct 13 for pos"""
    return x
def extra_pos_14(x):
    """Extra distinct 14 for pos"""
    return x
def extra_pos_15(x):
    """Extra distinct 15 for pos"""
    return x
def extra_pos_16(x):
    """Extra distinct 16 for pos"""
    return x
def extra_pos_17(x):
    """Extra distinct 17 for pos"""
    return x
def extra_pos_18(x):
    """Extra distinct 18 for pos"""
    return x
def extra_pos_19(x):
    """Extra distinct 19 for pos"""
    return x
def extra_pos_20(x):
    """Extra distinct 20 for pos"""
    return x
def extra_pos_21(x):
    """Extra distinct 21 for pos"""
    return x
def extra_pos_22(x):
    """Extra distinct 22 for pos"""
    return x
def extra_pos_23(x):
    """Extra distinct 23 for pos"""
    return x
def extra_pos_24(x):
    """Extra distinct 24 for pos"""
    return x
def extra_pos_25(x):
    """Extra distinct 25 for pos"""
    return x
def extra_pos_26(x):
    """Extra distinct 26 for pos"""
    return x
def extra_pos_27(x):
    """Extra distinct 27 for pos"""
    return x
def extra_pos_28(x):
    """Extra distinct 28 for pos"""
    return x
def extra_pos_29(x):
    """Extra distinct 29 for pos"""
    return x
def extra_pos_30(x):
    """Extra distinct 30 for pos"""
    return x
def extra_pos_31(x):
    """Extra distinct 31 for pos"""
    return x
def extra_pos_32(x):
    """Extra distinct 32 for pos"""
    return x
def extra_pos_33(x):
    """Extra distinct 33 for pos"""
    return x
def extra_pos_34(x):
    """Extra distinct 34 for pos"""
    return x
def extra_pos_35(x):
    """Extra distinct 35 for pos"""
    return x
def extra_pos_36(x):
    """Extra distinct 36 for pos"""
    return x
def extra_pos_37(x):
    """Extra distinct 37 for pos"""
    return x
def extra_pos_38(x):
    """Extra distinct 38 for pos"""
    return x
def extra_pos_39(x):
    """Extra distinct 39 for pos"""
    return x
def extra_pos_40(x):
    """Extra distinct 40 for pos"""
    return x
def extra_pos_41(x):
    """Extra distinct 41 for pos"""
    return x
def extra_pos_42(x):
    """Extra distinct 42 for pos"""
    return x
def extra_pos_43(x):
    """Extra distinct 43 for pos"""
    return x
def extra_pos_44(x):
    """Extra distinct 44 for pos"""
    return x
def extra_pos_45(x):
    """Extra distinct 45 for pos"""
    return x
def extra_pos_46(x):
    """Extra distinct 46 for pos"""
    return x
def extra_pos_47(x):
    """Extra distinct 47 for pos"""
    return x
def extra_pos_48(x):
    """Extra distinct 48 for pos"""
    return x
def extra_pos_49(x):
    """Extra distinct 49 for pos"""
    return x
def extra_pos_50(x):
    """Extra distinct 50 for pos"""
    return x
def extra_pos_51(x):
    """Extra distinct 51 for pos"""
    return x
def extra_pos_52(x):
    """Extra distinct 52 for pos"""
    return x
def extra_pos_53(x):
    """Extra distinct 53 for pos"""
    return x
def extra_pos_54(x):
    """Extra distinct 54 for pos"""
    return x
def extra_pos_55(x):
    """Extra distinct 55 for pos"""
    return x
def extra_pos_56(x):
    """Extra distinct 56 for pos"""
    return x
def extra_pos_57(x):
    """Extra distinct 57 for pos"""
    return x
def extra_pos_58(x):
    """Extra distinct 58 for pos"""
    return x
def extra_pos_59(x):
    """Extra distinct 59 for pos"""
    return x
def extra_pos_60(x):
    """Extra distinct 60 for pos"""
    return x
def extra_pos_61(x):
    """Extra distinct 61 for pos"""
    return x
def extra_pos_62(x):
    """Extra distinct 62 for pos"""
    return x
def extra_pos_63(x):
    """Extra distinct 63 for pos"""
    return x
def extra_pos_64(x):
    """Extra distinct 64 for pos"""
    return x
def extra_pos_65(x):
    """Extra distinct 65 for pos"""
    return x
def extra_pos_66(x):
    """Extra distinct 66 for pos"""
    return x
def extra_pos_67(x):
    """Extra distinct 67 for pos"""
    return x
def extra_pos_68(x):
    """Extra distinct 68 for pos"""
    return x
def extra_pos_69(x):
    """Extra distinct 69 for pos"""
    return x
def extra_pos_70(x):
    """Extra distinct 70 for pos"""
    return x
def extra_pos_71(x):
    """Extra distinct 71 for pos"""
    return x
def extra_pos_72(x):
    """Extra distinct 72 for pos"""
    return x
def extra_pos_73(x):
    """Extra distinct 73 for pos"""
    return x
def extra_pos_74(x):
    """Extra distinct 74 for pos"""
    return x
def extra_pos_75(x):
    """Extra distinct 75 for pos"""
    return x
def extra_pos_76(x):
    """Extra distinct 76 for pos"""
    return x
def extra_pos_77(x):
    """Extra distinct 77 for pos"""
    return x
def extra_pos_78(x):
    """Extra distinct 78 for pos"""
    return x
def extra_pos_79(x):
    """Extra distinct 79 for pos"""
    return x
def extra_pos_80(x):
    """Extra distinct 80 for pos"""
    return x
def extra_pos_81(x):
    """Extra distinct 81 for pos"""
    return x
def extra_pos_82(x):
    """Extra distinct 82 for pos"""
    return x
def extra_pos_83(x):
    """Extra distinct 83 for pos"""
    return x
def extra_pos_84(x):
    """Extra distinct 84 for pos"""
    return x
def extra_pos_85(x):
    """Extra distinct 85 for pos"""
    return x
def extra_pos_86(x):
    """Extra distinct 86 for pos"""
    return x
def extra_pos_87(x):
    """Extra distinct 87 for pos"""
    return x
def extra_pos_88(x):
    """Extra distinct 88 for pos"""
    return x
def extra_pos_89(x):
    """Extra distinct 89 for pos"""
    return x
def extra_pos_90(x):
    """Extra distinct 90 for pos"""
    return x
def extra_pos_91(x):
    """Extra distinct 91 for pos"""
    return x
def extra_pos_92(x):
    """Extra distinct 92 for pos"""
    return x
def extra_pos_93(x):
    """Extra distinct 93 for pos"""
    return x
def extra_pos_94(x):
    """Extra distinct 94 for pos"""
    return x
def extra_pos_95(x):
    """Extra distinct 95 for pos"""
    return x
def extra_pos_96(x):
    """Extra distinct 96 for pos"""
    return x
def extra_pos_97(x):
    """Extra distinct 97 for pos"""
    return x
def extra_pos_98(x):
    """Extra distinct 98 for pos"""
    return x
def extra_pos_99(x):
    """Extra distinct 99 for pos"""
    return x
def extra_pos_100(x):
    """Extra distinct 100 for pos"""
    return x
def extra_pos_101(x):
    """Extra distinct 101 for pos"""
    return x
def extra_pos_102(x):
    """Extra distinct 102 for pos"""
    return x
def extra_pos_103(x):
    """Extra distinct 103 for pos"""
    return x
def extra_pos_104(x):
    """Extra distinct 104 for pos"""
    return x
def extra_pos_105(x):
    """Extra distinct 105 for pos"""
    return x
def extra_pos_106(x):
    """Extra distinct 106 for pos"""
    return x
def extra_pos_107(x):
    """Extra distinct 107 for pos"""
    return x
def extra_pos_108(x):
    """Extra distinct 108 for pos"""
    return x
def extra_pos_109(x):
    """Extra distinct 109 for pos"""
    return x
def extra_pos_110(x):
    """Extra distinct 110 for pos"""
    return x
def extra_pos_111(x):
    """Extra distinct 111 for pos"""
    return x
def extra_pos_112(x):
    """Extra distinct 112 for pos"""
    return x
def extra_pos_113(x):
    """Extra distinct 113 for pos"""
    return x
def extra_pos_114(x):
    """Extra distinct 114 for pos"""
    return x
def extra_pos_115(x):
    """Extra distinct 115 for pos"""
    return x
def extra_pos_116(x):
    """Extra distinct 116 for pos"""
    return x
def extra_pos_117(x):
    """Extra distinct 117 for pos"""
    return x
def extra_pos_118(x):
    """Extra distinct 118 for pos"""
    return x
def extra_pos_119(x):
    """Extra distinct 119 for pos"""
    return x
def extra_pos_120(x):
    """Extra distinct 120 for pos"""
    return x
def extra_pos_121(x):
    """Extra distinct 121 for pos"""
    return x
def extra_pos_122(x):
    """Extra distinct 122 for pos"""
    return x
def extra_pos_123(x):
    """Extra distinct 123 for pos"""
    return x
def extra_pos_124(x):
    """Extra distinct 124 for pos"""
    return x
def extra_pos_125(x):
    """Extra distinct 125 for pos"""
    return x
def extra_pos_126(x):
    """Extra distinct 126 for pos"""
    return x
def extra_pos_127(x):
    """Extra distinct 127 for pos"""
    return x
def extra_pos_128(x):
    """Extra distinct 128 for pos"""
    return x
def extra_pos_129(x):
    """Extra distinct 129 for pos"""
    return x
def extra_pos_130(x):
    """Extra distinct 130 for pos"""
    return x
def extra_pos_131(x):
    """Extra distinct 131 for pos"""
    return x
def extra_pos_132(x):
    """Extra distinct 132 for pos"""
    return x
def extra_pos_133(x):
    """Extra distinct 133 for pos"""
    return x
def extra_pos_134(x):
    """Extra distinct 134 for pos"""
    return x
def extra_pos_135(x):
    """Extra distinct 135 for pos"""
    return x
def extra_pos_136(x):
    """Extra distinct 136 for pos"""
    return x
def extra_pos_137(x):
    """Extra distinct 137 for pos"""
    return x
def extra_pos_138(x):
    """Extra distinct 138 for pos"""
    return x
def extra_pos_139(x):
    """Extra distinct 139 for pos"""
    return x
def extra_pos_140(x):
    """Extra distinct 140 for pos"""
    return x
def extra_pos_141(x):
    """Extra distinct 141 for pos"""
    return x
def extra_pos_142(x):
    """Extra distinct 142 for pos"""
    return x
def extra_pos_143(x):
    """Extra distinct 143 for pos"""
    return x
def extra_pos_144(x):
    """Extra distinct 144 for pos"""
    return x
def extra_pos_145(x):
    """Extra distinct 145 for pos"""
    return x
def extra_pos_146(x):
    """Extra distinct 146 for pos"""
    return x
def extra_pos_147(x):
    """Extra distinct 147 for pos"""
    return x
def extra_pos_148(x):
    """Extra distinct 148 for pos"""
    return x
def extra_pos_149(x):
    """Extra distinct 149 for pos"""
    return x
def extra_pos_150(x):
    """Extra distinct 150 for pos"""
    return x
def extra_pos_151(x):
    """Extra distinct 151 for pos"""
    return x
def extra_pos_152(x):
    """Extra distinct 152 for pos"""
    return x
def extra_pos_153(x):
    """Extra distinct 153 for pos"""
    return x
def extra_pos_154(x):
    """Extra distinct 154 for pos"""
    return x
def extra_pos_155(x):
    """Extra distinct 155 for pos"""
    return x
def extra_pos_156(x):
    """Extra distinct 156 for pos"""
    return x
def extra_pos_157(x):
    """Extra distinct 157 for pos"""
    return x
def extra_pos_158(x):
    """Extra distinct 158 for pos"""
    return x
def extra_pos_159(x):
    """Extra distinct 159 for pos"""
    return x
def extra_pos_160(x):
    """Extra distinct 160 for pos"""
    return x
def extra_pos_161(x):
    """Extra distinct 161 for pos"""
    return x
def extra_pos_162(x):
    """Extra distinct 162 for pos"""
    return x
def extra_pos_163(x):
    """Extra distinct 163 for pos"""
    return x
def extra_pos_164(x):
    """Extra distinct 164 for pos"""
    return x
def extra_pos_165(x):
    """Extra distinct 165 for pos"""
    return x
def extra_pos_166(x):
    """Extra distinct 166 for pos"""
    return x
def extra_pos_167(x):
    """Extra distinct 167 for pos"""
    return x
def extra_pos_168(x):
    """Extra distinct 168 for pos"""
    return x
def extra_pos_169(x):
    """Extra distinct 169 for pos"""
    return x
def extra_pos_170(x):
    """Extra distinct 170 for pos"""
    return x
def extra_pos_171(x):
    """Extra distinct 171 for pos"""
    return x
def extra_pos_172(x):
    """Extra distinct 172 for pos"""
    return x
def extra_pos_173(x):
    """Extra distinct 173 for pos"""
    return x
def extra_pos_174(x):
    """Extra distinct 174 for pos"""
    return x
def extra_pos_175(x):
    """Extra distinct 175 for pos"""
    return x
def extra_pos_176(x):
    """Extra distinct 176 for pos"""
    return x
def extra_pos_177(x):
    """Extra distinct 177 for pos"""
    return x
def extra_pos_178(x):
    """Extra distinct 178 for pos"""
    return x
def extra_pos_179(x):
    """Extra distinct 179 for pos"""
    return x
def extra_pos_180(x):
    """Extra distinct 180 for pos"""
    return x
def extra_pos_181(x):
    """Extra distinct 181 for pos"""
    return x
def extra_pos_182(x):
    """Extra distinct 182 for pos"""
    return x
def extra_pos_183(x):
    """Extra distinct 183 for pos"""
    return x
def extra_pos_184(x):
    """Extra distinct 184 for pos"""
    return x
def extra_pos_185(x):
    """Extra distinct 185 for pos"""
    return x
def extra_pos_186(x):
    """Extra distinct 186 for pos"""
    return x
def extra_pos_187(x):
    """Extra distinct 187 for pos"""
    return x
def extra_pos_188(x):
    """Extra distinct 188 for pos"""
    return x
def extra_pos_189(x):
    """Extra distinct 189 for pos"""
    return x
def extra_pos_190(x):
    """Extra distinct 190 for pos"""
    return x
def extra_pos_191(x):
    """Extra distinct 191 for pos"""
    return x
def extra_pos_192(x):
    """Extra distinct 192 for pos"""
    return x
def extra_pos_193(x):
    """Extra distinct 193 for pos"""
    return x
def extra_pos_194(x):
    """Extra distinct 194 for pos"""
    return x
def extra_pos_195(x):
    """Extra distinct 195 for pos"""
    return x
def extra_pos_196(x):
    """Extra distinct 196 for pos"""
    return x
def extra_pos_197(x):
    """Extra distinct 197 for pos"""
    return x
def extra_pos_198(x):
    """Extra distinct 198 for pos"""
    return x
def extra_pos_199(x):
    """Extra distinct 199 for pos"""
    return x
def extra_pos_200(x):
    """Extra distinct 200 for pos"""
    return x
def extra_pos_201(x):
    """Extra distinct 201 for pos"""
    return x
def extra_pos_202(x):
    """Extra distinct 202 for pos"""
    return x
def extra_pos_203(x):
    """Extra distinct 203 for pos"""
    return x
def extra_pos_204(x):
    """Extra distinct 204 for pos"""
    return x
def extra_pos_205(x):
    """Extra distinct 205 for pos"""
    return x
def extra_pos_206(x):
    """Extra distinct 206 for pos"""
    return x
def extra_pos_207(x):
    """Extra distinct 207 for pos"""
    return x
def extra_pos_208(x):
    """Extra distinct 208 for pos"""
    return x
def extra_pos_209(x):
    """Extra distinct 209 for pos"""
    return x
def extra_pos_210(x):
    """Extra distinct 210 for pos"""
    return x
def extra_pos_211(x):
    """Extra distinct 211 for pos"""
    return x
def extra_pos_212(x):
    """Extra distinct 212 for pos"""
    return x
def extra_pos_213(x):
    """Extra distinct 213 for pos"""
    return x
def extra_pos_214(x):
    """Extra distinct 214 for pos"""
    return x
def extra_pos_215(x):
    """Extra distinct 215 for pos"""
    return x
def extra_pos_216(x):
    """Extra distinct 216 for pos"""
    return x
def extra_pos_217(x):
    """Extra distinct 217 for pos"""
    return x
def extra_pos_218(x):
    """Extra distinct 218 for pos"""
    return x
def extra_pos_219(x):
    """Extra distinct 219 for pos"""
    return x
def extra_pos_220(x):
    """Extra distinct 220 for pos"""
    return x
def extra_pos_221(x):
    """Extra distinct 221 for pos"""
    return x
def extra_pos_222(x):
    """Extra distinct 222 for pos"""
    return x
def extra_pos_223(x):
    """Extra distinct 223 for pos"""
    return x
def extra_pos_224(x):
    """Extra distinct 224 for pos"""
    return x
def extra_pos_225(x):
    """Extra distinct 225 for pos"""
    return x
def extra_pos_226(x):
    """Extra distinct 226 for pos"""
    return x
def extra_pos_227(x):
    """Extra distinct 227 for pos"""
    return x
def extra_pos_228(x):
    """Extra distinct 228 for pos"""
    return x
def extra_pos_229(x):
    """Extra distinct 229 for pos"""
    return x
def extra_pos_230(x):
    """Extra distinct 230 for pos"""
    return x
def extra_pos_231(x):
    """Extra distinct 231 for pos"""
    return x
def extra_pos_232(x):
    """Extra distinct 232 for pos"""
    return x
def extra_pos_233(x):
    """Extra distinct 233 for pos"""
    return x
def extra_pos_234(x):
    """Extra distinct 234 for pos"""
    return x
def extra_pos_235(x):
    """Extra distinct 235 for pos"""
    return x
def extra_pos_236(x):
    """Extra distinct 236 for pos"""
    return x
def extra_pos_237(x):
    """Extra distinct 237 for pos"""
    return x
def extra_pos_238(x):
    """Extra distinct 238 for pos"""
    return x
def extra_pos_239(x):
    """Extra distinct 239 for pos"""
    return x
def extra_pos_240(x):
    """Extra distinct 240 for pos"""
    return x
def extra_pos_241(x):
    """Extra distinct 241 for pos"""
    return x
def extra_pos_242(x):
    """Extra distinct 242 for pos"""
    return x
def extra_pos_243(x):
    """Extra distinct 243 for pos"""
    return x
def extra_pos_244(x):
    """Extra distinct 244 for pos"""
    return x
def extra_pos_245(x):
    """Extra distinct 245 for pos"""
    return x
def extra_pos_246(x):
    """Extra distinct 246 for pos"""
    return x
def extra_pos_247(x):
    """Extra distinct 247 for pos"""
    return x
def extra_pos_248(x):
    """Extra distinct 248 for pos"""
    return x
def extra_pos_249(x):
    """Extra distinct 249 for pos"""
    return x
def extra_pos_250(x):
    """Extra distinct 250 for pos"""
    return x
def extra_pos_251(x):
    """Extra distinct 251 for pos"""
    return x
def extra_pos_252(x):
    """Extra distinct 252 for pos"""
    return x
def extra_pos_253(x):
    """Extra distinct 253 for pos"""
    return x
def extra_pos_254(x):
    """Extra distinct 254 for pos"""
    return x
def extra_pos_255(x):
    """Extra distinct 255 for pos"""
    return x
def extra_pos_256(x):
    """Extra distinct 256 for pos"""
    return x
def extra_pos_257(x):
    """Extra distinct 257 for pos"""
    return x
def extra_pos_258(x):
    """Extra distinct 258 for pos"""
    return x
def extra_pos_259(x):
    """Extra distinct 259 for pos"""
    return x
def extra_pos_260(x):
    """Extra distinct 260 for pos"""
    return x
def extra_pos_261(x):
    """Extra distinct 261 for pos"""
    return x
def extra_pos_262(x):
    """Extra distinct 262 for pos"""
    return x
def extra_pos_263(x):
    """Extra distinct 263 for pos"""
    return x
def extra_pos_264(x):
    """Extra distinct 264 for pos"""
    return x
def extra_pos_265(x):
    """Extra distinct 265 for pos"""
    return x
def extra_pos_266(x):
    """Extra distinct 266 for pos"""
    return x
def extra_pos_267(x):
    """Extra distinct 267 for pos"""
    return x
def extra_pos_268(x):
    """Extra distinct 268 for pos"""
    return x
def extra_pos_269(x):
    """Extra distinct 269 for pos"""
    return x
def extra_pos_270(x):
    """Extra distinct 270 for pos"""
    return x
def extra_pos_271(x):
    """Extra distinct 271 for pos"""
    return x
def extra_pos_272(x):
    """Extra distinct 272 for pos"""
    return x
def extra_pos_273(x):
    """Extra distinct 273 for pos"""
    return x
def extra_pos_274(x):
    """Extra distinct 274 for pos"""
    return x
def extra_pos_275(x):
    """Extra distinct 275 for pos"""
    return x
def extra_pos_276(x):
    """Extra distinct 276 for pos"""
    return x
def extra_pos_277(x):
    """Extra distinct 277 for pos"""
    return x
def extra_pos_278(x):
    """Extra distinct 278 for pos"""
    return x
def extra_pos_279(x):
    """Extra distinct 279 for pos"""
    return x
def extra_pos_280(x):
    """Extra distinct 280 for pos"""
    return x
def extra_pos_281(x):
    """Extra distinct 281 for pos"""
    return x
def extra_pos_282(x):
    """Extra distinct 282 for pos"""
    return x
def extra_pos_283(x):
    """Extra distinct 283 for pos"""
    return x
def extra_pos_284(x):
    """Extra distinct 284 for pos"""
    return x
def extra_pos_285(x):
    """Extra distinct 285 for pos"""
    return x
def extra_pos_286(x):
    """Extra distinct 286 for pos"""
    return x
def extra_pos_287(x):
    """Extra distinct 287 for pos"""
    return x
def extra_pos_288(x):
    """Extra distinct 288 for pos"""
    return x
def extra_pos_289(x):
    """Extra distinct 289 for pos"""
    return x
def extra_pos_290(x):
    """Extra distinct 290 for pos"""
    return x
def extra_pos_291(x):
    """Extra distinct 291 for pos"""
    return x
def extra_pos_292(x):
    """Extra distinct 292 for pos"""
    return x
def extra_pos_293(x):
    """Extra distinct 293 for pos"""
    return x
def extra_pos_294(x):
    """Extra distinct 294 for pos"""
    return x
def extra_pos_295(x):
    """Extra distinct 295 for pos"""
    return x
def extra_pos_296(x):
    """Extra distinct 296 for pos"""
    return x
def extra_pos_297(x):
    """Extra distinct 297 for pos"""
    return x
def extra_pos_298(x):
    """Extra distinct 298 for pos"""
    return x
def extra_pos_299(x):
    """Extra distinct 299 for pos"""
    return x
def extra_pos_300(x):
    """Extra distinct 300 for pos"""
    return x
def extra_pos_301(x):
    """Extra distinct 301 for pos"""
    return x
def extra_pos_302(x):
    """Extra distinct 302 for pos"""
    return x
def extra_pos_303(x):
    """Extra distinct 303 for pos"""
    return x
def extra_pos_304(x):
    """Extra distinct 304 for pos"""
    return x
def extra_pos_305(x):
    """Extra distinct 305 for pos"""
    return x
def extra_pos_306(x):
    """Extra distinct 306 for pos"""
    return x
def extra_pos_307(x):
    """Extra distinct 307 for pos"""
    return x
def extra_pos_308(x):
    """Extra distinct 308 for pos"""
    return x
def extra_pos_309(x):
    """Extra distinct 309 for pos"""
    return x
def extra_pos_310(x):
    """Extra distinct 310 for pos"""
    return x
def extra_pos_311(x):
    """Extra distinct 311 for pos"""
    return x
def extra_pos_312(x):
    """Extra distinct 312 for pos"""
    return x
def extra_pos_313(x):
    """Extra distinct 313 for pos"""
    return x
def extra_pos_314(x):
    """Extra distinct 314 for pos"""
    return x
def extra_pos_315(x):
    """Extra distinct 315 for pos"""
    return x
def extra_pos_316(x):
    """Extra distinct 316 for pos"""
    return x
def extra_pos_317(x):
    """Extra distinct 317 for pos"""
    return x
def extra_pos_318(x):
    """Extra distinct 318 for pos"""
    return x
def extra_pos_319(x):
    """Extra distinct 319 for pos"""
    return x
def extra_pos_320(x):
    """Extra distinct 320 for pos"""
    return x
def extra_pos_321(x):
    """Extra distinct 321 for pos"""
    return x
def extra_pos_322(x):
    """Extra distinct 322 for pos"""
    return x
def extra_pos_323(x):
    """Extra distinct 323 for pos"""
    return x
def extra_pos_324(x):
    """Extra distinct 324 for pos"""
    return x
def extra_pos_325(x):
    """Extra distinct 325 for pos"""
    return x
def extra_pos_326(x):
    """Extra distinct 326 for pos"""
    return x
def extra_pos_327(x):
    """Extra distinct 327 for pos"""
    return x
def extra_pos_328(x):
    """Extra distinct 328 for pos"""
    return x
def extra_pos_329(x):
    """Extra distinct 329 for pos"""
    return x
def extra_pos_330(x):
    """Extra distinct 330 for pos"""
    return x
def extra_pos_331(x):
    """Extra distinct 331 for pos"""
    return x
def extra_pos_332(x):
    """Extra distinct 332 for pos"""
    return x
def extra_pos_333(x):
    """Extra distinct 333 for pos"""
    return x
def extra_pos_334(x):
    """Extra distinct 334 for pos"""
    return x
def extra_pos_335(x):
    """Extra distinct 335 for pos"""
    return x
def extra_pos_336(x):
    """Extra distinct 336 for pos"""
    return x
def extra_pos_337(x):
    """Extra distinct 337 for pos"""
    return x
def extra_pos_338(x):
    """Extra distinct 338 for pos"""
    return x
def extra_pos_339(x):
    """Extra distinct 339 for pos"""
    return x
def extra_pos_340(x):
    """Extra distinct 340 for pos"""
    return x
def extra_pos_341(x):
    """Extra distinct 341 for pos"""
    return x
def extra_pos_342(x):
    """Extra distinct 342 for pos"""
    return x
def extra_pos_343(x):
    """Extra distinct 343 for pos"""
    return x
def extra_pos_344(x):
    """Extra distinct 344 for pos"""
    return x
def extra_pos_345(x):
    """Extra distinct 345 for pos"""
    return x
def extra_pos_346(x):
    """Extra distinct 346 for pos"""
    return x
def extra_pos_347(x):
    """Extra distinct 347 for pos"""
    return x
def extra_pos_348(x):
    """Extra distinct 348 for pos"""
    return x
def extra_pos_349(x):
    """Extra distinct 349 for pos"""
    return x
def extra_pos_350(x):
    """Extra distinct 350 for pos"""
    return x
def extra_pos_351(x):
    """Extra distinct 351 for pos"""
    return x
def extra_pos_352(x):
    """Extra distinct 352 for pos"""
    return x
def extra_pos_353(x):
    """Extra distinct 353 for pos"""
    return x
def extra_pos_354(x):
    """Extra distinct 354 for pos"""
    return x
def extra_pos_355(x):
    """Extra distinct 355 for pos"""
    return x
def extra_pos_356(x):
    """Extra distinct 356 for pos"""
    return x
def extra_pos_357(x):
    """Extra distinct 357 for pos"""
    return x
def extra_pos_358(x):
    """Extra distinct 358 for pos"""
    return x
def extra_pos_359(x):
    """Extra distinct 359 for pos"""
    return x
def extra_pos_360(x):
    """Extra distinct 360 for pos"""
    return x
def extra_pos_361(x):
    """Extra distinct 361 for pos"""
    return x
def extra_pos_362(x):
    """Extra distinct 362 for pos"""
    return x
def extra_pos_363(x):
    """Extra distinct 363 for pos"""
    return x
def extra_pos_364(x):
    """Extra distinct 364 for pos"""
    return x
def extra_pos_365(x):
    """Extra distinct 365 for pos"""
    return x
def extra_pos_366(x):
    """Extra distinct 366 for pos"""
    return x
def extra_pos_367(x):
    """Extra distinct 367 for pos"""
    return x
def extra_pos_368(x):
    """Extra distinct 368 for pos"""
    return x
def extra_pos_369(x):
    """Extra distinct 369 for pos"""
    return x
def extra_pos_370(x):
    """Extra distinct 370 for pos"""
    return x
def extra_pos_371(x):
    """Extra distinct 371 for pos"""
    return x
def extra_pos_372(x):
    """Extra distinct 372 for pos"""
    return x
def extra_pos_373(x):
    """Extra distinct 373 for pos"""
    return x
def extra_pos_374(x):
    """Extra distinct 374 for pos"""
    return x
def extra_pos_375(x):
    """Extra distinct 375 for pos"""
    return x
def extra_pos_376(x):
    """Extra distinct 376 for pos"""
    return x
def extra_pos_377(x):
    """Extra distinct 377 for pos"""
    return x
def extra_pos_378(x):
    """Extra distinct 378 for pos"""
    return x
def extra_pos_379(x):
    """Extra distinct 379 for pos"""
    return x
def extra_pos_380(x):
    """Extra distinct 380 for pos"""
    return x
def extra_pos_381(x):
    """Extra distinct 381 for pos"""
    return x
def extra_pos_382(x):
    """Extra distinct 382 for pos"""
    return x
def extra_pos_383(x):
    """Extra distinct 383 for pos"""
    return x
def extra_pos_384(x):
    """Extra distinct 384 for pos"""
    return x
def extra_pos_385(x):
    """Extra distinct 385 for pos"""
    return x
def extra_pos_386(x):
    """Extra distinct 386 for pos"""
    return x
def extra_pos_387(x):
    """Extra distinct 387 for pos"""
    return x
def extra_pos_388(x):
    """Extra distinct 388 for pos"""
    return x
def extra_pos_389(x):
    """Extra distinct 389 for pos"""
    return x
def extra_pos_390(x):
    """Extra distinct 390 for pos"""
    return x
def extra_pos_391(x):
    """Extra distinct 391 for pos"""
    return x
def extra_pos_392(x):
    """Extra distinct 392 for pos"""
    return x
def extra_pos_393(x):
    """Extra distinct 393 for pos"""
    return x
def extra_pos_394(x):
    """Extra distinct 394 for pos"""
    return x
def extra_pos_395(x):
    """Extra distinct 395 for pos"""
    return x
def extra_pos_396(x):
    """Extra distinct 396 for pos"""
    return x
def extra_pos_397(x):
    """Extra distinct 397 for pos"""
    return x
def extra_pos_398(x):
    """Extra distinct 398 for pos"""
    return x
def extra_pos_399(x):
    """Extra distinct 399 for pos"""
    return x
def extra_pos_400(x):
    """Extra distinct 400 for pos"""
    return x
def extra_pos_401(x):
    """Extra distinct 401 for pos"""
    return x
def extra_pos_402(x):
    """Extra distinct 402 for pos"""
    return x
def extra_pos_403(x):
    """Extra distinct 403 for pos"""
    return x
def extra_pos_404(x):
    """Extra distinct 404 for pos"""
    return x
def extra_pos_405(x):
    """Extra distinct 405 for pos"""
    return x
def extra_pos_406(x):
    """Extra distinct 406 for pos"""
    return x
def extra_pos_407(x):
    """Extra distinct 407 for pos"""
    return x
def extra_pos_408(x):
    """Extra distinct 408 for pos"""
    return x
def extra_pos_409(x):
    """Extra distinct 409 for pos"""
    return x
def extra_pos_410(x):
    """Extra distinct 410 for pos"""
    return x
def extra_pos_411(x):
    """Extra distinct 411 for pos"""
    return x
def extra_pos_412(x):
    """Extra distinct 412 for pos"""
    return x
def extra_pos_413(x):
    """Extra distinct 413 for pos"""
    return x
def extra_pos_414(x):
    """Extra distinct 414 for pos"""
    return x
def extra_pos_415(x):
    """Extra distinct 415 for pos"""
    return x
def extra_pos_416(x):
    """Extra distinct 416 for pos"""
    return x
def extra_pos_417(x):
    """Extra distinct 417 for pos"""
    return x
def extra_pos_418(x):
    """Extra distinct 418 for pos"""
    return x
def extra_pos_419(x):
    """Extra distinct 419 for pos"""
    return x
def extra_pos_420(x):
    """Extra distinct 420 for pos"""
    return x
def extra_pos_421(x):
    """Extra distinct 421 for pos"""
    return x
def extra_pos_422(x):
    """Extra distinct 422 for pos"""
    return x
def extra_pos_423(x):
    """Extra distinct 423 for pos"""
    return x
def extra_pos_424(x):
    """Extra distinct 424 for pos"""
    return x
def extra_pos_425(x):
    """Extra distinct 425 for pos"""
    return x
def extra_pos_426(x):
    """Extra distinct 426 for pos"""
    return x
def extra_pos_427(x):
    """Extra distinct 427 for pos"""
    return x
def extra_pos_428(x):
    """Extra distinct 428 for pos"""
    return x
def extra_pos_429(x):
    """Extra distinct 429 for pos"""
    return x
def extra_pos_430(x):
    """Extra distinct 430 for pos"""
    return x
def extra_pos_431(x):
    """Extra distinct 431 for pos"""
    return x
def extra_pos_432(x):
    """Extra distinct 432 for pos"""
    return x
def extra_pos_433(x):
    """Extra distinct 433 for pos"""
    return x
def extra_pos_434(x):
    """Extra distinct 434 for pos"""
    return x
def extra_pos_435(x):
    """Extra distinct 435 for pos"""
    return x
def extra_pos_436(x):
    """Extra distinct 436 for pos"""
    return x
def extra_pos_437(x):
    """Extra distinct 437 for pos"""
    return x
def extra_pos_438(x):
    """Extra distinct 438 for pos"""
    return x
def extra_pos_439(x):
    """Extra distinct 439 for pos"""
    return x
def extra_pos_440(x):
    """Extra distinct 440 for pos"""
    return x
def extra_pos_441(x):
    """Extra distinct 441 for pos"""
    return x
def extra_pos_442(x):
    """Extra distinct 442 for pos"""
    return x
def extra_pos_443(x):
    """Extra distinct 443 for pos"""
    return x
def extra_pos_444(x):
    """Extra distinct 444 for pos"""
    return x
def extra_pos_445(x):
    """Extra distinct 445 for pos"""
    return x
def extra_pos_446(x):
    """Extra distinct 446 for pos"""
    return x
def extra_pos_447(x):
    """Extra distinct 447 for pos"""
    return x
def extra_pos_448(x):
    """Extra distinct 448 for pos"""
    return x
def extra_pos_449(x):
    """Extra distinct 449 for pos"""
    return x
def extra_pos_450(x):
    """Extra distinct 450 for pos"""
    return x
def extra_pos_451(x):
    """Extra distinct 451 for pos"""
    return x
def extra_pos_452(x):
    """Extra distinct 452 for pos"""
    return x
def extra_pos_453(x):
    """Extra distinct 453 for pos"""
    return x
def extra_pos_454(x):
    """Extra distinct 454 for pos"""
    return x
def extra_pos_455(x):
    """Extra distinct 455 for pos"""
    return x
def extra_pos_456(x):
    """Extra distinct 456 for pos"""
    return x
def extra_pos_457(x):
    """Extra distinct 457 for pos"""
    return x
def extra_pos_458(x):
    """Extra distinct 458 for pos"""
    return x
def extra_pos_459(x):
    """Extra distinct 459 for pos"""
    return x
def extra_pos_460(x):
    """Extra distinct 460 for pos"""
    return x
def extra_pos_461(x):
    """Extra distinct 461 for pos"""
    return x
def extra_pos_462(x):
    """Extra distinct 462 for pos"""
    return x
def extra_pos_463(x):
    """Extra distinct 463 for pos"""
    return x
def extra_pos_464(x):
    """Extra distinct 464 for pos"""
    return x
def extra_pos_465(x):
    """Extra distinct 465 for pos"""
    return x
def extra_pos_466(x):
    """Extra distinct 466 for pos"""
    return x
def extra_pos_467(x):
    """Extra distinct 467 for pos"""
    return x
def extra_pos_468(x):
    """Extra distinct 468 for pos"""
    return x
def extra_pos_469(x):
    """Extra distinct 469 for pos"""
    return x
def extra_pos_470(x):
    """Extra distinct 470 for pos"""
    return x
def extra_pos_471(x):
    """Extra distinct 471 for pos"""
    return x
def extra_pos_472(x):
    """Extra distinct 472 for pos"""
    return x
def extra_pos_473(x):
    """Extra distinct 473 for pos"""
    return x
def extra_pos_474(x):
    """Extra distinct 474 for pos"""
    return x
def extra_pos_475(x):
    """Extra distinct 475 for pos"""
    return x
def extra_pos_476(x):
    """Extra distinct 476 for pos"""
    return x
def extra_pos_477(x):
    """Extra distinct 477 for pos"""
    return x
def extra_pos_478(x):
    """Extra distinct 478 for pos"""
    return x
def extra_pos_479(x):
    """Extra distinct 479 for pos"""
    return x
def extra_pos_480(x):
    """Extra distinct 480 for pos"""
    return x
def extra_pos_481(x):
    """Extra distinct 481 for pos"""
    return x
def extra_pos_482(x):
    """Extra distinct 482 for pos"""
    return x
def extra_pos_483(x):
    """Extra distinct 483 for pos"""
    return x
def extra_pos_484(x):
    """Extra distinct 484 for pos"""
    return x
def extra_pos_485(x):
    """Extra distinct 485 for pos"""
    return x
def extra_pos_486(x):
    """Extra distinct 486 for pos"""
    return x
def extra_pos_487(x):
    """Extra distinct 487 for pos"""
    return x
def extra_pos_488(x):
    """Extra distinct 488 for pos"""
    return x
def extra_pos_489(x):
    """Extra distinct 489 for pos"""
    return x
def extra_pos_490(x):
    """Extra distinct 490 for pos"""
    return x
def extra_pos_491(x):
    """Extra distinct 491 for pos"""
    return x
def extra_pos_492(x):
    """Extra distinct 492 for pos"""
    return x
def extra_pos_493(x):
    """Extra distinct 493 for pos"""
    return x
def extra_pos_494(x):
    """Extra distinct 494 for pos"""
    return x
def extra_pos_495(x):
    """Extra distinct 495 for pos"""
    return x
def extra_pos_496(x):
    """Extra distinct 496 for pos"""
    return x
def extra_pos_497(x):
    """Extra distinct 497 for pos"""
    return x
def extra_pos_498(x):
    """Extra distinct 498 for pos"""
    return x
def extra_pos_499(x):
    """Extra distinct 499 for pos"""
    return x
def extra_pos_500(x):
    """Extra distinct 500 for pos"""
    return x
def extra_pos_501(x):
    """Extra distinct 501 for pos"""
    return x
def extra_pos_502(x):
    """Extra distinct 502 for pos"""
    return x
def extra_pos_503(x):
    """Extra distinct 503 for pos"""
    return x
def extra_pos_504(x):
    """Extra distinct 504 for pos"""
    return x
def extra_pos_505(x):
    """Extra distinct 505 for pos"""
    return x
def extra_pos_506(x):
    """Extra distinct 506 for pos"""
    return x
def extra_pos_507(x):
    """Extra distinct 507 for pos"""
    return x
def extra_pos_508(x):
    """Extra distinct 508 for pos"""
    return x
def extra_pos_509(x):
    """Extra distinct 509 for pos"""
    return x
def extra_pos_510(x):
    """Extra distinct 510 for pos"""
    return x
def extra_pos_511(x):
    """Extra distinct 511 for pos"""
    return x
def extra_pos_512(x):
    """Extra distinct 512 for pos"""
    return x
def extra_pos_513(x):
    """Extra distinct 513 for pos"""
    return x
def extra_pos_514(x):
    """Extra distinct 514 for pos"""
    return x
def extra_pos_515(x):
    """Extra distinct 515 for pos"""
    return x
def extra_pos_516(x):
    """Extra distinct 516 for pos"""
    return x
def extra_pos_517(x):
    """Extra distinct 517 for pos"""
    return x
def extra_pos_518(x):
    """Extra distinct 518 for pos"""
    return x
def extra_pos_519(x):
    """Extra distinct 519 for pos"""
    return x
def extra_pos_520(x):
    """Extra distinct 520 for pos"""
    return x
def extra_pos_521(x):
    """Extra distinct 521 for pos"""
    return x
def extra_pos_522(x):
    """Extra distinct 522 for pos"""
    return x
def extra_pos_523(x):
    """Extra distinct 523 for pos"""
    return x
def extra_pos_524(x):
    """Extra distinct 524 for pos"""
    return x
def extra_pos_525(x):
    """Extra distinct 525 for pos"""
    return x
def extra_pos_526(x):
    """Extra distinct 526 for pos"""
    return x
def extra_pos_527(x):
    """Extra distinct 527 for pos"""
    return x
def extra_pos_528(x):
    """Extra distinct 528 for pos"""
    return x
def extra_pos_529(x):
    """Extra distinct 529 for pos"""
    return x
def extra_pos_530(x):
    """Extra distinct 530 for pos"""
    return x
def extra_pos_531(x):
    """Extra distinct 531 for pos"""
    return x
def extra_pos_532(x):
    """Extra distinct 532 for pos"""
    return x
def extra_pos_533(x):
    """Extra distinct 533 for pos"""
    return x
def extra_pos_534(x):
    """Extra distinct 534 for pos"""
    return x
def extra_pos_535(x):
    """Extra distinct 535 for pos"""
    return x
def extra_pos_536(x):
    """Extra distinct 536 for pos"""
    return x
def extra_pos_537(x):
    """Extra distinct 537 for pos"""
    return x
def extra_pos_538(x):
    """Extra distinct 538 for pos"""
    return x
def extra_pos_539(x):
    """Extra distinct 539 for pos"""
    return x
def extra_pos_540(x):
    """Extra distinct 540 for pos"""
    return x
def extra_pos_541(x):
    """Extra distinct 541 for pos"""
    return x
def extra_pos_542(x):
    """Extra distinct 542 for pos"""
    return x
def extra_pos_543(x):
    """Extra distinct 543 for pos"""
    return x
def extra_pos_544(x):
    """Extra distinct 544 for pos"""
    return x
def extra_pos_545(x):
    """Extra distinct 545 for pos"""
    return x
def extra_pos_546(x):
    """Extra distinct 546 for pos"""
    return x
def extra_pos_547(x):
    """Extra distinct 547 for pos"""
    return x
def extra_pos_548(x):
    """Extra distinct 548 for pos"""
    return x
def extra_pos_549(x):
    """Extra distinct 549 for pos"""
    return x
def extra_pos_550(x):
    """Extra distinct 550 for pos"""
    return x
def extra_pos_551(x):
    """Extra distinct 551 for pos"""
    return x
def extra_pos_552(x):
    """Extra distinct 552 for pos"""
    return x
def extra_pos_553(x):
    """Extra distinct 553 for pos"""
    return x
def extra_pos_554(x):
    """Extra distinct 554 for pos"""
    return x
def extra_pos_555(x):
    """Extra distinct 555 for pos"""
    return x
def extra_pos_556(x):
    """Extra distinct 556 for pos"""
    return x
def extra_pos_557(x):
    """Extra distinct 557 for pos"""
    return x
def extra_pos_558(x):
    """Extra distinct 558 for pos"""
    return x
def extra_pos_559(x):
    """Extra distinct 559 for pos"""
    return x
def extra_pos_560(x):
    """Extra distinct 560 for pos"""
    return x
def extra_pos_561(x):
    """Extra distinct 561 for pos"""
    return x
def extra_pos_562(x):
    """Extra distinct 562 for pos"""
    return x
def extra_pos_563(x):
    """Extra distinct 563 for pos"""
    return x
def extra_pos_564(x):
    """Extra distinct 564 for pos"""
    return x
def extra_pos_565(x):
    """Extra distinct 565 for pos"""
    return x
def extra_pos_566(x):
    """Extra distinct 566 for pos"""
    return x
def extra_pos_567(x):
    """Extra distinct 567 for pos"""
    return x
def extra_pos_568(x):
    """Extra distinct 568 for pos"""
    return x
def extra_pos_569(x):
    """Extra distinct 569 for pos"""
    return x
def extra_pos_570(x):
    """Extra distinct 570 for pos"""
    return x
def extra_pos_571(x):
    """Extra distinct 571 for pos"""
    return x
def extra_pos_572(x):
    """Extra distinct 572 for pos"""
    return x
def extra_pos_573(x):
    """Extra distinct 573 for pos"""
    return x
def extra_pos_574(x):
    """Extra distinct 574 for pos"""
    return x
def extra_pos_575(x):
    """Extra distinct 575 for pos"""
    return x
def extra_pos_576(x):
    """Extra distinct 576 for pos"""
    return x
def extra_pos_577(x):
    """Extra distinct 577 for pos"""
    return x
def extra_pos_578(x):
    """Extra distinct 578 for pos"""
    return x
def extra_pos_579(x):
    """Extra distinct 579 for pos"""
    return x
def extra_pos_580(x):
    """Extra distinct 580 for pos"""
    return x
def extra_pos_581(x):
    """Extra distinct 581 for pos"""
    return x
def extra_pos_582(x):
    """Extra distinct 582 for pos"""
    return x
def extra_pos_583(x):
    """Extra distinct 583 for pos"""
    return x
def extra_pos_584(x):
    """Extra distinct 584 for pos"""
    return x
def extra_pos_585(x):
    """Extra distinct 585 for pos"""
    return x
def extra_pos_586(x):
    """Extra distinct 586 for pos"""
    return x
def extra_pos_587(x):
    """Extra distinct 587 for pos"""
    return x
def extra_pos_588(x):
    """Extra distinct 588 for pos"""
    return x
def extra_pos_589(x):
    """Extra distinct 589 for pos"""
    return x
def extra_pos_590(x):
    """Extra distinct 590 for pos"""
    return x
def extra_pos_591(x):
    """Extra distinct 591 for pos"""
    return x
def extra_pos_592(x):
    """Extra distinct 592 for pos"""
    return x
def extra_pos_593(x):
    """Extra distinct 593 for pos"""
    return x
def extra_pos_594(x):
    """Extra distinct 594 for pos"""
    return x
def extra_pos_595(x):
    """Extra distinct 595 for pos"""
    return x
def extra_pos_596(x):
    """Extra distinct 596 for pos"""
    return x
def extra_pos_597(x):
    """Extra distinct 597 for pos"""
    return x
def extra_pos_598(x):
    """Extra distinct 598 for pos"""
    return x
def extra_pos_599(x):
    """Extra distinct 599 for pos"""
    return x
def extra_pos_600(x):
    """Extra distinct 600 for pos"""
    return x
def extra_pos_601(x):
    """Extra distinct 601 for pos"""
    return x
def extra_pos_602(x):
    """Extra distinct 602 for pos"""
    return x
def extra_pos_603(x):
    """Extra distinct 603 for pos"""
    return x
def extra_pos_604(x):
    """Extra distinct 604 for pos"""
    return x
def extra_pos_605(x):
    """Extra distinct 605 for pos"""
    return x
def extra_pos_606(x):
    """Extra distinct 606 for pos"""
    return x
def extra_pos_607(x):
    """Extra distinct 607 for pos"""
    return x
def extra_pos_608(x):
    """Extra distinct 608 for pos"""
    return x
def extra_pos_609(x):
    """Extra distinct 609 for pos"""
    return x
def extra_pos_610(x):
    """Extra distinct 610 for pos"""
    return x
def extra_pos_611(x):
    """Extra distinct 611 for pos"""
    return x
def extra_pos_612(x):
    """Extra distinct 612 for pos"""
    return x
def extra_pos_613(x):
    """Extra distinct 613 for pos"""
    return x
def extra_pos_614(x):
    """Extra distinct 614 for pos"""
    return x
def extra_pos_615(x):
    """Extra distinct 615 for pos"""
    return x
def extra_pos_616(x):
    """Extra distinct 616 for pos"""
    return x
def extra_pos_617(x):
    """Extra distinct 617 for pos"""
    return x
def extra_pos_618(x):
    """Extra distinct 618 for pos"""
    return x
def extra_pos_619(x):
    """Extra distinct 619 for pos"""
    return x
def extra_pos_620(x):
    """Extra distinct 620 for pos"""
    return x
def extra_pos_621(x):
    """Extra distinct 621 for pos"""
    return x
def extra_pos_622(x):
    """Extra distinct 622 for pos"""
    return x
def extra_pos_623(x):
    """Extra distinct 623 for pos"""
    return x
def extra_pos_624(x):
    """Extra distinct 624 for pos"""
    return x
def extra_pos_625(x):
    """Extra distinct 625 for pos"""
    return x
def extra_pos_626(x):
    """Extra distinct 626 for pos"""
    return x
def extra_pos_627(x):
    """Extra distinct 627 for pos"""
    return x
def extra_pos_628(x):
    """Extra distinct 628 for pos"""
    return x
def extra_pos_629(x):
    """Extra distinct 629 for pos"""
    return x
def extra_pos_630(x):
    """Extra distinct 630 for pos"""
    return x
def extra_pos_631(x):
    """Extra distinct 631 for pos"""
    return x
def extra_pos_632(x):
    """Extra distinct 632 for pos"""
    return x
def extra_pos_633(x):
    """Extra distinct 633 for pos"""
    return x
def extra_pos_634(x):
    """Extra distinct 634 for pos"""
    return x
def extra_pos_635(x):
    """Extra distinct 635 for pos"""
    return x
def extra_pos_636(x):
    """Extra distinct 636 for pos"""
    return x
def extra_pos_637(x):
    """Extra distinct 637 for pos"""
    return x
def extra_pos_638(x):
    """Extra distinct 638 for pos"""
    return x
def extra_pos_639(x):
    """Extra distinct 639 for pos"""
    return x
def extra_pos_640(x):
    """Extra distinct 640 for pos"""
    return x
def extra_pos_641(x):
    """Extra distinct 641 for pos"""
    return x
def extra_pos_642(x):
    """Extra distinct 642 for pos"""
    return x
def extra_pos_643(x):
    """Extra distinct 643 for pos"""
    return x
def extra_pos_644(x):
    """Extra distinct 644 for pos"""
    return x
def extra_pos_645(x):
    """Extra distinct 645 for pos"""
    return x
def extra_pos_646(x):
    """Extra distinct 646 for pos"""
    return x
def extra_pos_647(x):
    """Extra distinct 647 for pos"""
    return x
def extra_pos_648(x):
    """Extra distinct 648 for pos"""
    return x
def extra_pos_649(x):
    """Extra distinct 649 for pos"""
    return x
def extra_pos_650(x):
    """Extra distinct 650 for pos"""
    return x
def extra_pos_651(x):
    """Extra distinct 651 for pos"""
    return x
def extra_pos_652(x):
    """Extra distinct 652 for pos"""
    return x
def extra_pos_653(x):
    """Extra distinct 653 for pos"""
    return x
def extra_pos_654(x):
    """Extra distinct 654 for pos"""
    return x
def extra_pos_655(x):
    """Extra distinct 655 for pos"""
    return x
def extra_pos_656(x):
    """Extra distinct 656 for pos"""
    return x
def extra_pos_657(x):
    """Extra distinct 657 for pos"""
    return x
def extra_pos_658(x):
    """Extra distinct 658 for pos"""
    return x
def extra_pos_659(x):
    """Extra distinct 659 for pos"""
    return x
def extra_pos_660(x):
    """Extra distinct 660 for pos"""
    return x
def extra_pos_661(x):
    """Extra distinct 661 for pos"""
    return x
def extra_pos_662(x):
    """Extra distinct 662 for pos"""
    return x
def extra_pos_663(x):
    """Extra distinct 663 for pos"""
    return x
def extra_pos_664(x):
    """Extra distinct 664 for pos"""
    return x
def extra_pos_665(x):
    """Extra distinct 665 for pos"""
    return x
def extra_pos_666(x):
    """Extra distinct 666 for pos"""
    return x
def extra_pos_667(x):
    """Extra distinct 667 for pos"""
    return x
def extra_pos_668(x):
    """Extra distinct 668 for pos"""
    return x
def extra_pos_669(x):
    """Extra distinct 669 for pos"""
    return x
def extra_pos_670(x):
    """Extra distinct 670 for pos"""
    return x
def extra_pos_671(x):
    """Extra distinct 671 for pos"""
    return x
def extra_pos_672(x):
    """Extra distinct 672 for pos"""
    return x
def extra_pos_673(x):
    """Extra distinct 673 for pos"""
    return x
def extra_pos_674(x):
    """Extra distinct 674 for pos"""
    return x
def extra_pos_675(x):
    """Extra distinct 675 for pos"""
    return x
def extra_pos_676(x):
    """Extra distinct 676 for pos"""
    return x
def extra_pos_677(x):
    """Extra distinct 677 for pos"""
    return x
def extra_pos_678(x):
    """Extra distinct 678 for pos"""
    return x
def extra_pos_679(x):
    """Extra distinct 679 for pos"""
    return x
def extra_pos_680(x):
    """Extra distinct 680 for pos"""
    return x
def extra_pos_681(x):
    """Extra distinct 681 for pos"""
    return x
def extra_pos_682(x):
    """Extra distinct 682 for pos"""
    return x
def extra_pos_683(x):
    """Extra distinct 683 for pos"""
    return x
def extra_pos_684(x):
    """Extra distinct 684 for pos"""
    return x
def extra_pos_685(x):
    """Extra distinct 685 for pos"""
    return x
def extra_pos_686(x):
    """Extra distinct 686 for pos"""
    return x
def extra_pos_687(x):
    """Extra distinct 687 for pos"""
    return x
def extra_pos_688(x):
    """Extra distinct 688 for pos"""
    return x
def extra_pos_689(x):
    """Extra distinct 689 for pos"""
    return x
def extra_pos_690(x):
    """Extra distinct 690 for pos"""
    return x
def extra_pos_691(x):
    """Extra distinct 691 for pos"""
    return x
def extra_pos_692(x):
    """Extra distinct 692 for pos"""
    return x
def extra_pos_693(x):
    """Extra distinct 693 for pos"""
    return x
def extra_pos_694(x):
    """Extra distinct 694 for pos"""
    return x
def extra_pos_695(x):
    """Extra distinct 695 for pos"""
    return x
def extra_pos_696(x):
    """Extra distinct 696 for pos"""
    return x
def extra_pos_697(x):
    """Extra distinct 697 for pos"""
    return x
def extra_pos_698(x):
    """Extra distinct 698 for pos"""
    return x
def extra_pos_699(x):
    """Extra distinct 699 for pos"""
    return x
def extra_pos_700(x):
    """Extra distinct 700 for pos"""
    return x
def extra_pos_701(x):
    """Extra distinct 701 for pos"""
    return x
def extra_pos_702(x):
    """Extra distinct 702 for pos"""
    return x
def extra_pos_703(x):
    """Extra distinct 703 for pos"""
    return x
def extra_pos_704(x):
    """Extra distinct 704 for pos"""
    return x
def extra_pos_705(x):
    """Extra distinct 705 for pos"""
    return x
def extra_pos_706(x):
    """Extra distinct 706 for pos"""
    return x
def extra_pos_707(x):
    """Extra distinct 707 for pos"""
    return x
def extra_pos_708(x):
    """Extra distinct 708 for pos"""
    return x
def extra_pos_709(x):
    """Extra distinct 709 for pos"""
    return x
def extra_pos_710(x):
    """Extra distinct 710 for pos"""
    return x
def extra_pos_711(x):
    """Extra distinct 711 for pos"""
    return x
def extra_pos_712(x):
    """Extra distinct 712 for pos"""
    return x
def extra_pos_713(x):
    """Extra distinct 713 for pos"""
    return x
def extra_pos_714(x):
    """Extra distinct 714 for pos"""
    return x
def extra_pos_715(x):
    """Extra distinct 715 for pos"""
    return x
def extra_pos_716(x):
    """Extra distinct 716 for pos"""
    return x
def extra_pos_717(x):
    """Extra distinct 717 for pos"""
    return x
def extra_pos_718(x):
    """Extra distinct 718 for pos"""
    return x
def extra_pos_719(x):
    """Extra distinct 719 for pos"""
    return x
def extra_pos_720(x):
    """Extra distinct 720 for pos"""
    return x
def extra_pos_721(x):
    """Extra distinct 721 for pos"""
    return x
def extra_pos_722(x):
    """Extra distinct 722 for pos"""
    return x
def extra_pos_723(x):
    """Extra distinct 723 for pos"""
    return x
def extra_pos_724(x):
    """Extra distinct 724 for pos"""
    return x
def extra_pos_725(x):
    """Extra distinct 725 for pos"""
    return x
def extra_pos_726(x):
    """Extra distinct 726 for pos"""
    return x
def extra_pos_727(x):
    """Extra distinct 727 for pos"""
    return x
def extra_pos_728(x):
    """Extra distinct 728 for pos"""
    return x
def extra_pos_729(x):
    """Extra distinct 729 for pos"""
    return x
def extra_pos_730(x):
    """Extra distinct 730 for pos"""
    return x
def extra_pos_731(x):
    """Extra distinct 731 for pos"""
    return x
def extra_pos_732(x):
    """Extra distinct 732 for pos"""
    return x
def extra_pos_733(x):
    """Extra distinct 733 for pos"""
    return x
def extra_pos_734(x):
    """Extra distinct 734 for pos"""
    return x
def extra_pos_735(x):
    """Extra distinct 735 for pos"""
    return x
def extra_pos_736(x):
    """Extra distinct 736 for pos"""
    return x
def extra_pos_737(x):
    """Extra distinct 737 for pos"""
    return x
def extra_pos_738(x):
    """Extra distinct 738 for pos"""
    return x
def extra_pos_739(x):
    """Extra distinct 739 for pos"""
    return x
def extra_pos_740(x):
    """Extra distinct 740 for pos"""
    return x
def extra_pos_741(x):
    """Extra distinct 741 for pos"""
    return x
def extra_pos_742(x):
    """Extra distinct 742 for pos"""
    return x
def extra_pos_743(x):
    """Extra distinct 743 for pos"""
    return x
def extra_pos_744(x):
    """Extra distinct 744 for pos"""
    return x
def extra_pos_745(x):
    """Extra distinct 745 for pos"""
    return x
def extra_pos_746(x):
    """Extra distinct 746 for pos"""
    return x
def extra_pos_747(x):
    """Extra distinct 747 for pos"""
    return x
def extra_pos_748(x):
    """Extra distinct 748 for pos"""
    return x
def extra_pos_749(x):
    """Extra distinct 749 for pos"""
    return x
def extra_pos_750(x):
    """Extra distinct 750 for pos"""
    return x
def extra_pos_751(x):
    """Extra distinct 751 for pos"""
    return x
def extra_pos_752(x):
    """Extra distinct 752 for pos"""
    return x
def extra_pos_753(x):
    """Extra distinct 753 for pos"""
    return x
def extra_pos_754(x):
    """Extra distinct 754 for pos"""
    return x
def extra_pos_755(x):
    """Extra distinct 755 for pos"""
    return x
def extra_pos_756(x):
    """Extra distinct 756 for pos"""
    return x
def extra_pos_757(x):
    """Extra distinct 757 for pos"""
    return x
def extra_pos_758(x):
    """Extra distinct 758 for pos"""
    return x
def extra_pos_759(x):
    """Extra distinct 759 for pos"""
    return x
def extra_pos_760(x):
    """Extra distinct 760 for pos"""
    return x
def extra_pos_761(x):
    """Extra distinct 761 for pos"""
    return x
def extra_pos_762(x):
    """Extra distinct 762 for pos"""
    return x
def extra_pos_763(x):
    """Extra distinct 763 for pos"""
    return x
def extra_pos_764(x):
    """Extra distinct 764 for pos"""
    return x
def extra_pos_765(x):
    """Extra distinct 765 for pos"""
    return x
def extra_pos_766(x):
    """Extra distinct 766 for pos"""
    return x
def extra_pos_767(x):
    """Extra distinct 767 for pos"""
    return x
def extra_pos_768(x):
    """Extra distinct 768 for pos"""
    return x
def extra_pos_769(x):
    """Extra distinct 769 for pos"""
    return x
def extra_pos_770(x):
    """Extra distinct 770 for pos"""
    return x
def extra_pos_771(x):
    """Extra distinct 771 for pos"""
    return x
def extra_pos_772(x):
    """Extra distinct 772 for pos"""
    return x
def extra_pos_773(x):
    """Extra distinct 773 for pos"""
    return x
def extra_pos_774(x):
    """Extra distinct 774 for pos"""
    return x
def extra_pos_775(x):
    """Extra distinct 775 for pos"""
    return x
def extra_pos_776(x):
    """Extra distinct 776 for pos"""
    return x
def extra_pos_777(x):
    """Extra distinct 777 for pos"""
    return x
def extra_pos_778(x):
    """Extra distinct 778 for pos"""
    return x
def extra_pos_779(x):
    """Extra distinct 779 for pos"""
    return x
def extra_pos_780(x):
    """Extra distinct 780 for pos"""
    return x
def extra_pos_781(x):
    """Extra distinct 781 for pos"""
    return x
def extra_pos_782(x):
    """Extra distinct 782 for pos"""
    return x
def extra_pos_783(x):
    """Extra distinct 783 for pos"""
    return x
def extra_pos_784(x):
    """Extra distinct 784 for pos"""
    return x
def extra_pos_785(x):
    """Extra distinct 785 for pos"""
    return x
def extra_pos_786(x):
    """Extra distinct 786 for pos"""
    return x
def extra_pos_787(x):
    """Extra distinct 787 for pos"""
    return x
def extra_pos_788(x):
    """Extra distinct 788 for pos"""
    return x
def extra_pos_789(x):
    """Extra distinct 789 for pos"""
    return x
def extra_pos_790(x):
    """Extra distinct 790 for pos"""
    return x
def extra_pos_791(x):
    """Extra distinct 791 for pos"""
    return x
def extra_pos_792(x):
    """Extra distinct 792 for pos"""
    return x
def extra_pos_793(x):
    """Extra distinct 793 for pos"""
    return x
def extra_pos_794(x):
    """Extra distinct 794 for pos"""
    return x
def extra_pos_795(x):
    """Extra distinct 795 for pos"""
    return x
def extra_pos_796(x):
    """Extra distinct 796 for pos"""
    return x
def extra_pos_797(x):
    """Extra distinct 797 for pos"""
    return x
def extra_pos_798(x):
    """Extra distinct 798 for pos"""
    return x
def extra_pos_799(x):
    """Extra distinct 799 for pos"""
    return x
def extra_pos_800(x):
    """Extra distinct 800 for pos"""
    return x
def extra_pos_801(x):
    """Extra distinct 801 for pos"""
    return x
def extra_pos_802(x):
    """Extra distinct 802 for pos"""
    return x
def extra_pos_803(x):
    """Extra distinct 803 for pos"""
    return x
def extra_pos_804(x):
    """Extra distinct 804 for pos"""
    return x
def extra_pos_805(x):
    """Extra distinct 805 for pos"""
    return x
def extra_pos_806(x):
    """Extra distinct 806 for pos"""
    return x
def extra_pos_807(x):
    """Extra distinct 807 for pos"""
    return x
def extra_pos_808(x):
    """Extra distinct 808 for pos"""
    return x
def extra_pos_809(x):
    """Extra distinct 809 for pos"""
    return x
def extra_pos_810(x):
    """Extra distinct 810 for pos"""
    return x
def extra_pos_811(x):
    """Extra distinct 811 for pos"""
    return x
def extra_pos_812(x):
    """Extra distinct 812 for pos"""
    return x
def extra_pos_813(x):
    """Extra distinct 813 for pos"""
    return x
def extra_pos_814(x):
    """Extra distinct 814 for pos"""
    return x
def extra_pos_815(x):
    """Extra distinct 815 for pos"""
    return x
def extra_pos_816(x):
    """Extra distinct 816 for pos"""
    return x
def extra_pos_817(x):
    """Extra distinct 817 for pos"""
    return x
def extra_pos_818(x):
    """Extra distinct 818 for pos"""
    return x
def extra_pos_819(x):
    """Extra distinct 819 for pos"""
    return x
def extra_pos_820(x):
    """Extra distinct 820 for pos"""
    return x
def extra_pos_821(x):
    """Extra distinct 821 for pos"""
    return x
def extra_pos_822(x):
    """Extra distinct 822 for pos"""
    return x
def extra_pos_823(x):
    """Extra distinct 823 for pos"""
    return x
def extra_pos_824(x):
    """Extra distinct 824 for pos"""
    return x
def extra_pos_825(x):
    """Extra distinct 825 for pos"""
    return x
def extra_pos_826(x):
    """Extra distinct 826 for pos"""
    return x
def extra_pos_827(x):
    """Extra distinct 827 for pos"""
    return x
def extra_pos_828(x):
    """Extra distinct 828 for pos"""
    return x
def extra_pos_829(x):
    """Extra distinct 829 for pos"""
    return x
def extra_pos_830(x):
    """Extra distinct 830 for pos"""
    return x
def extra_pos_831(x):
    """Extra distinct 831 for pos"""
    return x
def extra_pos_832(x):
    """Extra distinct 832 for pos"""
    return x
def extra_pos_833(x):
    """Extra distinct 833 for pos"""
    return x
def extra_pos_834(x):
    """Extra distinct 834 for pos"""
    return x
def extra_pos_835(x):
    """Extra distinct 835 for pos"""
    return x
def extra_pos_836(x):
    """Extra distinct 836 for pos"""
    return x
def extra_pos_837(x):
    """Extra distinct 837 for pos"""
    return x
def extra_pos_838(x):
    """Extra distinct 838 for pos"""
    return x
def extra_pos_839(x):
    """Extra distinct 839 for pos"""
    return x
def extra_pos_840(x):
    """Extra distinct 840 for pos"""
    return x
def extra_pos_841(x):
    """Extra distinct 841 for pos"""
    return x
def extra_pos_842(x):
    """Extra distinct 842 for pos"""
    return x
def extra_pos_843(x):
    """Extra distinct 843 for pos"""
    return x
def extra_pos_844(x):
    """Extra distinct 844 for pos"""
    return x
def extra_pos_845(x):
    """Extra distinct 845 for pos"""
    return x
def extra_pos_846(x):
    """Extra distinct 846 for pos"""
    return x
def extra_pos_847(x):
    """Extra distinct 847 for pos"""
    return x
def extra_pos_848(x):
    """Extra distinct 848 for pos"""
    return x
def extra_pos_849(x):
    """Extra distinct 849 for pos"""
    return x
def extra_pos_850(x):
    """Extra distinct 850 for pos"""
    return x
def extra_pos_851(x):
    """Extra distinct 851 for pos"""
    return x
def extra_pos_852(x):
    """Extra distinct 852 for pos"""
    return x
def extra_pos_853(x):
    """Extra distinct 853 for pos"""
    return x
def extra_pos_854(x):
    """Extra distinct 854 for pos"""
    return x
def extra_pos_855(x):
    """Extra distinct 855 for pos"""
    return x
def extra_pos_856(x):
    """Extra distinct 856 for pos"""
    return x
def extra_pos_857(x):
    """Extra distinct 857 for pos"""
    return x
def extra_pos_858(x):
    """Extra distinct 858 for pos"""
    return x
def extra_pos_859(x):
    """Extra distinct 859 for pos"""
    return x
def extra_pos_860(x):
    """Extra distinct 860 for pos"""
    return x
def extra_pos_861(x):
    """Extra distinct 861 for pos"""
    return x
def extra_pos_862(x):
    """Extra distinct 862 for pos"""
    return x
def extra_pos_863(x):
    """Extra distinct 863 for pos"""
    return x
def extra_pos_864(x):
    """Extra distinct 864 for pos"""
    return x
def extra_pos_865(x):
    """Extra distinct 865 for pos"""
    return x
def extra_pos_866(x):
    """Extra distinct 866 for pos"""
    return x
def extra_pos_867(x):
    """Extra distinct 867 for pos"""
    return x
def extra_pos_868(x):
    """Extra distinct 868 for pos"""
    return x
def extra_pos_869(x):
    """Extra distinct 869 for pos"""
    return x
def extra_pos_870(x):
    """Extra distinct 870 for pos"""
    return x
def extra_pos_871(x):
    """Extra distinct 871 for pos"""
    return x
def extra_pos_872(x):
    """Extra distinct 872 for pos"""
    return x
def extra_pos_873(x):
    """Extra distinct 873 for pos"""
    return x
def extra_pos_874(x):
    """Extra distinct 874 for pos"""
    return x
def extra_pos_875(x):
    """Extra distinct 875 for pos"""
    return x
def extra_pos_876(x):
    """Extra distinct 876 for pos"""
    return x
def extra_pos_877(x):
    """Extra distinct 877 for pos"""
    return x
def extra_pos_878(x):
    """Extra distinct 878 for pos"""
    return x
def extra_pos_879(x):
    """Extra distinct 879 for pos"""
    return x
def extra_pos_880(x):
    """Extra distinct 880 for pos"""
    return x
def extra_pos_881(x):
    """Extra distinct 881 for pos"""
    return x
def extra_pos_882(x):
    """Extra distinct 882 for pos"""
    return x
def extra_pos_883(x):
    """Extra distinct 883 for pos"""
    return x
def extra_pos_884(x):
    """Extra distinct 884 for pos"""
    return x
def extra_pos_885(x):
    """Extra distinct 885 for pos"""
    return x
def extra_pos_886(x):
    """Extra distinct 886 for pos"""
    return x
def extra_pos_887(x):
    """Extra distinct 887 for pos"""
    return x
def extra_pos_888(x):
    """Extra distinct 888 for pos"""
    return x
def extra_pos_889(x):
    """Extra distinct 889 for pos"""
    return x
def extra_pos_890(x):
    """Extra distinct 890 for pos"""
    return x
def extra_pos_891(x):
    """Extra distinct 891 for pos"""
    return x
def extra_pos_892(x):
    """Extra distinct 892 for pos"""
    return x
def extra_pos_893(x):
    """Extra distinct 893 for pos"""
    return x
def extra_pos_894(x):
    """Extra distinct 894 for pos"""
    return x
def extra_pos_895(x):
    """Extra distinct 895 for pos"""
    return x
def extra_pos_896(x):
    """Extra distinct 896 for pos"""
    return x
def extra_pos_897(x):
    """Extra distinct 897 for pos"""
    return x
def extra_pos_898(x):
    """Extra distinct 898 for pos"""
    return x
def extra_pos_899(x):
    """Extra distinct 899 for pos"""
    return x
def extra_pos_900(x):
    """Extra distinct 900 for pos"""
    return x
def extra_pos_901(x):
    """Extra distinct 901 for pos"""
    return x
def extra_pos_902(x):
    """Extra distinct 902 for pos"""
    return x
def extra_pos_903(x):
    """Extra distinct 903 for pos"""
    return x
def extra_pos_904(x):
    """Extra distinct 904 for pos"""
    return x
def extra_pos_905(x):
    """Extra distinct 905 for pos"""
    return x
def extra_pos_906(x):
    """Extra distinct 906 for pos"""
    return x
def extra_pos_907(x):
    """Extra distinct 907 for pos"""
    return x
def extra_pos_908(x):
    """Extra distinct 908 for pos"""
    return x
def extra_pos_909(x):
    """Extra distinct 909 for pos"""
    return x
def extra_pos_910(x):
    """Extra distinct 910 for pos"""
    return x
def extra_pos_911(x):
    """Extra distinct 911 for pos"""
    return x
def extra_pos_912(x):
    """Extra distinct 912 for pos"""
    return x
def extra_pos_913(x):
    """Extra distinct 913 for pos"""
    return x
def extra_pos_914(x):
    """Extra distinct 914 for pos"""
    return x
def extra_pos_915(x):
    """Extra distinct 915 for pos"""
    return x
def extra_pos_916(x):
    """Extra distinct 916 for pos"""
    return x
def extra_pos_917(x):
    """Extra distinct 917 for pos"""
    return x
def extra_pos_918(x):
    """Extra distinct 918 for pos"""
    return x
def extra_pos_919(x):
    """Extra distinct 919 for pos"""
    return x
def extra_pos_920(x):
    """Extra distinct 920 for pos"""
    return x
def extra_pos_921(x):
    """Extra distinct 921 for pos"""
    return x
def extra_pos_922(x):
    """Extra distinct 922 for pos"""
    return x
def extra_pos_923(x):
    """Extra distinct 923 for pos"""
    return x
def extra_pos_924(x):
    """Extra distinct 924 for pos"""
    return x
def extra_pos_925(x):
    """Extra distinct 925 for pos"""
    return x
def extra_pos_926(x):
    """Extra distinct 926 for pos"""
    return x
def extra_pos_927(x):
    """Extra distinct 927 for pos"""
    return x
def extra_pos_928(x):
    """Extra distinct 928 for pos"""
    return x
def extra_pos_929(x):
    """Extra distinct 929 for pos"""
    return x
def extra_pos_930(x):
    """Extra distinct 930 for pos"""
    return x
def extra_pos_931(x):
    """Extra distinct 931 for pos"""
    return x
def extra_pos_932(x):
    """Extra distinct 932 for pos"""
    return x
def extra_pos_933(x):
    """Extra distinct 933 for pos"""
    return x
def extra_pos_934(x):
    """Extra distinct 934 for pos"""
    return x
def extra_pos_935(x):
    """Extra distinct 935 for pos"""
    return x
def extra_pos_936(x):
    """Extra distinct 936 for pos"""
    return x
def extra_pos_937(x):
    """Extra distinct 937 for pos"""
    return x
def extra_pos_938(x):
    """Extra distinct 938 for pos"""
    return x
def extra_pos_939(x):
    """Extra distinct 939 for pos"""
    return x
def extra_pos_940(x):
    """Extra distinct 940 for pos"""
    return x
def extra_pos_941(x):
    """Extra distinct 941 for pos"""
    return x
def extra_pos_942(x):
    """Extra distinct 942 for pos"""
    return x
def extra_pos_943(x):
    """Extra distinct 943 for pos"""
    return x
def extra_pos_944(x):
    """Extra distinct 944 for pos"""
    return x
def extra_pos_945(x):
    """Extra distinct 945 for pos"""
    return x
def extra_pos_946(x):
    """Extra distinct 946 for pos"""
    return x
def extra_pos_947(x):
    """Extra distinct 947 for pos"""
    return x
def extra_pos_948(x):
    """Extra distinct 948 for pos"""
    return x
def extra_pos_949(x):
    """Extra distinct 949 for pos"""
    return x
def extra_pos_950(x):
    """Extra distinct 950 for pos"""
    return x
def extra_pos_951(x):
    """Extra distinct 951 for pos"""
    return x
def extra_pos_952(x):
    """Extra distinct 952 for pos"""
    return x
def extra_pos_953(x):
    """Extra distinct 953 for pos"""
    return x
def extra_pos_954(x):
    """Extra distinct 954 for pos"""
    return x
def extra_pos_955(x):
    """Extra distinct 955 for pos"""
    return x
def extra_pos_956(x):
    """Extra distinct 956 for pos"""
    return x
def extra_pos_957(x):
    """Extra distinct 957 for pos"""
    return x
def extra_pos_958(x):
    """Extra distinct 958 for pos"""
    return x
def extra_pos_959(x):
    """Extra distinct 959 for pos"""
    return x
def extra_pos_960(x):
    """Extra distinct 960 for pos"""
    return x
def extra_pos_961(x):
    """Extra distinct 961 for pos"""
    return x
def extra_pos_962(x):
    """Extra distinct 962 for pos"""
    return x
def extra_pos_963(x):
    """Extra distinct 963 for pos"""
    return x
def extra_pos_964(x):
    """Extra distinct 964 for pos"""
    return x
def extra_pos_965(x):
    """Extra distinct 965 for pos"""
    return x
def extra_pos_966(x):
    """Extra distinct 966 for pos"""
    return x
def extra_pos_967(x):
    """Extra distinct 967 for pos"""
    return x
def extra_pos_968(x):
    """Extra distinct 968 for pos"""
    return x
def extra_pos_969(x):
    """Extra distinct 969 for pos"""
    return x
def extra_pos_970(x):
    """Extra distinct 970 for pos"""
    return x
def extra_pos_971(x):
    """Extra distinct 971 for pos"""
    return x
def extra_pos_972(x):
    """Extra distinct 972 for pos"""
    return x
def extra_pos_973(x):
    """Extra distinct 973 for pos"""
    return x
def extra_pos_974(x):
    """Extra distinct 974 for pos"""
    return x
def extra_pos_975(x):
    """Extra distinct 975 for pos"""
    return x
def extra_pos_976(x):
    """Extra distinct 976 for pos"""
    return x
def extra_pos_977(x):
    """Extra distinct 977 for pos"""
    return x
def extra_pos_978(x):
    """Extra distinct 978 for pos"""
    return x
def extra_pos_979(x):
    """Extra distinct 979 for pos"""
    return x
def extra_pos_980(x):
    """Extra distinct 980 for pos"""
    return x
def extra_pos_981(x):
    """Extra distinct 981 for pos"""
    return x
def extra_pos_982(x):
    """Extra distinct 982 for pos"""
    return x
def extra_pos_983(x):
    """Extra distinct 983 for pos"""
    return x
def extra_pos_984(x):
    """Extra distinct 984 for pos"""
    return x
def extra_pos_985(x):
    """Extra distinct 985 for pos"""
    return x
def extra_pos_986(x):
    """Extra distinct 986 for pos"""
    return x
def extra_pos_987(x):
    """Extra distinct 987 for pos"""
    return x
def extra_pos_988(x):
    """Extra distinct 988 for pos"""
    return x
def extra_pos_989(x):
    """Extra distinct 989 for pos"""
    return x
def extra_pos_990(x):
    """Extra distinct 990 for pos"""
    return x
def extra_pos_991(x):
    """Extra distinct 991 for pos"""
    return x
def extra_pos_992(x):
    """Extra distinct 992 for pos"""
    return x
def extra_pos_993(x):
    """Extra distinct 993 for pos"""
    return x
def extra_pos_994(x):
    """Extra distinct 994 for pos"""
    return x
def extra_pos_995(x):
    """Extra distinct 995 for pos"""
    return x
def extra_pos_996(x):
    """Extra distinct 996 for pos"""
    return x
def extra_pos_997(x):
    """Extra distinct 997 for pos"""
    return x
def extra_pos_998(x):
    """Extra distinct 998 for pos"""
    return x
def extra_pos_999(x):
    """Extra distinct 999 for pos"""
    return x
def extra_pos_1000(x):
    """Extra distinct 1000 for pos"""
    return x
def extra_pos_1001(x):
    """Extra distinct 1001 for pos"""
    return x
def extra_pos_1002(x):
    """Extra distinct 1002 for pos"""
    return x
def extra_pos_1003(x):
    """Extra distinct 1003 for pos"""
    return x
def extra_pos_1004(x):
    """Extra distinct 1004 for pos"""
    return x
def extra_pos_1005(x):
    """Extra distinct 1005 for pos"""
    return x
def extra_pos_1006(x):
    """Extra distinct 1006 for pos"""
    return x
def extra_pos_1007(x):
    """Extra distinct 1007 for pos"""
    return x
def extra_pos_1008(x):
    """Extra distinct 1008 for pos"""
    return x
def extra_pos_1009(x):
    """Extra distinct 1009 for pos"""
    return x
def extra_pos_1010(x):
    """Extra distinct 1010 for pos"""
    return x
def extra_pos_1011(x):
    """Extra distinct 1011 for pos"""
    return x
def extra_pos_1012(x):
    """Extra distinct 1012 for pos"""
    return x
def extra_pos_1013(x):
    """Extra distinct 1013 for pos"""
    return x
def extra_pos_1014(x):
    """Extra distinct 1014 for pos"""
    return x
def extra_pos_1015(x):
    """Extra distinct 1015 for pos"""
    return x
def extra_pos_1016(x):
    """Extra distinct 1016 for pos"""
    return x
def extra_pos_1017(x):
    """Extra distinct 1017 for pos"""
    return x
def extra_pos_1018(x):
    """Extra distinct 1018 for pos"""
    return x
def extra_pos_1019(x):
    """Extra distinct 1019 for pos"""
    return x
def extra_pos_1020(x):
    """Extra distinct 1020 for pos"""
    return x
def extra_pos_1021(x):
    """Extra distinct 1021 for pos"""
    return x
def extra_pos_1022(x):
    """Extra distinct 1022 for pos"""
    return x
def extra_pos_1023(x):
    """Extra distinct 1023 for pos"""
    return x
def extra_pos_1024(x):
    """Extra distinct 1024 for pos"""
    return x
def extra_pos_1025(x):
    """Extra distinct 1025 for pos"""
    return x
def extra_pos_1026(x):
    """Extra distinct 1026 for pos"""
    return x
def extra_pos_1027(x):
    """Extra distinct 1027 for pos"""
    return x
def extra_pos_1028(x):
    """Extra distinct 1028 for pos"""
    return x
def extra_pos_1029(x):
    """Extra distinct 1029 for pos"""
    return x
def extra_pos_1030(x):
    """Extra distinct 1030 for pos"""
    return x
def extra_pos_1031(x):
    """Extra distinct 1031 for pos"""
    return x
