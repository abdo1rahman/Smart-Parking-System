# """ 
# TODO: Generate sample data in Madinaty and perform ML algorithms (Gradient Descent) on it to predict where parking will be availble within 6 hours from request
# """
# import csv
# import random
# from datetime import datetime, timedelta, timezone

# def generate_csv_data(num_spots=30, file_path="data/parking_data.csv"):
#     # Ensure reproducibility (optional)
#     random.seed()

#     # Prepare data
#     data = []

#     for i in range(1, num_spots + 1):
#         spot_id = f'MAD-{i:03d}'  # e.g., MAD-001
#         lat = round(random.uniform(30.060, 30.080), 6)
#         lon = round(random.uniform(31.635, 31.655), 6)
#         status = random.choices(['available', 'occupied'], weights=[0.6, 0.4])[0]
#         timestamp = (datetime.now(timezone.utc) - timedelta(minutes=random.randint(1, 60))).strftime('%Y-%m-%d %H:%M:%S')

#         data.append([spot_id, lat, lon, status, timestamp])

#     # Write to CSV
#     with open(file_path, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['spot_id', 'latitude', 'longitude', 'status', 'timestamp'])  # Header
#         writer.writerows(data)

#     print(f"🚗 CSV dataset for Madinaty generated and saved to {file_path}.")

# # Generate and save
# generate_csv_data(30)
