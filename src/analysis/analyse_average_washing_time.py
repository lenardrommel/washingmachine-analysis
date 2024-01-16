from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from tueplots.constants.color import rgb

csv_name = "../../data/anonymized.csv"
plots_path = "../../plots/"
indices = {"weekday" : 0, "day" : 1, "month" : 2, "year" : 3, "start_time" : 4, "end_time" : 5, "duration" : 6, "pseudonym" : 7, "sex" : 8, "machine": 9}
months = {"DEC" : 12, "JAN" : 1, "FEB" : 2, "MAR": 3, "APR": 4, "MAI": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OKT": 10, "NOV": 11, "DEZ":12}
data = []

def readInData():
    with open(csv_name) as fr:
        head = fr.readline()
        for line in fr:
            row = line.strip().split(",")
            data.append(row)

def printNumberOfIndividuals():
    nbr_individual_females_excluding_cleaning_lady = 0
    nbr_individual_males = 0
    nbr_individuals_undefined = 0
    names_already_seen = {"Putzfrau"}
    for entry in data:
        name = entry[indices["pseudonym"]]
        sex = entry[indices["sex"]]
        if name not in names_already_seen:
            names_already_seen.add(name)
            if sex == "f":
                nbr_individual_females_excluding_cleaning_lady +=1
            elif sex == "m":
                nbr_individual_males +=1
            elif sex == "u":
                nbr_individuals_undefined +=1

    print("Females:", nbr_individual_females_excluding_cleaning_lady)
    print("Males:", nbr_individual_males)
    print("Undefined", nbr_individuals_undefined)
    print()

def get_for_each_individual_first_and_last_date_in_dataset_and_total_nbr_of_washing_time():
    # {name: [first_date, last_date, total_washing_hours, sex]}
    map_individual_to_information = dict()
    for entry in data:
        name = entry[indices["pseudonym"]]
        day = int(entry[indices["day"]])
        month = months[entry[indices["month"]]]
        year = int(entry[indices["year"]])
        washing_hours = float(entry[indices["duration"]])
        sex = entry[indices["sex"]]
        date = datetime(year, month, day)
        if name not in map_individual_to_information:
            map_individual_to_information[name] = [date, date, washing_hours, sex]
        else:
            map_individual_to_information[name][1] = date
            map_individual_to_information[name][2] += washing_hours

    return map_individual_to_information

def get_average_washing_hours_per_week_for_females_and_males():
    females_average_hours_per_week = dict()
    males_average_hours_per_week = dict()
    individuals_information = get_for_each_individual_first_and_last_date_in_dataset_and_total_nbr_of_washing_time()

    # exclude cleaning lady
    individuals_information.pop("Putzfrau")

    for individual in individuals_information:
        data = individuals_information[individual]
        first_date = data[0]
        last_date = data[1]
        total_washing_hours = data[2]
        sex = data[3]

        # skip undefined data entries
        if sex != "f" and sex != "m":
            continue

        difference_dates = last_date - first_date
        total_nbr_days = difference_dates.days

        # skip if individual has only washed once:
        if total_nbr_days == 0:
            print("Skipping",individual, "due to appearing only once")
            continue

        weeks = total_nbr_days / 7
        hours_per_week = total_washing_hours / weeks

        if sex == "f":
            females_average_hours_per_week[individual] = hours_per_week
        else:
            males_average_hours_per_week[individual] = hours_per_week

    print()
    return females_average_hours_per_week, males_average_hours_per_week


def remove_outliers(dictionary, threshold):
    keys_to_remove = set()
    for key in dictionary:
        if dictionary[key] >= threshold:
            keys_to_remove.add(key)

    for key in keys_to_remove:
        print("Removing outlier", key)
        dictionary.pop(key)

    print()


def plot_female_and_male_washing_frequency(female_avg_hrs, male_avg_hrs):
    nbr_fml = len(female_avg_hrs)
    nbr_ml = len(male_avg_hrs)

    fig, ax = plt.subplots()
    ax.set_title("Washing Machine Usage Frequency")
    ax.set_xlabel("avg. hours per week")

    mean_female = np.mean(female_avg_hrs)
    mean_male = np.mean(male_avg_hrs)
    std_female = np.std(female_avg_hrs)
    std_male = np.std(male_avg_hrs)
    print("Mean f/m:", mean_female,mean_male)
    print("Std. f/m", std_female, std_male)

    # get some random values for y-axis
    np.random.seed(2)
    u_m = np.random.rand(nbr_ml)
    u_f = np.random.rand(nbr_fml)
    ax.plot(
        female_avg_hrs, 1 + 0.5 * u_f, "o", label=f"{nbr_fml} female students", color=rgb.tue_red, alpha=0.5, mec="none", ms=4
    )

    ax.plot(
        male_avg_hrs,  0.5 * u_m, "o", label=f"{nbr_ml} male students", color=rgb.tue_blue, alpha=0.5, mec="none", ms=4
    )

    # 1,125 / 0.375
    ax.errorbar(mean_female, 1.25, xerr=std_female, capsize=5, color=rgb.tue_red, alpha=0.3, elinewidth=1.1, label=f"std. female:    {std_female:.2f}")
    ax.errorbar(mean_male, 0.25, xerr=std_male, capsize=5, color=rgb.tue_blue,alpha=0.3, elinewidth=1.1, label=f"std. male:       {std_male:.2f}")


    ax.axhline(0.75, color=rgb.tue_dark, alpha=0.5)
    ax.yaxis.set_visible(False)
    ax.axvline(mean_female, 0.5, 1, color = rgb.tue_red, alpha = 1, label = f"mean female: {mean_female:.2f}")
    ax.axvline(mean_male, 0, 0.49, color=rgb.tue_blue, alpha=1, label = f"mean male:    {mean_male:.2f}")
    ax.legend(loc='center right', framealpha=1.0, facecolor='white', edgecolor='black')
    fig.savefig(plots_path + "AverageWashingHours.pdf")
    fig.savefig(plots_path + "AverageWashingHours.png")



def permutation_test(female_avg_hrs, male_avg_hrs, operation, num_permutations = 10000):
    np.random.seed(2)

    combined_data = np.concatenate([female_avg_hrs, male_avg_hrs])
    observed_diff = operation(male_avg_hrs, female_avg_hrs)

    # difference in each permutation (initialized with 0s)
    permuted_diffs = np.zeros(num_permutations)

    for i in range(num_permutations):
        # randomly permutate data
        permuted_data = np.random.permutation(combined_data)

        randomly_assigned_males = permuted_data[:len(male_avg_hrs)]
        randomly_assigned_females = permuted_data[len(male_avg_hrs):]

        permuted_diffs[i] = operation(randomly_assigned_males, randomly_assigned_females)

    # percentage of permutations at least as extreme as observed
    # TODO: Ask whether to use absolute values!
    p_value = np.sum(np.abs(permuted_diffs) >= np.abs(observed_diff))/num_permutations
    return p_value



def mean_difference(group1, group2):
    return np.mean(group1) - np.mean(group2)

def std_difference(group1, group2):
    return np.std(group1) - np.std(group2)

def print_min_max(fml_avg, male_avg):
    min_f = round(np.min(fml_avg), 2)
    max_f = round(np.max(fml_avg), 2)
    min_m = round(np.min(male_avg), 2)
    max_m = round(np.max(male_avg), 2)
    print("Female: min:", min_f, time_in_minutes(min_f), "max:", max_f, time_in_minutes(max_f))
    print("Male: Min:", min_m, time_in_minutes(min_m), "Max:", max_m, time_in_minutes(max_m))


def time_in_minutes(hours):
    return "(" + str(hours*60) +")"
def analyse_washing_frequency():
    readInData()
    printNumberOfIndividuals()
    fml_averg, male_averg = get_average_washing_hours_per_week_for_females_and_males()

    # remove outliers
    remove_outliers(fml_averg, 10)
    remove_outliers(male_averg, 10)

    female_pseudonyms = fml_averg.keys()
    female_avg_hrs = np.array(list(fml_averg.values()))
    male_pseudonyms = male_averg.keys()
    male_avg_hrs = np.array(list(male_averg.values()))
    plot_female_and_male_washing_frequency(female_avg_hrs, male_avg_hrs)
    p_value_mean_difference = permutation_test(female_avg_hrs, male_avg_hrs, mean_difference)
    print("p-value mean difference:", p_value_mean_difference)
    p_value_std_difference = permutation_test(female_avg_hrs, male_avg_hrs, std_difference)
    print("p-value std difference", p_value_std_difference)
    print_min_max(female_avg_hrs, male_avg_hrs)


analyse_washing_frequency()




