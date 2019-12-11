import requests
from bs4 import BeautifulSoup

#List of sites that contain NJIT classes
sites = ["https://next.catalog.njit.edu/undergraduate/computing-sciences/#coursestext","https://next.catalog.njit.edu/undergraduate/architecture-design/#coursestext","https://next.catalog.njit.edu/undergraduate/science-liberal-arts/#coursestext","https://next.catalog.njit.edu/undergraduate/newark-college-engineering/#coursestext","https://next.catalog.njit.edu/undergraduate/management/#coursestext"]

#Takes input from user to find which classes are prerequisites for other NJIT classes
givenClass = input("Enter the name of a class that you wish to find which classes are prerequisites/corequisites to that class(Case Sensitive, ex. \"CS 100\"):")
givenHrefClass = givenClass.replace(" ","\xa0")


def searchClassDatabase(site,givenClass,givenHrefClass):
    #Searchs a single website for classes that need the given class as a prereq

    #Parses website data
    result = requests.get(site)
    src = result.content
    soup = BeautifulSoup(src, features="html.parser")
    #Separates parsed data into 2 lists, class titles, and class descriptions
    classTitle = soup.findAll("p", "courseblocktitle")
    classDesc = soup.findAll("p", "courseblockdesc")
    iteration = 0

    def printClassTitle(iterate):
        # Formats the class title given the iteration of the for loop, and prints it
        step1 = classTitle[iterate].getText().split(".")[0]
        #final = step1.split("a")[0]
        print(step1)

    #Searchs for the given class in the class description, then if it finds it it gets the name of the class
    for desc in classDesc:
        desc = desc.getText()
        if givenClass in desc:
            printClassTitle(iteration)
        if givenHrefClass in desc:
            printClassTitle(iteration)
        iteration += 1


#Searchs through all NJIT colleges for classes that might have the given class as a prerequisite
for website in sites:
    searchClassDatabase(website, givenClass,givenHrefClass)
