# 🔥 AI-Oven: AI-Powered Smart Oven

![GitHub top language](https://img.shields.io/github/languages/top/tamerdn/ai-powered-oven)
![License](https://img.shields.io/github/license/tamerdn/ai-powered-oven)

This project is a web application powered by artificial intelligence that analyzes an image of uncooked food and recommends the optimal cooking temperature and duration. It's designed to take the guesswork out of cooking, ensuring perfectly cooked meals every time.

---

## 🎯 Purpose of the Project

The primary goal of this project is to automate and simplify the cooking process using computer vision and deep learning techniques. It aims to eliminate trial-and-error in the kitchen, helping users to cook their meals perfectly every single time.

## ✨ Features

* **Image Upload:** A user-friendly web interface to upload a photo of the uncooked food.
* **AI-Powered Prediction:** A deep learning model that analyzes the uploaded image to:
    * Recognize the type of food (e.g., Fish, Pizza, Steak).
    * Recommend the optimal **cooking temperature** in Celsius (°C).
    * Recommend the optimal **cooking duration** in minutes.
* **Results Display:** A clear and intuitive results screen to present the analysis outcome to the user.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Deep Learning:** TensorFlow, Keras
* **Image Processing:** OpenCV, Pillow
* **Model Architecture:** CNN + ResNet50 based multiple output regression model
* **Frontend:** HTML, CSS, JavaScript
* **Version Control:** Git, GitHub

## 🚀 Installation and Usage

To run this project on your local machine, please follow the steps below.

**1. Prerequisites:**
* Python 3.8+
* Git

**2. Clone the Repository:**
```bash
git clone [https://github.com/tamerdn/ai-powered-oven.git](https://github.com/tamerdn/ai-powered-oven.git)
cd ai-powered-oven
```
**3. Set up a Virtual Environment and Install Dependencies:**
* Create and activate a virtual environment.
* Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

**4. Download the Trained Model:**
The trained model file (`oven_model.keras`) is not included in the repository due to its large size. You can download it from the link below and place it in the project's root directory.
> **[Download Model](https://drive.google.com/file/d/1PBA6WnHDFD2hFkNfJOb4B98BT3l2MAPL/view?usp=sharing)**

**5. Run the Application:**
```bash
python app.py
```
Once the application is running, navigate to the address shown in your terminal (usually `http://127.0.0.1:5000`) in your web browser to see the project in action.

## 📂 Project Structure

```
.
├── website/                # Web interface files (HTML, CSS, JS)
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   └── templates/
│       └── index.html
├── app.py                  # Main Flask application file
├── oven_model.keras        # Trained deep learning model (needs to be downloaded)
├── requirements.txt        # Required Python libraries
├── .gitignore              # Files to be ignored by Git
└── README.md               # This file
```

## 📜 License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details.
