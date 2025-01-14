import os
import requests
from bs4 import BeautifulSoup

# Crie a pasta para salvar as imagens
output_folder = "cat_images"
os.makedirs(output_folder, exist_ok=True)

# URL de pesquisa do Google (ou outra fonte de imagens)
url = "https://unsplash.com/s/photos/cats"

# Faça a requisição para a página
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Encontre as imagens na página
images = soup.find_all("img")
count = 0

# Faça o download das imagens
for img in images:
    img_url = img.get("src")
    if img_url and "http" in img_url:
        try:
            img_data = requests.get(img_url).content
            with open(f"{output_folder}/cat_{count}.jpg", "wb") as handler:
                handler.write(img_data)
                print(f"Imagem {count} salva com sucesso!")
                count += 1
            if count >= 100:  # Limite de 100 imagens
                break
        except Exception as e:
            print(f"Erro ao baixar {img_url}: {e}")
