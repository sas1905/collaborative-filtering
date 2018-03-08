from dataset_file import dataset
from euclidean_distance import pearson_correlation

def most_similar_users(person,number_of_users):
	# returns the number_of_users (similar persons) for a given specific person.
	scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]
	
	# Sort the similar persons so that highest scores person will appear at the first
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]
 
print(most_similar_users('Lisa Rose',3))
 
#print("Lisa Rose rating on Lady in the water: {}n".format(dataset['Lisa Rose']['Lady in the Water']))
#print("Michael Phillips rating on Lady in the water: {}n".format(dataset['Michael Phillips']['Lady in the Water']))
 
#print('**************Jack Matthews ratings**************')
#print(dataset['Jack Matthews'])
