"""
  -> Date: 15-September-2019

  -> Purpose:
  thin_film calculates the thickness of a thin film assuming it's deposited on
  silicon. The simplistic UI allows the user to manange a database of films.
  The data are stored in a csv file, films.csv, in the same directory as
  thin_film.py.

  -> authors: Patrick O'Hara, Nicholas Lenz
  -> version: 1.0
"""

# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from math import sqrt
import csv

class Thin_film(object):
    """
    Class for the Thin_film object
    """
    def __init__(self, name='SiO2', spectral_range=0.0, index=0.0,
        number_of_maxima=0.0):
        """
        Constructs an instance of the Thin_film class
            Args
                self
                name : material of the film
                spectral_range : range over which the film was measured in nm
                index : refractive index of the film
                number_of_maxima : number of maxima measured
            Returns
                None
        """
        self.name = name
        self.spectral_range = spectral_range
        self.index = index
        self.number_of_maxima = number_of_maxima


    def __str__(self):
        """
        Provides casting of a thin_film object to a string
            Args
                self
            Returns
                (str) name,spectral_range,index,number_of_maxima
        """
        out = ''
        out += self.name
        out += ',' + str(self.spectral_range)
        out += ',' + str(self.index)
        out += ',' + str(self.number_of_maxima)
        return out

    def Get_spectral_range(self):
        """
        GET_SPECTRAL_RANGE
            Returns the spectral range of the Thin_film (measured instance)
        Args
            self
        Returns
            (float) spectral_range
        """
        return self.spectral_range


    def Get_index(self):
        """
        GET_INDEX
        Args
            self
        Returns
            (float) index of the Thin_film
        """
        return self.index


    def Get_number_of_maxima(self):
        """
        GET_NUMBER_OF_MAXIMA
        Args
            self
        Returns
            (int) number_of_maxima measured for the Thin_film
        """
        return self.number_of_maxima


    def Get_thickness(self):
        """
        GET_THICKNESS
        Args
            self
        Returns
            (float) thickness of the Thin_film
        """
        return (self.number_of_maxima * self.spectral_range \
                * sqrt(self.index**2-1)) / 2.0

    def Write(self):
        """
        WRITE
            Overwrites the instance variables of Thin_film based on user input
            for each instance variable.
        Args
            self
        Returns
            None
        """
        self.name = input('Enter the name of the film: ')
        self.index= float(input('Enter the refractive index of the film: '))
        self.spectral_range = float(input('Enter the spectral bandwidth over which' \
                                    + ' the spectra was acquired in nm: '))
        self.number_of_maxima = int(input('Enter the number of maxima within the' \
                                    +  ' spectral range: '))


    def Display(self):
        """
        DISPLAY
            Prints the given Thin_film to the console.
        Args
            self
        Returns
            None
        """
        print('Material width: {}\n \
              Index: {}\n \
              Number of Maxima: {}\n \
              Thickness: {}\n ')


def Read(material_string):
    """
    READ
        Creates an instance of Thin_film from a passed string
    Args
        material_string : name,spectral_range,index,number_of_maxima
    Returns
        (Thin_film)
    """
    properties = material_string.split(',')
    return Thin_film(*properties)


def List_films(material_list):
    """
    LIST_FILMS
        Prints all the thin films in the database to the console
    Args
        material_list : python list of Thin_films
    Returns
        None
    """
    if not material_list:
        print('The material list is empty.')
    else:
        print('\n{:<3}|{:<15}|{:<15}|{:<15}|{:<15}'.format('#',
                                                           'Composition',
                                                           'Spectral Range',
                                                           'Index',
                                                           'Number of Maxima'))
        print(68*'-')
        for idx,material in enumerate(material_list):
            print('{:<3}|{:<15}|{:<15}|{:<15}|{:<15}'.format(idx,
                                                             material.name,
                                                             material.spectral_range,
                                                             material.index,
                                                             material.number_of_maxima))

def Add_film(material_list):
    """
    ADD_FILM
        Adds a Thin_film to the database
    Args
        material_list : python list of Thin_films
    Returns
        None
    """
    material = Thin_film()
    material.Write()
    material_list.append(material)


def Delete_film(material_list):
    pass

def Get_film_Index(material_list):
    pass

def Load_data(material_list, filename):
    """
    LOAD_DATA
        Adds thin films from filename.csv to material_list
    Args
        material_list : python list of Thin_films
        filename : name of csv file to load data from
    """
    with open(filename) as reader:
        lines = reader.read().splitlines()
        for line in lines:
            fields = line.split(',')
            material_list.append(Thin_film(fields[0], \
                                           float(fields[1]), \
                                           float(fields[2]), \
                                           int(fields[3])))

def Calculate_thickness(material_list):
    """
    CALCULATE_THICKNESS
        Calculates the thickness of a file chosen from the database
    Args
        material_list : python list of Thin_films
    Returns
        (float) thickness of the thin film
    """
    print()
    List_films(material_list)
    print()
    chosen_idx = int(input('film #\n>> '))
    thickness = material_list[chosen_idx].Get_thickness()
    print(str(thickness) + ' nm')
    return thickness

def Edit_film(material_list):
    """
    EDIT_FILM
        Edits a given film from the database.
    Args
        material_list : python list of Thin_films
    Returns
        None
    """
    print()
    List_films(material_list)
    print()
    chosen_idx = int(input('film #\n>> '))
    material_list[chosen_idx].Write()

def Remove_film(material_list):
    """
    REMOVE_FILM
        Removes a given thin_film from the database
    Args
        material_list : python list of Thin_films
    Returns
        None
    """
    print()
    List_films(material_list)
    print()
    chosen_idx = int(input('film #\n>> '))
    del material_list[chosen_idx]

def Save_data(material_list, filename):
    pass

if __name__ == "__main__":
    material_list = []
    option_range = [i for i in range(1,9)]

    print('\n' \
            + '        T   H   I   N   F   I   L   M    /\n' \
            + '      --*---*---*---*---*---*---*---*---/\n' \
            + '       / \ / \ / \ / \ / \ / \ / \ / \ / \n' \
            + '      /---*---*---*---*---*---*---*---*--\n' \
            + '     /     C  A  L  C  U  L  A  T  O  R')

    choice = -1
    while (choice is not option_range[-1]):
        print('\n' \
              + 'Please choose one of the following: \n' \
                '(1) Add Material\n' \
                '(2) Edit Materal\n' \
                '(3) Delete Material\n' \
                '(4) List Materials\n' \
                '(5) Calculate Thickness \n' \
                '(6) Load Data\n' \
                '(7) Export Data\n' \
                '(8) Exit\n' \
              )
        while choice not in option_range:
            choice = int(input('>> '))
            if choice not in option_range:
                print('PLEASE CHOOSE A VALID OPTION!!!')

        if choice == 1:
            Add_film(material_list)
        elif choice == 2:
            Edit_film(material_list)
        elif choice == 3:
            Remove_film(material_list)
        elif choice == 4:
            List_films(material_list)
        elif choice == 5:
            Calculate_thickness(material_list)
        elif choice == 6:
            Load_data(material_list, 'film.csv')
        elif choice == 7:
            pass
        else:
            print('Goodbye!')
            break
        choice = -1
