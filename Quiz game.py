from tabulate import tabulate as tb
from pymongo import MongoClient

def quiz(questions):
    n=len(questions)
    score=0
    name=input("Enter your name : ")
    age=input("Enter your age : ")
    data=[]
    for ques in questions:
        print(ques["prompt"])
        for op in ques["options"]:
            print(op)
        user_answer=input("Enter your answer (A or B or C or D) :  ")
        if user_answer==ques['answer']:
            print("Correct answer!!...Keep it up!!")
            score+=1
        else:
            print(f"Wrong answer!!...Correct answer is {ques['answer']}")
        print('--------------------------------------------------------------')
    row = []
    headers = ["Name", "Age", "Score"]
    row.append((name))
    row.append((age))
    row.append((score))
    data.append(row)
    mongo_data={
            "Name":name,
            "Age":age,
            "Marks":score
    }
    print(f'Your Score is {score} out of {n}....Your Score Card is Below 👇👇')
    print(tb(data, headers=headers, tablefmt="grid"))

    client = MongoClient("mongodb://localhost:27017/")
    db = client["Quiz_game"]
    collection = db["user_data"]
    result = collection.insert_one(mongo_data)

    print("Your Marks are recorded...")

questions = [
    {
        'prompt': 'Who is the current President of the United States?',
        'options': ['A. Joe Biden', 'B. Donald Trump', 'C. Barack Obama', 'D. Kamala Harris'],
        'answer': 'B'
    },
    {
        'prompt': 'What is the name of the first privately developed spacecraft to reach orbit?',
        'options': ['A. SpaceX Falcon 9', 'B. Blue Origin New Shepard', 'C. Virgin Galactic SpaceShipTwo', 'D. SpaceX Starship'],
        'answer': 'A'
    },
    {
        'prompt': 'In 2024, which country will host the Summer Olympics?',
        'options': ['A. France', 'B. Japan', 'C. USA', 'D. Australia'],
        'answer': 'A'
    },
    {
        'prompt': 'Who became the Prime Minister of the United Kingdom after Liz Truss resigned in 2022?',
        'options': ['A. Rishi Sunak', 'B. Boris Johnson', 'C. Keir Starmer', 'D. Theresa May'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country recently became the first to legalize the sale of lab-grown meat?',
        'options': ['A. USA', 'B. Singapore', 'C. Canada', 'D. Germany'],
        'answer': 'B'
    },
    {
        'prompt': 'What is the name of NASA\'s Mars rover that landed in 2021?',
        'options': ['A. Curiosity', 'B. Perseverance', 'C. Opportunity', 'D. Spirit'],
        'answer': 'B'
    },
    {
        'prompt': 'Which company is the largest producer of electric vehicles in the world as of 2023?',
        'options': ['A. Tesla', 'B. BYD', 'C. Rivian', 'D. General Motors'],
        'answer': 'A'
    },
    {
        'prompt': 'Who won the 2023 FIFA Women\'s World Cup?',
        'options': ['A. USA', 'B. Germany', 'C. Spain', 'D. Japan'],
        'answer': 'C'
    },
    {
        'prompt':'Which is the capital of India?',
        'options':['A. Agra','B. Mumbai','C. Delhi','D. Chennai'],
        'answer':'C'
    },
    {
        'prompt': 'Which country is the largest producer of solar power in the world?',
        'options': ['A. China', 'B. India', 'C. USA', 'D. Germany'],
        'answer': 'A'
    },
    {
        'prompt': 'In which country did the catastrophic earthquake strike in February 2023, resulting in thousands of deaths?',
        'options': ['A. Turkey', 'B. Haiti', 'C. Indonesia', 'D. Mexico'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country became the first to launch a solar-powered aircraft that flew nonstop around the world?',
        'options': ['A. Germany', 'B. USA', 'C. China', 'D. UAE'],
        'answer': 'D'
    },
    {
        'prompt': 'Who won the 2023 Nobel Peace Prize?',
        'options': ['A. Volodymyr Zelenskyy', 'B. Ales Bialiatski', 'C. Narges Mohammadi', 'D. Greta Thunberg'],
        'answer': 'C'
    },
    {
        'prompt': 'What year did the European Union achieve 100% renewable electricity for the first time?',
        'options': ['A. 2020', 'B. 2022', 'C. 2023', 'D. 2021'],
        'answer': 'B'
    },
    {
        'prompt': 'Which country became the first to approve a malaria vaccine?',
        'options': ['A. Kenya', 'B. India', 'C. Malawi', 'D. Nigeria'],
        'answer': 'C'
    },
    {
        'prompt': 'Which company launched the first commercial quantum computer for the public in 2023?',
        'options': ['A. IBM', 'B. Google', 'C. Honeywell', 'D. Microsoft'],
        'answer': 'C'
    },
    {
        'prompt': 'What is the name of the new currency launched by India for digital transactions?',
        'options': ['A. Digital Rupee', 'B. Digital Dollar', 'C. Cryptocurrency', 'D. RuPay'],
        'answer': 'A'
    },
    {
        'prompt': 'Who was the winner of the 2023 Academy Award for Best Picture?',
        'options': ['A. Everything Everywhere All at Once', 'B. Top Gun: Maverick', 'C. Avatar: The Way of Water', 'D. The Fabelmans'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country hosted the COP28 climate summit in 2023?',
        'options': ['A. Qatar', 'B. UAE', 'C. Saudi Arabia', 'D. Egypt'],
        'answer': 'B'
    },
    {
        'prompt': 'Which major tech company announced plans to develop a “metaverse” in 2023?',
        'options': ['A. Facebook (Meta)', 'B. Microsoft', 'C. Apple', 'D. Google'],
        'answer': 'A'
    },
    {
        'prompt': 'Which Asian country became the first to offer nationwide 5G internet services?',
        'options': ['A. South Korea', 'B. Japan', 'C. India', 'D. China'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country launched the first-ever "carbon-neutral" cargo ship in 2023?',
        'options': ['A. Norway', 'B. Sweden', 'C. USA', 'D. Finland'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country became the first to implement a national four-day workweek trial in 2023?',
        'options': ['A. UK', 'B. Iceland', 'C. Japan', 'D. Australia'],
        'answer': 'B'
    },
    {
        'prompt': 'Which country became the first to open a tourist visa for space travelers in 2023?',
        'options': ['A. Russia', 'B. China', 'C. USA', 'D. United Arab Emirates'],
        'answer': 'D'
    },
    {
        'prompt': 'Which Asian country has become the largest market for electric vehicles as of 2023?',
        'options': ['A. India', 'B. Japan', 'C. China', 'D. South Korea'],
        'answer': 'C'
    },
    {
        'prompt': 'Who became the first woman to lead the European Central Bank in 2023?',
        'options': ['A. Ursula von der Leyen', 'B. Christine Lagarde', 'C. Angela Merkel', 'D. Janet Yellen'],
        'answer': 'B'
    },
    {
        'prompt': 'What country’s government launched a “digital nomad visa” in 2023 to attract remote workers?',
        'options': ['A. Portugal', 'B. Estonia', 'C. Mexico', 'D. Costa Rica'],
        'answer': 'A'
    },
    {
        'prompt': 'Which tech giant reached a valuation of $3 trillion for the first time in 2023?',
        'options': ['A. Microsoft', 'B. Tesla', 'C. Apple', 'D. Amazon'],
        'answer': 'C'
    },
    {
        'prompt': 'Which country became the first to announce a national AI strategy in 2023?',
        'options': ['A. USA', 'B. China', 'C. Canada', 'D. United Kingdom'],
        'answer': 'B'
    },
    {
        'prompt': 'Which international organization announced plans to phase out single-use plastic by 2025?',
        'options': ['A. United Nations', 'B. World Bank', 'C. WHO', 'D. World Economic Forum'],
        'answer': 'A'
    },
    {
        'prompt': 'Who became the first woman to serve as the US Secretary of the Treasury in 2023?',
        'options': ['A. Janet Yellen', 'B. Kamala Harris', 'C. Hillary Clinton', 'D. Elizabeth Warren'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country became the first to establish a national artificial intelligence laboratory in 2023?',
        'options': ['A. China', 'B. USA', 'C. South Korea', 'D. Japan'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country became the first to build a carbon-neutral city?',
        'options': ['A. Netherlands', 'B. Denmark', 'C. UAE', 'D. Sweden'],
        'answer': 'B'
    },
    {
        'prompt': 'Which country hosted the 2022 FIFA World Cup?',
        'options': ['A. Qatar', 'B. Russia', 'C. France', 'D. Brazil'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country’s government implemented a “green new deal” in 2023?',
        'options': ['A. South Korea', 'B. Canada', 'C. UK', 'D. Japan'],
        'answer': 'A'
    }
]   # Questions(35)

quiz(questions)


