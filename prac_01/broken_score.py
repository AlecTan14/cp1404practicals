def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

if __name__ == "__main__":
    main()