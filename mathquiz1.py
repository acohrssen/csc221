from random import randint

correct = 0

print()

questionCount = randint(1,8)

print()

for question in range(questionCount):
	n1 = randint(1, 10)
	n2 = randint(1, 10)

	print(f'  -- Question {question + 1} of {questionCount} --')
	print()

	print(f'What is {n1} * {n2}?')
	guess = int(input('> '))

	answer = n1 * n2

	print()
	print(f'The answer is {answer}.')

	if answer == guess:
		print('You got it right!!')
		correct = correct + 1
	else:
		print('Sorry, wrong answer :(')

	print()
	print()

print('  -- You finished the quiz! --')
print()
print(f'You got {correct} out of {questionCount}.')
print()