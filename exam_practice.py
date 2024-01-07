#!/usr/bin/env python3

import sys, os, random

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def win_mac_func():
	backslash = "\\"
	forwardslash = "/"
	user_home = os.path.expanduser("~")
	desktop_path = os.path.join(user_home, "Desktop")
	if backslash in desktop_path:
		slash = backslash
	elif forwardslash in desktop_path:
		slash = forwardslash
	return desktop_path, slash

def num_func(my_st):
	while True:
		number = input(my_st)
		if number.isdecimal():
			number = int(number)
			break
	return number

def head(my_st):
	while True:
		head_var = input(my_st).upper()
		if head_var:
			break
	return head_var

def duration(my_list=[]):
	while True:
		time1_var = input(my_list[0])
		format1_var = input(my_list[1])
		if (is_float(time1_var) or time1_var.isdecimal()) and format1_var:
			if format1_var.lower() == "h":
				if time1_var == "1":
					format1_var = "Hr"
				else:
					format1_var = "Hrs"
				break
			elif format1_var.lower() == "m":
				if time1_var == "1":
					format1_var = "Min"
				else:
					format1_var = "Mins"
				break
	return time1_var, format1_var

def questions_and_answers(default=0):
	if default != 0:
		while True:
			number_of_questions = input("Enter number of questions >>> ")
			if number_of_questions.isdecimal() and int(number_of_questions) > 3:
				number_of_questions = int(number_of_questions)
				break
			print("You must enter atleast 4 questions.")
		print("""Minimum question you have to enter is 4.
			and the questions and answers must be in the format:

			Question # Answer
			""")
		
		questions_then_answers = {}
		for i in range(number_of_questions):
			while True:
				user_input = input(f'Enter question {i + 1}, followed by its answer (separate them using "#"): ')
				if "#" in user_input:
					key, value = user_input.split('#')
					questions_then_answers[key.strip()] = value.strip()
					break
				print('The question and answer must be separated by "#"')		

	else:
		print('Using the default questions and answers.')
		questions_then_answers = {
		"Abia State": "Umuahia",
		"Adamawa": "Yola",
		"Akwa Ibom": "Uyo",
		"Anambra": "Awka",
		"Bauchi": "Bauchi",
		"Bayelsa": "Yenagoa",
		"Benue": "Makurdi",
		"Borno": "Maiduguri",
		"Cross River": "Calabar",
		"Delta": "Asaba",
		"Ebonyi": "Abakaliki",
		"Edo": "Benin City",
		"Ekiti": "Ado Ekiti",
		"Enugu": "Enugu",
		"Gombe": "Gombe",
		"Imo": "Owerri",
		"Jigawa": "Dutse",
		"Kaduna": "Kaduna",
		"Kano": "Kano",
		"Katsina": "Katsina",
		"Kebbi": "Birnin Kebbi",
		"Kogi": "Lokoja",
		"Kwara": "Ilorin",
		"Lagos": "Ikeja",
		"Nasarawa": "Lafia",
		"Niger": "Minna",
		"Ogun": "Abeokuta",
		"Ondo": "Akure",
		"Osun": "Oshogbo",
		"Oyo": "Ibadan",
		"Plateau": "Jos",
		"Rivers": "Port Harcourt",
		"Sokoto": "Sokoto",
		"Taraba": "Jalingo",
		"Yobe": "Damaturu",
		"Zamfara": "Gusau",
		"Federal Capital Territory": "Abuja",
		}

		number_of_questions = None
	return questions_then_answers, number_of_questions


