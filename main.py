import json
from abc import ABC, abstractmethod

# NIM: SSI202504386 - NAMA: REZA AHMAD JAHID - UTS PBO
# INHERITANCE, POLYMORPHISM, OVERRIDE - 2 ULTIMATE

# === DATA LANGSUNG DI DALAM KODE (BIAR GAK ERROR FileNotFoundError) ===
EMP_DATA = {"employees": [
    {"emp_id": "EMP-001", "name": "Budi Pratama", "base_salary": 8500000.0, "is_permanent": True, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-002", "name": "Siti Rahma", "base_salary": 6000000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-003", "name": "Andi Wijaya", "base_salary": 12500000.0, "is_permanent": True, "bonus_code": None},
    {"emp_id": "EMP-004", "name": "Dewi Lestari", "base_salary": 7200000.0, "is_permanent": True, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-005", "name": "Eko Prasetyo", "base_salary": 5500000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-006", "name": "Fajar Nugraha", "base_salary": 9800000.0, "is_permanent": True, "bonus_code": "SENIOR10"},
    {"emp_id": "EMP-007", "name": "Gita Gutawa", "base_salary": 6800000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-008", "name": "Hendra Kurniawan", "base_salary": 11000000.0, "is_permanent": True, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-009", "name": "Indah Permata", "base_salary": 8000000.0, "is_permanent": True, "bonus_code": None},
    {"emp_id": "EMP-010", "name": "Joko Widodo", "base_salary": 5000000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-011", "name": "Kiki Amalia", "base_salary": 7700000.0, "is_permanent": True, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-012", "name": "Lukman Hakim", "base_salary": 13500000.0, "is_permanent": True, "bonus_code": "LEAD2026"},
    {"emp_id": "EMP-013", "name": "Maya Putri", "base_salary": 6200000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-014", "name": "Nurdin Hasan", "base_salary": 8900000.0, "is_permanent": True, "bonus_code": None},
    {"emp_id": "EMP-015", "name": "Oki Setiana", "base_salary": 9500000.0, "is_permanent": True, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-016", "name": "Panji Petualang", "base_salary": 5800000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-017", "name": "Qory Sandioriva", "base_salary": 10500000.0, "is_permanent": True, "bonus_code": "SENIOR10"},
    {"emp_id": "EMP-018", "name": "Rian D'Masiv", "base_salary": 7000000.0, "is_permanent": True, "bonus_code": None},
    {"emp_id": "EMP-019", "name": "Siska Kohl", "base_salary": 14000000.0, "is_permanent": True, "bonus_code": "LEAD2026"},
    {"emp_id": "EMP-020", "name": "Tora Sudiro", "base_salary": 6400000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-021", "name": "Uus Kartajaya", "base_salary": 8300000.0, "is_permanent": True, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-022", "name": "Vina Panduwinata", "base_salary": 9100000.0, "is_permanent": True, "bonus_code": None},
    {"emp_id": "EMP-023", "name": "Wendra Pratama", "base_salary": 5300000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-024", "name": "Xavier Marks", "base_salary": 11800000.0, "is_permanent": True, "bonus_code": "SENIOR10"},
    {"emp_id": "EMP-025", "name": "Yuni Shara", "base_salary": 7600000.0, "is_permanent": True, "bonus_code": None},
    {"emp_id": "EMP-026", "name": "Zainal Abidin", "base_salary": 6500000.0, "is_permanent": False, "bonus_code": None},
    {"emp_id": "EMP-027", "name": "Ahmad Dhani", "base_salary": 15000000.0, "is_permanent": True, "bonus_code": "LEAD2026"},
    {"emp_id": "EMP-028", "name": "Bella Saphira", "base_salary": 8200000.0, "is_permanent": True, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-029", "name": "Cinta Laura", "base_salary": 10000000.0, "is_permanent": True, "bonus_code": None},
    {"emp_id": "EMP-030", "name": "Deddy Corbuzier", "base_salary": 6100000.0, "is_permanent": False, "bonus_code": None}
]}

SENSOR_DATA = {"readings": [
    {"sensor_id": "SNS-A01", "location": "Boiler Room", "temperature": 88.5, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A02", "location": "Assembly Line", "temperature": 42.0, "status": "NORMAL", "operator_id": 102},
    {"sensor_id": "SNS-A03", "location": "Server Room", "temperature": 95.2, "status": "DANGER", "operator_id": None},
    {"sensor_id": "SNS-A04", "location": "Chemical Lab", "temperature": 73.1, "status": "WARNING", "operator_id": 104},
    {"sensor_id": "SNS-A05", "location": "Boiler Room", "temperature": 91.0, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A06", "location": "Warehouse", "temperature": 31.5, "status": "NORMAL", "operator_id": None},
    {"sensor_id": "SNS-A07", "location": "Turbine House", "temperature": 87.3, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A08", "location": "Assembly Line", "temperature": 45.8, "status": "NORMAL", "operator_id": 102},
    {"sensor_id": "SNS-A09", "location": "Server Room", "temperature": 89.9, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A10", "location": "Data Center", "temperature": 24.0, "status": "NORMAL", "operator_id": None},
    {"sensor_id": "SNS-A11", "location": "Boiler Room", "temperature": 96.4, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A12", "location": "Chemical Lab", "temperature": 68.0, "status": "WARNING", "operator_id": 104},
    {"sensor_id": "SNS-A13", "location": "Turbine House", "temperature": 92.1, "status": "DANGER", "operator_id": None},
    {"sensor_id": "SNS-A14", "location": "Warehouse", "temperature": 29.8, "status": "NORMAL", "operator_id": 114},
    {"sensor_id": "SNS-A15", "location": "Server Room", "temperature": 86.0, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A16", "location": "Assembly Line", "temperature": 41.2, "status": "NORMAL", "operator_id": 102},
    {"sensor_id": "SNS-A17", "location": "Boiler Room", "temperature": 99.5, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A18", "location": "Data Center", "temperature": 22.5, "status": "NORMAL", "operator_id": None},
    {"sensor_id": "SNS-A19", "location": "Turbine House", "temperature": 88.0, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A20", "location": "Chemical Lab", "temperature": 75.4, "status": "WARNING", "operator_id": None},
    {"sensor_id": "SNS-A21", "location": "Boiler Room", "temperature": 90.2, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A22", "location": "Assembly Line", "temperature": 39.9, "status": "NORMAL", "operator_id": 122},
    {"sensor_id": "SNS-A23", "location": "Server Room", "temperature": 93.7, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A24", "location": "Warehouse", "temperature": 30.0, "status": "NORMAL", "operator_id": None},
    {"sensor_id": "SNS-A25", "location": "Turbine House", "temperature": 87.8, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A26", "location": "Data Center", "temperature": 25.1, "status": "NORMAL", "operator_id": 126},
    {"sensor_id": "SNS-A27", "location": "Boiler Room", "temperature": 97.0, "status": "DANGER", "operator_id": None},
    {"sensor_id": "SNS-A28", "location": "Chemical Lab", "temperature": 71.3, "status": "WARNING", "operator_id": 104},
    {"sensor_id": "SNS-A29", "location": "Server Room", "temperature": 85.5, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A30", "location": "Assembly Line", "temperature": 43.5, "status": "NORMAL", "operator_id": None}
]}

# === CLASS INHERITANCE & OVERRIDE ===
class Employee(ABC):
    def __init__(self, emp_id, name, base_salary, bonus_code):
        self.emp_id=emp_id; self.name=name; self.base_salary=base_salary; self.bonus_code=bonus_code
    def get_bonus(self): return self.base_salary * {"PERF2026":0.20,"SENIOR10":0.10,"LEAD2026":0.30}.get(self.bonus_code,0)
    @abstractmethod
    def calculate_total_salary(self): pass

class PermanentEmployee(Employee): # ULTIMATE 1 - OVERRIDE
    def calculate_total_salary(self): return self.base_salary*1.15 + self.get_bonus()
    def display(self): return f"[PERMANENT] {self.emp_id} | {self.name} | TOTAL: {self.calculate_total_salary():,.0f}"

class ContractEmployee(Employee): # ULTIMATE 1 - OVERRIDE
    def calculate_total_salary(self): return self.base_salary + self.get_bonus()
    def display(self): return f"[CONTRACT] {self.emp_id} | {self.name} | TOTAL: {self.calculate_total_salary():,.0f}"

class Sensor(ABC):
    def __init__(self, sid, loc, temp, op): self.sensor_id=sid; self.location=loc; self.temperature=temp; self.operator_id=op
    def get_emp_id(self):
        if self.operator_id is None: return None
        return f"EMP-{self.operator_id-100:03d}"
    @abstractmethod
    def handle_alert(self): pass

class DangerSensor(Sensor): # ULTIMATE 2 - OVERRIDE
    def handle_alert(self): return f"DANGER - EVACUATE {self.location}! {self.temperature}C"
class WarningSensor(Sensor):
    def handle_alert(self): return f"WARNING - {self.location}: {self.temperature}C"
class NormalSensor(Sensor):
    def handle_alert(self): return f"NORMAL - {self.location} Safe {self.temperature}C"

def make_sensor(d):
    t=d["temperature"]
    if t>=85: return DangerSensor(d["sensor_id"],d["location"],t,d["operator_id"])
    elif t>=65: return WarningSensor(d["sensor_id"],d["location"],t,d["operator_id"])
    else: return NormalSensor(d["sensor_id"],d["location"],t,d["operator_id"])

# === MAIN - POLYMORPHISM ===
print("="*70)
print("UTS PBO - REZA AHMAD JAHID - SSI202504386")
print("Inheritance, Polymorphism, Override")
print("="*70)
emp_dict={}
for e in EMP_DATA["employees"]:
    obj=PermanentEmployee(e["emp_id"],e["name"],e["base_salary"],e["bonus_code"]) if e["is_permanent"] else ContractEmployee(e["emp_id"],e["name"],e["base_salary"],e["bonus_code"])
    emp_dict[e["emp_id"]]=obj
    print(obj.display()) # Polymorphism

print("\n--- SENSOR (ULTIMATE KEDUA - OVERRIDE handle_alert) ---")
for s in SENSOR_DATA["readings"]:
    sens=make_sensor(s) # Polymorphism factory
    eid=sens.get_emp_id()
    oname=emp_dict[eid].name if eid in emp_dict else "No Operator"
    print(f"{sens.sensor_id} | {sens.handle_alert()} | Operator: {oname}")
print("\n=== SELESAI - SIAP UPLOAD GITHUB ===")