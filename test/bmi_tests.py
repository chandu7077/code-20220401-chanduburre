from bmi import calculate_BMI
from bmi import calculate_BMI_category_and_health_risk
from bmi import get_total_number_of_overweight_people
from bmi import get_total_number_of_overweight_people_by_gender

def test_calculate_BMI():
    data = [[175,75],[180,90],[177,67]]
    expected_results = [24.49,27.78,21.39]
    for i in range(0,len(data)):
        result = calculate_BMI(data[i][0],data[i][1])
        assert result == expected_results[i]

def test_calculate_BMI_category_and_health_risk():
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    expected_results = ["Moderately Obese","Overweight"]
    result = calculate_BMI_category_and_health_risk(data)
    assert result.loc[0,"BMI Category"] == expected_results[0]
    assert result.loc[1, "BMI Category"] == expected_results[1]

def test_get_total_number_of_overweight_people():
    test_file = "test/test_data.json"
    expected_result = 1
    result = get_total_number_of_overweight_people(test_file)
    assert expected_result == result

def test_get_total_number_of_overweight_people_by_gender():
    test_file = "test/test_data.json"
    expected_result = [0,1]
    result = get_total_number_of_overweight_people_by_gender(test_file,"Male")
    assert expected_result[0] == result
    result = get_total_number_of_overweight_people_by_gender(test_file, "Female")
    assert expected_result[1] == result