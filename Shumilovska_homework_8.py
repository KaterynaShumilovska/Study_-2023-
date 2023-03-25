#Завдання 1
numbers = [3,5,45,97,32,22,10,19,39,43]
result = [number for number in numbers if number % 2 ==0]
print(result)

#Завдання 2
story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much."
num_spaces =len([i for i in story if i == ' '])
print(num_spaces)

#Завдання 3
new_story = story.replace(',', '').replace('.', '').split()
num_words = len([i for i in new_story if len(i) > 4])
print(num_words)