import pandas as pd

category2Question = {
    "Depression" : [
        "I couldn’t seem to experience any positive feeling at all ",
        "I found it difficult to work up the initiative to do things",
        "I felt that I had nothing to look forward to ",
        "I felt down-hearted and blue",
        "I was unable to become enthusiastic about anything",
        "I felt I wasn’t worth much as a person",
        "I felt that life was meaningless",
        
    ],
    "Anxiety" : [
        "I was aware of dryness of my mouth",
        "I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion)",
        "I experienced trembling (e.g. in the hands)",
        "I was worried about situations in which I might panic and make a fool of myself",
        "I felt I was close to panic",
        "I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat)",
        "I felt scared without any good reason",
        ],
    "Stress" : [
        "I found it difficult to relax ",
        "I tended to over-react to situations",
        "I felt that I was using a lot of nervous energy",
        "I found myself getting agitated ",
        "I was intolerant of anything that kept me from getting on with what I was doing ",
        "I felt that I was rather touchy",  
    ],
}

response2Score = {
    "Almost always" : 6,
    "Often" : 4,
    "Sometimes" : 2,
    "Never" : 0,
}

category2Bounds = {
    "Stress" : [10, 18, 26, 34],
    "Depression" : [6, 9, 14, 19],
    "Anxiety" : [9, 12, 20, 27],
}
category2Resource = {
    "Stress" : "https://www.mayoclinic.org/healthy-lifestyle/stress-management/in-depth/stress-relievers/art-20047257",
    "Depression" : "https://www.webmd.com/depression/features/natural-treatments",
    "Anxiety" : "https://www.healthline.com/health/natural-ways-to-reduce-anxiety",
}
def add_resource(readable_score, category):
    result = f"Your {category} score was {readable_score}."
    if readable_score != "Normal":
        result += f" For tips on reducing this score, please see {category2Resource[category]}"
    return result

def score2readable(score, category):
    bounds = category2Bounds[category]
    readable_score = None
    if score < bounds[0]:
        readable_score = "Normal"
    elif score < bounds[1]:
        readable_score = "Mild"
    elif score < bounds[2]:
        readable_score = "Moderate"
    elif score < bounds[3]:
        readable_score = "Severe"
    else:
        readable_score = "Extremely Severe"
    return add_resource(readable_score, category)

def calculateScore(category, df, user):
    users_responses = df[df['Email Address'] == user]
    score = 0
    for question in category2Question[category]:
        resp = list(users_responses[question])
        score += response2Score[resp[0]]
    return score2readable(score, category)


def main():
    df = pd.read_csv('~/Downloads/responses.csv')
    scores = []
    for email in df['Email Address']:
        for category in category2Question.keys():
            scores.append(calculateScore(category, df, email))
        print(email + "\n", "\n".join(scores))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
