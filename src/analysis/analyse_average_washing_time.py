import numpy as np
import matplotlib.pyplot as plt
from tueplots.constants.color import rgb
from tueplots import bundles
import pandas as pd

data_path = "../../data/"
csv_name = data_path + "anonymized.csv"
plots_path = "../../plots/"

months = {"DEC": 12, "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAI": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9,
          "OKT": 10, "NOV": 11, "DEZ": 12}

df = pd.read_csv(csv_name)
df = df.replace({'month': months})
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
#plt.rcParams.update(bundles.icml2022(usetex=False))
plt.rcParams["font.family"] = "Times New Roman"


def print_number_of_individual_females_males_and_undefined():
    result = df[df['pseudonym'] != "Putzfrau"].groupby('sex')['pseudonym'].nunique()
    result = result.rename({'f': 'female:', 'm': 'male:', 'u': 'undefined:'})
    print(result)
    print()


def create_data_for_individuals():
    df_individual = df.groupby('pseudonym').agg(
        sex=('sex', 'first'),
        total_duration=('duration(in h)', 'sum'),
        first_date=('date', 'first'),
        last_date=('date', 'last'),
        nbr_washing_instances=('pseudonym', 'size')
    )
    df_individual['active_time_in_weeks'] = (df_individual['last_date'] - df_individual['first_date']).dt.days / 7
    df_individual['avg_times_per_week'] = (
                df_individual['nbr_washing_instances'] / df_individual['active_time_in_weeks'])
    df_individual['avg_hours_per_week'] = (df_individual['total_duration'] / df_individual['active_time_in_weeks'])
    df_individual.to_csv(data_path + 'processed_data.csv', index=True)

    df_individual_female = df_individual[df_individual['sex'] == 'f']
    df_individual_male = df_individual[df_individual['sex'] == 'm']
    return df_individual_female, df_individual_male


def plot_avg_washing_time(female_avg_hrs, male_avg_hrs):
    nbr_fml = len(female_avg_hrs)
    nbr_ml = len(male_avg_hrs)

    fig, ax = plt.subplots()
    ax.set_title("Washing Machine Utilization Rate")
    ax.set_xlabel("hours per week")

    mean_female = np.mean(female_avg_hrs)
    mean_male = np.mean(male_avg_hrs)
    std_female = np.std(female_avg_hrs)
    std_male = np.std(male_avg_hrs)
    print("Mean f/m:", mean_female, mean_male)
    print("Std. f/m", std_female, std_male)
    print()

    # get some random values for y-axis
    np.random.seed(12)
    u_m = np.random.rand(nbr_ml)
    u_f = np.random.rand(nbr_fml)
    ax.plot(
        female_avg_hrs, 1 + 0.5 * u_f, "o", label=f"{nbr_fml} female students", color=rgb.tue_red, alpha=0.5,
        mec="none", ms=4
    )

    ax.plot(
        male_avg_hrs, 0.5 * u_m, "o", label=f"{nbr_ml} male students", color=rgb.tue_blue, alpha=0.5, mec="none", ms=4
    )

    # 1,125 / 0.375
    ax.errorbar(mean_female, 1.25, xerr=std_female, capsize=5, color=rgb.tue_red, alpha=0.3, elinewidth=1.1,
                label=f"std. female:    {std_female:.2f}")
    ax.errorbar(mean_male, 0.25, xerr=std_male, capsize=5, color=rgb.tue_blue, alpha=0.3, elinewidth=1.1,
                label=f"std. male:       {std_male:.2f}")

    ax.axhline(0.75, color=rgb.tue_dark, alpha=0.5)
    ax.yaxis.set_visible(False)
    ax.axvline(mean_female, 0.51, 1, color=rgb.tue_red, alpha=1, label=f"mean female: {mean_female:.2f}")
    ax.axvline(mean_male, 0, 0.5, color=rgb.tue_blue, alpha=1, label=f"mean male:    {mean_male:.2f}")
    ax.legend(loc='center right', framealpha=1.0, facecolor='white', edgecolor='black')
    fig.savefig(plots_path + "WashingMachineUtilizationRate.pdf")
    fig.savefig(plots_path + "WashingMachineUtilizationRate.png")


