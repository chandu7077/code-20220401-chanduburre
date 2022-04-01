
import json
import pandas as pd

def load_json_data(filename):
    """ Reads the file and returns JSON Object
    :param filename: str
        (filename of person's data)
    :return: list
        (The list of key-pairs containing person's data)
    """
    file_reader = open(filename,"r")
    data = json.load(file_reader)
    return data

def calculate_BMI(height_in_CM, weight_in_KG):
    """ Calculated Body Mass Index based on height and weight

    :param height_in_CM: int
        (height of a person in CM)
    :param weight_in_KG: int
        (weight of a person in KG)
    :return: float
        (BMI (Body Mass Index))
    """
    height_in_M = height_in_CM / 100
    BMI = round(weight_in_KG / height_in_M**2,2)
    return BMI

def calculate_BMI_category_and_health_risk(data):
    """ Accepts list of key-value pairs which contain persons data and
        returns dataframe with BMI Category and Health Risk calculated for
        each person

    :param data: list
        (list of key-value pairs containing data of each person)
    :return: dataframe
        (pandas dataframe containing BMI category and Health Risk for each person)
    """
    data_frame = pd.DataFrame(data,columns=["Gender","HeightCm","WeightKg"])
    data_frame["BMI"] = calculate_BMI(data_frame.HeightCm,data_frame.WeightKg)
    data_frame.loc[data_frame.BMI <= 18.4,
                   ["BMI Category", "BMI Range (kg/m2)", "Health Risk"]] = ["Underweight", "18.4 and below",
                                                                            "Malnutrition risk"]

    data_frame.loc[(data_frame.BMI >= 18.5) & (data_frame.BMI <=24.9),
                   ["BMI Category","BMI Range (kg/m2)","Health Risk"]] = ["Normal weight","18.5 - 24.9","Low risk"]

    data_frame.loc[(data_frame.BMI >= 25) & (data_frame.BMI <= 29.9),
                   ["BMI Category", "BMI Range (kg/m2)", "Health Risk"]] = ["Overweight", "25 - 29.9",
                                                                            "Enhanced risk"]

    data_frame.loc[(data_frame.BMI >= 30) & (data_frame.BMI <= 34.9),
                   ["BMI Category", "BMI Range (kg/m2)", "Health Risk"]] = ["Moderately Obese", "30 - 34.9",
                                                                            "Medium risk"]

    data_frame.loc[(data_frame.BMI >= 35) & (data_frame.BMI <= 39.9),
                   ["BMI Category", "BMI Range (kg/m2)", "Health Risk"]] = ["Severely Obese", "35 - 39.9",
                                                                            "High risk"]

    data_frame.loc[data_frame.BMI >= 40,
                   ["BMI Category", "BMI Range (kg/m2)", "Health Risk"]] = ["Very Severely Obese", "40 and above",
                                                                            "Very High risk"]
    del data_frame["BMI"]
    return data_frame

def get_total_number_of_overweight_people(filename):
    """ Accepts the filename and returns total number of overweight people

    :param filename: str
        (The filename where data of the people is present in JSON format)
    :return: int
        (Total number of overweight people)
    """
    data = load_json_data(filename)
    bmi_data = calculate_BMI_category_and_health_risk(data)
    overweight_people = bmi_data[(bmi_data["BMI Category"] == 'Overweight')]
    return len(overweight_people)

def get_total_number_of_overweight_people_by_gender(filename,gender="Male"):
    """ Accepts the filename and returns total number of overweight people

    :param filename: str
        (The filename where data of the people is present in JSON format)
    :return: int
        (Total number of overweight people)
    """
    data = load_json_data(filename)
    bmi_data = calculate_BMI_category_and_health_risk(data)
    overweight_people_by_gender = bmi_data[(bmi_data["BMI Category"] == 'Overweight') & (bmi_data["Gender"] == gender)]
    return len(overweight_people_by_gender)

if __name__ == '__main__':
    print("TOTAL NUMBER OF OVERWEIGHT PEOPLE:",end=":")
    print(get_total_number_of_overweight_people("data/data.json"))
    print("TOTAL NUMBER OF OVERWEIGHT PEOPLE WHO ARE MALE:", end=":")
    print(get_total_number_of_overweight_people_by_gender("data/data.json",gender="Male"))
    print("TOTAL NUMBER OF OVERWEIGHT PEOPLE WHO ARE FEMALE:", end=":")
    print(get_total_number_of_overweight_people_by_gender("data/data.json", gender="Female"))
