import random

def generate_words(letter_count):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word = ''.join(random.sample(alphabet, letter_count))
    return word

def generate_questions(no_questions,letter_count):
    objectionable_words={'KILL','MURDER','HATE','DIRTY'}
    generated_words=set()
    questions=[]

    while len(questions) <  no_questions:
        word=generate_words(letter_count)

        #Check whether the word has already been generated or if it is an objectionabale word
        if word in generated_words or word in objectionable_words:
            continue 

        #Formulation of questions
        question = f"The position of how many letters will remain unchanged if each of the letters in the word {word} is arranged in alphabetical order?"
        
        #To count the number of unchanged words
        sorted_word=''.join(sorted(word))
        count=0
        for i in range(0,len(word)):
            if(sorted_word[i]==word[i]):
                count+=1 
        
        #Producing Options
        correct_option = count
        incorrect_options=[]
        options=[]
        while len(incorrect_options) < 3:
            number=random.randint(0,len(word))

            if number in incorrect_options or number==correct_option:
                continue
            
            else:
                incorrect_options.append(number)
        
        options = [correct_option] + incorrect_options
        random.shuffle(options)

        #adding the current word to set of generated words
        generated_words.add(word)

    return questions
        


no_questions=int(input("Enter the number of questions needed: "))
letter_count = int(input("Enter the letter-count of the word: "))

questions = generate_questions(no_questions,letter_count)

for qno,(question,options,correct_option) in enumerate(questions):

    print("\nQuestion-",qno+1,": ",question)
    for j, option in enumerate(options):
        print(j+1,". ",option)
    
    print("Correct Answer: ",correct_option)

