import requests

SERVER_URL = "http://192.168.0.14:5000/get_content"
DEVICE_ID = "device_001"  # може да е hostname или серийния номер на Pi-то

def get_content():
    try:
        response = requests.post(SERVER_URL, json={"device_id": DEVICE_ID})
        if response.status_code == 200:
            content = response.json()
            print(f"Получено съдържание: {content}")
            # Тук ще добавим логика за показване на съдържание
        else:
            print("Няма съдържание или грешка:", response.text)
    except Exception as e:
        print("Грешка при връзка със сървъра:", e)

if __name__ == "__main__":
    get_content()
