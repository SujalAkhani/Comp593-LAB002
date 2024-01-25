def main():  #defining main function
    script_values = {
        'full_name': 'Sujal Akhani', #abiut myself
        'student_id': 10314176, #student id 
        'pizza_toppings': ['ONIONS', 'GREEN PEPPER', 'PANEER'], #topping name
        'movies': [
            {
                'title': 'Animal', #movie name1
                'genre': 'Action' #type
            },
            {
                'title': 'Dhammal', #movie name 2
                'genre': 'comedy' #type
            }
        ]
    }

    script_values['movies'].append({'title': 'Chello Divas', 'genre': 'Comedy'}) #movie name 3
    
    student_info(script_values)
    pizza_toppings(script_values)
    print()
    pizza_toppings(script_values, ('OLIVES', 'TOMATOES')) #topppings
    print()
    pizza_toppings(script_values)
    print()
    m_genres(script_values)
    m_titles(script_values['movies'])
    
def student_info(data):
    full_name = data['full_name']
    first_name = full_name.split()[0]
    student_id = data['student_id']
    
    print(f"My name is {full_name}, but you can call me {first_name} Buddy.")
    print(f"My student ID is {student_id}.")
    print()
    
def pizza_toppings(data, toppings):
    data['pizza_toppings'].extend(toppings)
    data['pizza_toppings'].sort()
    data['pizza_toppings'] = [topping.lower() for topping in data['pizza_toppings']]
    
def pizza_toppings(data):
    print("My favorite pizza toppings are:")
    for topping in data['pizza_toppings']:
      print(f"- {topping}")
     
#m_genre = movie genre
def m_genres(data):
        genres = [movie['genre'] for movie in data['movies']]
        print("I like to watch", end=" ")
        for i, genre in enumerate(genres):
            if i == len(genres) - 1:
                print(f"and {genre}", end=" ")
            else:
                print(f"{genre},", end=" ")
        print("movies.")
    
#m_titles = title of the movie
def m_titles(movie_list):
        titles = [movie['title'].title() for movie in movie_list]
        print("Some of my favorite movies are", end=" ")
        for i, title in enumerate(titles):
            if i == len(titles) - 1:
                print(f"and {title}!")
            else:
                print(f"{title},", end=" ")
    

if __name__ == "__main__":
    main()
#end of script


# There is a minor problem in my script but i am not able to find out it beacause of that my only half script is running
    