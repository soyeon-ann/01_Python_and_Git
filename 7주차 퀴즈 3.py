#Quiz 3

# 저는 이번 자유 프로그래밍으로 건설 현장 안전 관리 시스템에 대하여 작성 하였습니다.
# 건설 현장에서는 작업자들의 안전을 보장하기 위한 장비 상태 점검, 작업자 교육, 위험 요소 파악이 필수적입니다.
# 따라서, 체계적인 관리를 통해 안전사고가 발생하는 것을 목표로 이 자유 프로래밍 주제로 선정하게 되었습니다.

# 작업자 클래스 정의
class Worker:
    def __init__(self, name, role, trained=False, hours=0):
        self.name = name # 작업자의 이름
        self.role = role # 작업자의 역할
        self.trained = trained # 교육 여부
        self.hours = hours # 근무 시간

    def attend_training(self):
        self.trained = True

    def work(self, hours):
        self.hours += hours

    def get_info(self):
        return f"{self.name} ({self.role}): 교육 여부: {self.trained}, 근무 시간: {self.hours}시간"

# 장비 클래스 정의
class Equipment:
    def __init__(self, name, status="정상"):
        self.name = name # 장비의 이름
        self.status = status # 장비의 상태

    def update_status(self, status):
        self.status = status

    def needs_maintenance(self): # 정상이 아니면 True 반환
        return self.status != "정상"

# 위험 요소 클래스 정의
class Hazard:
    def __init__(self, name, severity="낮음"):
        self.name = name # 위험 요소의 이름
        self.severity = severity # 위험 요소의 심각도

    def update_severity(self, level):
        self.severity = level

    def is_high_risk(self):
        return self.severity == "높음"

# 예시 객체 생성 및 사용
worker1 = Worker("안소연", "전기공", True, 8)
equipment1 = Equipment("크레인")
hazard1 = Hazard("고압선 노출", "높음")

print(worker1.get_info()) # 작업자 정보 출력
print(equipment1.needs_maintenance()) # 장비의 유지보수 필요 여부 출력 (정상이라 False)
print(hazard1.is_high_risk()) # 위험 요소가 고위험인지 확인 (높음 이므로 True)