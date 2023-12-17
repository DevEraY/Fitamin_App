import pandas as pd

# Load data
deneme_df = pd.read_csv('deneme.csv')
food_nutrients_df = pd.read_csv('food_nutrientt.csv')
nutrient_df = pd.read_csv('nutrientt.csv')
food_portion_df = pd.read_csv('food_portionn.csv')
measure_unit_df = pd.read_csv('measure_unitt.csv')

# Merge food_nutrients_df with nutrient_df to get nutrient names and units
merged_nutrient_df = pd.merge(food_nutrients_df, nutrient_df, left_on='nutrient_id', right_on='id')

# Merge deneme_df with merged_nutrient_df on fdc_id using a left join
result_df = pd.merge(deneme_df, merged_nutrient_df, left_on='fdc_id', right_on='fdc_id', how='left')

# Group by food and nutrient name to sum the amounts
grouped_df = result_df.groupby(['description', 'name', 'unit_name', 'fdc_id'])['amount'].sum().reset_index()

# Merge with food portion data
food_portion_edited_df = food_portion_df.merge(measure_unit_df, on="measure_unit_id", how="left")
selected_columns = ["fdc_id", "measure_unit_id", "portion_name", "portion_amount", "gram_weight"]
food_portion_final_df = food_portion_edited_df[selected_columns]

# Merge with the grouped data
# Merge with food portion data using a left join
final_df = pd.merge(grouped_df, food_portion_final_df, left_on='fdc_id', right_on='fdc_id', how='left')
# Sort the final DataFrame by 'description'
final_df_sorted = final_df.sort_values(by='description')

# Save to CSV
final_df_sorted.to_csv('food_information_per_description_sorted.csv', index=False)