def plot_avg_washing_time_against_total_active_time(female_avg_hrs, male_avg_hrs, female_nbr_washing_instances,
                                                    male_nbr_washing_instances):
    nbr_fml = len(female_avg_hrs)
    nbr_ml = len(male_avg_hrs)

    fig, ax = plt.subplots()
    ax.set_title("Washing Machine Utilization Rate")
    ax.set_xlabel("hours per week")
    ax.set_ylabel("active time (in weeks)")

    mean_female = np.mean(female_avg_hrs)
    mean_male = np.mean(male_avg_hrs)
    std_female = np.std(female_avg_hrs)
    std_male = np.std(male_avg_hrs)

    distance_to_line = 10

    ax.plot(
        female_avg_hrs, 60 + 1 * distance_to_line + female_nbr_washing_instances, "o", label=f"{nbr_fml} females",
        color=rgb.tue_red, alpha=0.5,
        mec="none", ms=4
    )

    ax.plot(
        male_avg_hrs, male_nbr_washing_instances, "o", label=f"{nbr_ml} males", color=rgb.tue_blue, alpha=0.5,
        mec="none", ms=4
    )

    # 1,125 / 0.375
    ax.errorbar(mean_female, 60 + 52 / 2 + distance_to_line, xerr=std_female, capsize=5, color=rgb.tue_red, alpha=0.3,
                elinewidth=1.1,
                label=f"std. female:    {std_female:.2f}")
    ax.errorbar(mean_male, 52 / 2, xerr=std_male, capsize=5, color=rgb.tue_blue, alpha=0.3, elinewidth=1.1,
                label=f"std. male:       {std_male:.2f}")

    ax.axhline(60 + distance_to_line, color=rgb.tue_dark, alpha=0.5)
    ax.yaxis.set_visible(True)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 120 + 2 * distance_to_line)
    ticks = [10, 20, 30, 40, 52, 60 + 10 + 1 * distance_to_line, 60 + 20 + 1 * distance_to_line,
             60 + 30 + 1 * distance_to_line, 60 + 40 + 1 * distance_to_line, 60 + 52 + 1 * distance_to_line]
    labels = [10, 20, 30, 40, 52, 10, 20, 30, 40, 52]
    ax.set_yticks(ticks, labels)

    x_values_grid = np.arange(0, 3.25, 0.25)
    labels_x = [0, "", 0.5, "", 1.0, "", 1.5, "", 2.0, "", 2.5, "", 3.0]
    ax.set_xticks(x_values_grid, labels_x)
    ax.grid(True, linestyle=':')

    ax.axvline(mean_female, 0.5, 1, color=rgb.tue_red, alpha=1, label=f"mean female: {mean_female:.2f}")
    ax.axvline(mean_male, 0, 0.5, color=rgb.tue_blue, alpha=1, label=f"mean male:    {mean_male:.2f}")
    ax.legend(loc='upper right')
    fig.savefig(plots_path + "WashingMachineUtilizationRate_activeTime.pdf")
    fig.savefig(plots_path + "WashingMachineUtilizationRate_activeTime.png")


