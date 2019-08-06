#!/usr/local/bin/python3

# ATBS-8_quiz.py - random quiz generator

import random, os

# question and answer pool
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
   'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz file sets
for quizNum in range(35):
   # generate quiz files
   quizFile = open("ATBS/ATBS-8_quizzes/capitalsquiz{}.txt".format(quizNum +1), "w")
   # generate answer files
   answerKeyFile = open("ATBS/ATBS-8_quizzes/capitalsquiz_answers{}.txt".format(quizNum +1), "w")
   
   # add a header for the quiz
   quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
   quizFile.write((" " * 20)+ "State Capitals Quiz (Form {})\n\n".format(quizNum + 1))

   # shuffle the order of the states
   states = list(capitals.keys())
   random.shuffle(states)
   
   # loop through all 50 states, making a question for each
   for questionNum in range(50):
      # get right answer
      correctAnswer = capitals[states[questionNum]]
      # copy list to get the wrong answers
      wrongAnswers = list(capitals.values())
      # delete the correct answer
      del wrongAnswers[wrongAnswers.index(correctAnswer)]
      # pick 3 random wrong answes
      wrongAnswers = random.sample(wrongAnswers, 3)
      # add correct answer to list of 4 total options
      answerOptions = wrongAnswers + [correctAnswer]
      # shuffle answer options
      random.shuffle(answerOptions)

      # write question and answer options to the quiz file
      quizFile.write("{}. What is the capital of {}?\n".format(questionNum + 1, states[questionNum]))
      for i in range(4):
         quizFile.write(" {}. {}\n".format("ABCD"[i], answerOptions[i]))

      # Write the answer key to a file.
      answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
      
quizFile.close()
answerKeyFile.close()