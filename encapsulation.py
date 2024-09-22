import re 

class GradingSystem:
    def __init__(self):
        self.grade_regex = r'^[0-9]+(\.[0-9]+)?$'
        
    def grade(self, score):
        if re.match(self.grade_regex, score):
            score = float(score)
            if score >= 90:
                return 'A'
            elif score >= 80:
                return 'B'
            elif score >=70:
                return 'C'
            elif score >=60:
                return 'D'
            else:
                return 'E'
        else:
            return 'Invalid input'
        
demo = GradingSystem()
scores = ['95', '85,5', '75','65.7', 'abc']

for score in scores:
    print(f"Score: {score}, Grade: {demo.grade(score)}")