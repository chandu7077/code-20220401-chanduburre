### NAME
    bmi.py

### DESCRIPTION
    This module contains functions for calculating the BMI (Body Mass Index) of 
	each person, BMI Category and Health Risk associated with each BMI Category.

### FUNCTIONS

######load_json_data(filename)
    - Reads the file and returns JSON Object
		
######calculate_BMI(height_in_CM, weight_in_KG)
    - Calculated Body Mass Index based on height and weight
		
######calculate_BMI_category_and_health_risk(data)
    - Accepts list of key-value pairs which contain persons data and
      returns dataframe with BMI Category and Health Risk calculated for each person
  
######get_total_number_of_overweight_people(filename)
    - Accepts the filename and returns total number of overweight people

### OBSERVATIONS
    - TOTAL NUMBER OF OVERWEIGHT PEOPLE is 1
    - TOTAL NUMBER OF OVERWEIGHT PEOPLE WHO ARE MALE is 0
    - TOTAL NUMBER OF OVERWEIGHT PEOPLE WHO ARE FEMALE is 1




