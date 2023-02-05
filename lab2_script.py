def main():

    # DO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Tirth Sonani',
        'student_id': '10288130',
        'pizza_toppings': [
                'RED ONIONS',
                'GREEN PAPER',
                'MASHROOMS'   
        ],
        'movie':[{
        
            'title':'avenger:end game',
            'genre':'action'
            
        },
        {
            'title':'drishyam',
            'genre':'thriller'

        }

        ]
        
            }
    
    # DO: Step 3 - Add another movie to the data structure          

    about_me['movie'].append({'title':'criminal justice','genre':'drama'})
  
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me,('corn','paneer'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

    return
     
#DO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(name_id):
    
    first_name='Tirth Sonani'.split(" ")[0]
    
    
    print(f"My name is {name_id['full_name']},but you can call me Mr {first_name}. ")
    print(f"My student ID is {name_id['student_id']}.")

    return
    
# DO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    for i,t in  enumerate (about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = t.lower()
    about_me['pizza_toppings'].sort()





# DO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f"My favourite pizza toppings are:")

    for t in  about_me['pizza_toppings']:
        print(f'-{t}')

   



    return

# DO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print(f"I like to watch",end=' ')
    
    #for m in about_me['movie']:
    movie_genre=[m['genre'] for m in about_me['movie']]
    print(','.join(movie_genre),end='.\n')
    return 

# DO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):

    
    
    print(f"Some of my favourite movies are", end=' ')

    movie=[m['title'].title() for m in movie_list['movie']]

    print(', '.join(movie),end='!\n')

    
    
if __name__ == '__main__':
    main()