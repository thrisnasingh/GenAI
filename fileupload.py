import boto3
from PIL import Image
import io
import csv
from playground import generate_image_from_model

# Create a Boto3 S3 client
s3 = boto3.client('s3')

# Define your bucket name
bucket_name = 'genaihackathon2'

# Read and write data from CSV file
csv_file = 'National_Park.csv'  # Replace 'Beach.csv' with your actual CSV file name
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    # fieldnames = reader.fieldnames + ['image_url']  # Add 'image_url' as a new field
    # writer = csv.DictWriter(file, fieldnames=fieldnames)
    for row in reader:
        if 'Name' in row:
            # Get your prompt
            if 'Description' in row:
                # Get prompt for each row
                prompt = row['Description']
                # Remove any quotes from the prompt
                prompt = prompt.replace("", '')
                # Generate your image here or load it from somewhere
                image = generate_image_from_model(prompt)
                image.save("generated_image.jpg")

                # Convert the image to bytes
                image_bytes = io.BytesIO()
                image.save(image_bytes, format='JPEG')
                image_bytes.seek(0)

                # Replace 'generated_image.jpg' with the value from the CSV file
                key = row['Name']

                # Upload the image to S3
                s3.upload_fileobj(image_bytes, bucket_name, key)
                print(f"Image uploaded to S3 bucket: {bucket_name} with key: {key}")

                # # Construct URL of the uploaded image
                # image_url = f"https://{bucket_name}.s3.us-east-2.amazonaws.com/{key}"
                # row['Image'] = image_url  # Add the image URL to the row

                # # Update the current row in the CSV file
                # writer.writerow(row['Image'])
                # print(f"Image URL added to the CSV file: {image_url}")

