# VoiceDraw

![Görsel1](https://github.com/user-attachments/assets/27051b29-fd55-4fb5-8c26-994b5f574c59)

![Adsız tasarım (1)](https://github.com/user-attachments/assets/2157b14e-cd9a-4ae2-914f-0ddbb077be7f)

TR

Bu projede, mikrofon ile alınan ses kaydı kullanılarak (Ses kaydı türkçe olarak alınmaktadır) görsel üretme işlevi gerçekleştirilmiştir. Projede, görsel üretimi için OpenAI'nın DALL-E 3 modeli kullanılmıştır. Ayrıca, ses dosyasını metne dönüştürmek için OpenAI'nın Whisper-1 modeli kullanılmıştır. Prompt engineering ilkeleri doğrultusunda, Google'ın Gemini Pro Vision modeli kullanılarak zenginleştirilmiş prompt'lar üretilmiş ve bu sayede DALL·E 3 modelinin ürettiği görüntülerin kalitesi artırılmıştır.Son olarak "Son Görseli Kullan" seçeneği ile multi-modality moduna geçilip son üretilen görsel ve zenginleştirilmiş metin girdi olarak verilip bu girdiler doğrultusunda yeni bir görsel üretimi gerçekleştirilmiştir. Arayüz tasarımı için Streamlit kullanılmıştır. Bu proje, uçtan uca bir Generative AI projesi olup, prompt engineering konularını da kapsamaktadır.

NOT: OpenAI ve Google sunucularında model çıkarımı (inference) yapmak için token bazında ücretli API anahtarları (API keys) gerekmektedir. Bu projede, API anahtarları ücretli olarak alınmamıştır. Bu nedenle, görseller temsilidir. Çıktılar aynıdır; ancak yapılması gereken tek şey API anahtarı satın almaktır. Diğer tüm kodlar aynıdır.

EN

In this project, an image generation function was performed using audio recordings taken with a microphone (the recordings are in Turkish). The OpenAI DALL-E 3 model was used for generating images. Additionally, the OpenAI Whisper-1 model was used to convert the audio file to text. Enriched prompts were created using Google's Gemini Pro Vision model following prompt engineering principles, improving the quality of images produced by DALL·E 3. Finally, with the "Use Last Image" option, the multi-modality mode was activated, where the last generated image and enriched text were given as input to create a new image based on these inputs. Streamlit was used for the interface design. This project is an end-to-end Generative AI project and also includes prompt engineering topics

NOTE: To perform model inference on OpenAI and Google servers, paid API keys are required on a token basis. In this project, the API keys were not purchased. Therefore, the images are representative. The outputs are the same; the only thing needed is to purchase an API key. All other code remains the same.

