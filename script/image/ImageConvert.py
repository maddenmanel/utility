import base64
import json
import requests

def encode_image_to_base64(image_file_path):
    """Convert the image to a Base64 encoded string."""
    with open(image_file_path, "rb") as image_file:
        image_data = image_file.read()
    return base64.b64encode(image_data).decode('utf-8')

def recognize_vehicle_image(com_code, request_id, image_file_path, api_url):
    """Send a request to the image recognition API."""
    
    # Convert the image to Base64
    image_data = encode_image_to_base64(image_file_path)
    
    # Create the InlinedImage object
    inlined_image = {
        "id": "imageId",  # You can generate a unique ID if needed
        "name": image_file_path.split("\\")[-1],  # Extract image name from file path
        "data": image_data
    }
    
    # Prepare the payload
    payload = [inlined_image]
    
    # Headers for the request
    headers = {
        "Content-Type": "application/json"
    }
    
    # Send the POST request to the API
    response = requests.post(
        api_url,
        headers=headers,
        data=json.dumps(payload)
    )
    
    # Check the response
    if response.status_code == 200:
        return response.json()  # Assuming the response is a JSON object
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Example usage
if __name__ == "__main__":
    # Define your variables
    com_code = "ZSIC"  # Your com-code
    request_id = "661l8e1725496943565_002_013"  # Your request-id
    image_file_path = r"D:\project\utility\script\image\2.JPG"  # Path to the image
    api_url = ""  # API URL

    # Prepare the URL with query parameters
    full_url = f"{api_url}?com-code={com_code}&correlation-id={request_id}"
    
    # Call the method to send the request
    response = recognize_vehicle_image(com_code, request_id, image_file_path, full_url)
    
    # Print the response
    print(response)
