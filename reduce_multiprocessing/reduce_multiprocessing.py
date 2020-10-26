from functools import reduce
import json
import multiprocessing


def derive_guest_count(acc, attendee):
	"""
	Function calculates the number of attendees who brought guests.
	"""
	acc['total_guests'] += 1
	
	if attendee['brought_guests']:
		acc['guest_who_brought_guests'] += 1
		acc['total_guests'] += 1
		
	return acc
	

def derive_vegan_info(acc, attendee):
	"""
	Function checks vegan information among the list.
	"""
	if attendee['vegan']:
		acc['vegan'] += 1
	else:
		acc['non_vegan'] += 1

	if attendee.get('brought_guests'):
		for guest_brought in attendee['guests']:
			# Checks guests recursively
			acc = derive_vegan_info(acc, guest_brought)

	return acc


def extract(attendee):
	"""
	Function extracts guests information.
	"""
	return {
		'guest_name': attendee['name'],
		'vegan_info': 'vegan' if attendee['vegan'] == True else 'non_vegan',
		'guests_brought': attendee['guests'] if attendee['brought_guests'] else 0
	}


if __name__ == '__main__':
	list_of_attendees = [
			{"name": "Zeke", "vegan": True, "brought_guests": True,
			"guests": [{"name": "Amanda",
						"vegan": False},
			{"name": "Wayne", "vegan": True}]},
			{"name": "Xavier", "vegan": True, "brought_guests": False},
			{"name": "Yohanna", "vegan": False, "brought_guests": True,
			"guests": [{"name": "Lily",
						"vegan": True},
			{"name": "Stefano", "vegan": True}]},
			{"name": "Kael", "vegan": False, "brought_guests": False},
			{"name": "Landon", "vegan": True, "brought_guests": False},
		]
		
	result_guests = reduce(
		derive_guest_count,
		list_of_attendees,
		{
			'guest_who_brought_guests': 0,
			'total_guests': 0
		}
	)
	
	result_vegan = reduce(
		derive_vegan_info,
		list_of_attendees,
		{
			'vegan': 0,
			'non_vegan': 0
		}
	)
	
	print(json.dumps(result_guests, indent=4))
	print(json.dumps(result_vegan, indent=4))

	pool = multiprocessing.Pool(4)
	result_multiprocess = pool.map(
		extract,
		list_of_attendees
	)
	
	print(json.dumps(result_multiprocess, indent=4))