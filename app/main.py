from desertification_analyzer  import DesertificationAnalyzer
from qaoa_jobscheduler import QAOAJobScheduler

def get_user_input():
    country = input("Please provide the country for desertification analysis: ")
    nvdi_data = input("Please provide the NDVI data for desertification analysis: ")
    lst_data = input("Please provide the LST data for desertification analysis: ")
    models_available = ["Random Forest", "Gradient Boosted Trees", "Support Vector Machines", "CNN"]
    print("Choose models (separated by commas):")
    for index, model in enumerate(models_available, 1):
        print(f"{index}. {model}")
    
    models_indices = input("Enter the numbers of the models you choose: ")
    # Convert indices to int and subtract 1 to match list indices
    model_selections = [models_available[int(index.strip()) - 1] for index in models_indices.split(',')]
    return country, nvdi_data, lst_data, model_selections

def main():
    country, nvdi_data, lst_data, model_selections = get_user_input()
    data = {
        'country': country,
        'nvdi_data': nvdi_data,
        'lst_data': lst_data,
        'models': model_selections
    }
    analyzer = DesertificationAnalyzer(data)
    # Pass the analyzer object to the QAOAJobScheduler
    scheduler = QAOAJobScheduler(analyzer)
    result = scheduler.run()
    # depending on the result run on the available GPU
    # or run on the available CPU
    if result == 'GPU':
        print("Running on GPU")
        
    else:
        print("Running on CPU")
    print(result)


