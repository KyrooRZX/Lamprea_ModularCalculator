raw_score = float(input("Enter your score: "))
def add_bonus(score):
    bonus = 5
    total_score = bonus + (score)
    return total_score
    
result = int(add_bonus(raw_score))
print ("Total_score is ",result)