def main():
	# the dictionary that is used to develop the questions and answers
	while True:
		default = input("Do you want to type in your questions and answers? [y/N] >>> ")
		if default.lower() == "y":
			val = 1
			break
		elif default.lower() == "n":
			val = 0
			break

	questions_and_answers_var, num_of_questions = questions_and_answers(val)

	path_to, delimiter = win_mac_func()
	
	exam_location = f"{path_to}{delimiter}QuizFolder"
	question_location = f"{exam_location}{delimiter}Questions"
	answer_location = f"{exam_location}{delimiter}Answers"

	file_typ = "How many file-types do you want to make? >>> "
	number_of_types = num_func(file_typ)

	head_s:%s/old/new/gtr = "Enter a heading for the exam: "
	heading = head(head_str)

	time1_str = "Provide duration: "
	format1_str = "What format is this duration, Hrs or Mins [h/M] >>> "
	duration_tup = (time1_str, format1_str)
	time1, format1 = duration(duration_tup)

	if val == 0:
		QA = "How many questions >>> "
		number_of_QA = num_func(QA)
	else:
		number_of_QA = num_of_questions
	
	try:
		os.makedirs(question_location)
		os.makedirs(answer_location)

		examQuestionFilePath = question_location
		examAnswerFilePath = answer_location

	except FileExistsError:
		examQuestionFilePath = question_location
		examAnswerFilePath = answer_location
	
    ## loop for number of file to be created
	for examFileNumber in range(number_of_types):
		type1 = examFileNumber + 65
		file_type = f"Type{chr(type1)}.txt"
		# questions heading
		text = f" {heading}---QUESTIONS ".center(70, "*")
		bio = f"\n\n\nChoose from the options[A-D], the correct answer\n\nFirstname:\t\t\tLastname:\t\tType:{chr(type1)}\n\nDate:\t\t\t\tTime:{time1}{format1}\n\n"

        # answers heading
		textAnswers = f" {heading}---ANSWERS ".center(70, "*")
		body = f"\n\n\tType:{chr(type1)}\n"

        # answers txtfile creation and modification 
		answerExamFileName = open(f"{examAnswerFilePath}{delimiter}{file_type}", "w")
		answerExamFileName.write(textAnswers + body)

        # questions txtfile creation and modification
		questionExamFileName = open(f"{examQuestionFilePath}{delimiter}{file_type}", "w")
		questionExamFileName.write(text + bio)
		
        # extract the keys into list(states of the country )
		states = list(questions_and_answers_var.keys())
		
        # shuffle the list
		random.shuffle(states)

        # select number_of_QA items from the shuffled list
		selectedStates = random.sample(states, number_of_QA)
		
        ### creation of number_of_QA(questions and answers)
		for examNum in range(number_of_QA):
			# creation of correct answer for every question 
			correctAnswer = questions_and_answers_var[selectedStates[examNum]]
			# creation of wrong answer list for every question 
			wrongAnswers = list(questions_and_answers_var.values())
			# removing correct answer from the list of wrong answers for every question 
			del wrongAnswers[wrongAnswers.index(correctAnswer)]
			# selecting 3 options from the wrong answer list
			wrongAnswers = random.sample(wrongAnswers, 3)
			# combining 1 correct and 3 wrong answers to make 4 options 
			answerOptions = [correctAnswer] + wrongAnswers
			# shuffle the 4 options 
			random.shuffle(answerOptions)
			# write these to question file
			questionExamFileName.write(f"\n{examNum + 1}. What is the Capital of {selectedStates[examNum]}?\n")

            # write to answers file
			answerExamFileName.write(f"\n{examNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}")

            ### loop for multiple choice options 
			for options in range(4):
				# write to question file and change the numbers to alphabets
				### USE THIS! OR... 
				questionExamFileName.write(f"\t{'ABCD'[options]}. {answerOptions[options]}\n")
				### ...OR USE THIS!
				# examFileName.write(f"\t{'ABCD'[options]}. {answerOptions[options]}")
			
			
	### close the file(after writing)
	questionExamFileName.close()
	# print(readQuestionFile)

	### close the file(after writing)
	answerExamFileName.close()
	# print(readAnswerFile)

	print()
	print(f"{examFileNumber + 1} files, each having {examNum + 1} Questions and Answers has been created on to your {path_to.split(os.path.sep)[-1]} inside {os.path.basename(exam_location)} directory")
	print()
	print("Gracias!")

if __name__ == "__main__":
	main()
