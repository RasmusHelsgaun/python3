import numpy as np

# 2. exercise
def get_copenhagen_population_data_array():
    filename = './befkbhalderstatkode.csv'
    return np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

#3. exercise
english_speaking_countries = [5170,5309, 5502, 5303, 5305,5526, 5314, 5326,5339, 5308,5142,
5352, 5514, 5625, 5347, 5311, 5374,5390]

def get_amount_english_and_nonenglish(year=2015):
    cph_pop = get_copenhagen_population_data_array()
    #extracts all data from the given year
    year_data = cph_pop[cph_pop[:,0] == year]
    
    english_mask = np.in1d(year_data[:,3], english_speaking_countries)
    nonenglish_mask = np.in1d(year_data[:,3], english_speaking_countries, invert=True)
    
    english = np.sum(year_data[english_mask][:,4])
    nonenglish = np.sum(year_data[nonenglish_mask][:,4])
    
    return english, nonenglish

#4. exercise
def filtered_data(data, mask):
    return data[mask]

#5. exercise
def accumulated_value(data, datapicker): 
    return np.sum(data[:,datapicker.value])

#9. exercise
def get_age_population_of_age_in_area(data, max_age, area, datapicker, year=2015):
    age_population = []
    labels = []
    
    for age in range(0, max_age + 1, 10):
        if age == max_age:
            break
        mask = ((data[:,2] >= age) & 
                (data[:,2] <= age + 10) & 
                (data[:,1] == area) & 
                (data[:,0] == year))
        filtered = filtered_data(data, mask)
        if len(filtered) != 0:
            labels.append(str(age) + " - " + str(age + 10))
            acc = accumulated_value(filtered, datapicker.POPULATION)
            age_population.append(acc)
    return age_population, labels