def plot_comparison_of_avg_washing_time(fml_avg_hrs, ml_avg_hrs):
    fig, ax = plt.subplots()
    ax.set_title("Comparison of Washing Machine Utilization Rate")
    ax.set_xlabel("hours per week")
    ax.set_ylabel("percentage")
    nbr_females = len(fml_avg_hrs)
    nbr_males = len(ml_avg_hrs)
    categories = ['0-0.25', '0.25-0.5', '0.5-0.75', '0.75-1.0',
                  '1.0-1.25', '1.25-1.5', '1.5-1.75', '1.75-2.0',
                  '2.0-2.25', '2.25-2.5', '2.5-2.75']

    values_females = []
    values_males = []

    lower_bounds = np.arange(0, 2.75, 0.25)

    for lower_bound in lower_bounds:
        upper_bound = lower_bound + 0.25
        nbr_females_in_range = len(fml_avg_hrs[np.logical_and(fml_avg_hrs >= lower_bound, fml_avg_hrs < upper_bound)])
        nbr_males_in_range = len(ml_avg_hrs[np.logical_and(ml_avg_hrs >= lower_bound, ml_avg_hrs < upper_bound)])
        values_females.append(nbr_females_in_range / nbr_females)
        values_males.append(nbr_males_in_range / nbr_males)

    ax.bar(categories, values_females, color=rgb.tue_red, alpha=0.25, label="female")
    ax.bar(categories, values_males, color=rgb.tue_blue, alpha=0.25, label="male")
    ax.tick_params(axis='x', labelsize=8, rotation=50)
    #ax.tick_params(axis='x', rotation=50)
    ax.legend(loc='upper right')

    plt.tight_layout()

    fig.savefig(plots_path + "Comparison_Utilization_Rate.pdf")
    fig.savefig(plots_path + "Comparison_Utilization_Rate.png")


def permutation_test(female_avg_hrs, male_avg_hrs, operation, num_permutations=10000):
    np.random.seed(1)

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
    p_value = np.sum(np.abs(permuted_diffs) >= np.abs(observed_diff)) / num_permutations
    return p_value


def mean_difference(group1, group2):
    return np.mean(group1) - np.mean(group2)


def std_difference(group1, group2):
    return np.std(group1) - np.std(group2)


def print_min_and_max_active_times(df_female, df_male):
    print("Active time min/max:")
    print("female:", df_female['active_time_in_weeks'].min(), df_female['active_time_in_weeks'].max())
    print("male:", df_male['active_time_in_weeks'].min(), df_male['active_time_in_weeks'].max())
    print()


if __name__ == "__main__":
    # get general overview
    print_number_of_individual_females_males_and_undefined()

    # process data in df
    df_individual_females, df_individual_males = create_data_for_individuals()

    # remove cleaning lady
    df_individual_females = df_individual_females.drop('Putzfrau')

    # remove outliers
    threshold = 10
    df_individual_females = df_individual_females[
        (df_individual_females['active_time_in_weeks'] > 0) & (df_individual_females['avg_hours_per_week'] < threshold)]
    df_individual_males = df_individual_males[
        (df_individual_males['active_time_in_weeks'] > 0) & (df_individual_males['avg_hours_per_week'] < threshold)]

    print_min_and_max_active_times(df_individual_females, df_individual_males)

    avg_hours_per_week_female = np.array(df_individual_females['avg_hours_per_week'])
    avg_hours_per_week_male = np.array(df_individual_males['avg_hours_per_week'])
    active_time_in_weeks_female = np.array(df_individual_females['active_time_in_weeks'])
    active_time_in_weeks_male = np.array(df_individual_males['active_time_in_weeks'])

    # create plots
    plot_avg_washing_time(avg_hours_per_week_female, avg_hours_per_week_male)
    plot_avg_washing_time_against_total_active_time(avg_hours_per_week_female, avg_hours_per_week_male,
                                                    active_time_in_weeks_female, active_time_in_weeks_male)
    plot_comparison_of_avg_washing_time(avg_hours_per_week_female, avg_hours_per_week_male)

    # permutation test on mean and std
    p_value_mean_difference = permutation_test(avg_hours_per_week_female, avg_hours_per_week_male, mean_difference)
    print("p-value mean difference:", p_value_mean_difference)
    p_value_std_difference = permutation_test(avg_hours_per_week_female, avg_hours_per_week_male, std_difference)
    print("p-value std difference", p_value_std_difference)
