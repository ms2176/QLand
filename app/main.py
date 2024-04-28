from desertification_analyzer import DesertificationAnalyzer
from qaoa_jobscheduler import QAOAJobScheduler


def get_user_input():
    """Prompts the user to enter values for the following:
    country, nvdi_data, lst_data, model

    Returns:
        tuple: the user-set values (country, nvdi_data, lst_data, model_selections)
    """
    country = input("Please provide the country for desertification analysis: ")
    nvdi_data = input("Please provide the NDVI data for desertification analysis: ")
    lst_data = input("Please provide the LST data for desertification analysis: ")
    models_available = [
        "Random Forest",
        "Gradient Boosted Trees",
        "Support Vector Machines",
        "CNN",
    ]

    print("Choose models (separated by commas):")
    for index, model in enumerate(models_available, 1):
        print(f"{index}. {model}")

    models_indices = input("Enter the numbers of the models you choose: ")

    # Convert indices to int and subtract 1 to match list indices
    model_selections = [
        models_available[int(index.strip()) - 1] for index in models_indices.split(",")
    ]
    return country, nvdi_data, lst_data, model_selections


def main(args:list=None):
    """Calls the analyzer model to get estimated resources, then passes it to the scheduler to get the execution schedule over multiple machines"""
    if args is None:
        args = get_user_input()
    country, nvdi_data, lst_data, model_selections = args

    data = {
        "country": country,
        "nvdi_data": nvdi_data,
        "lst_data": lst_data,
        "models": model_selections,
    }
    analyzer = DesertificationAnalyzer(data)
    resources = analyzer.estimate_resources()

    # Pass the estimated resources to the QAOAJobScheduler
    scheduler = QAOAJobScheduler(resources)
    result = scheduler.run()

    # depending on the result run on the available GPU
    # or run on the available CPU
    print(result)


if __name__ == "__main__":
    main()
