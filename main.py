#import csv library
import csv


#create empty lists for the various attributes in insurance.csv
ages = []

sexes = []

bmis = []

num_children = []

smoker_statuses = []

regions = []

insurance_charges = []


#function to load csv data
def load_list_data(lst, csv_file, column_name):
    #open csv file
    with open(csv_file) as csv_info:
        # read the data from csv file
        csv_dict = csv.DictReader(csv_info)
        #iterate through the data in each row of the csv
        for row in csv_dict:
            #add data from each row to a list
            lst.append(row[column_name])
        #return the list
        return lst
    
#load the data from insurance.csv
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


class PatientsInfo:
    #init method
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    #method that calculates the average ages of the patients in insurance.csv
    def analyze_ages(self):
        #initialize total age at zero
        total_age = 0

        #iterate through all ages in the ages list
        for age in self.patients_ages:

            total_age += int(age)
        # return total age divided by the length of the patient list
        return("Average patient age: " + str(round(total_age/len(self.patients_ages), 2)) + " years")
    
    # method that calculates the number of males and females in insurance.csv
    def analyze_sexes(self):

        females = 0
        
        males = 0

        for sex in self.patients_sexes:

            if sex == "female":
                females += 1
            
            elif sex == "male":

                males += 1
            
        print("Count for female: " + str(females))
        print("Count for male: " + str(males))

    # method to find each unique region patients are from
    def unique_regions(self):
        # initialize empty list
        unique_regions = []
        # iterate through each region in regions list
        for region in self.patients_regions:
            # if the region is not already in the unique regions list
            # then add it to the unique regions list
            if region not in unique_regions: 
                unique_regions.append(region)
        # return unique regions list
        return unique_regions
    
    def average_charges(self):

        total_charges = 0

        for charge in self.patients_charges:
            total_charges += float(charge)

        return("Average Yearly Medical Insurance Charges: " + str(round(total_charges/len(self.patients_charges), 2)) + " dollars.")
    
    # method to create dictionary with all patients information
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary 


patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

print(patient_info.analyze_ages())

print(patient_info.analyze_sexes())

print(patient_info.average_charges())

patients_dictionary = patient_info.create_dictionary()






