import random

story_by_parts={
'when':['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived'],
'who':['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America'],
'went':['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ'],
'what':['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance']
}

story = ''

for que in story_by_parts:
	if que == 'went':
		story = story+f"went to {random.choice(story_by_parts[que])} "
	else:
		story = story+random.choice(story_by_parts[que])+' '

print(story)
