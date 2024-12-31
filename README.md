
# BrainTumorSegmentationUsingOpenCV

This repository implements a Convolutional Neural Network (CNN) to analyze MRI scans and determine whether a brain tumor is present. The project is designed to function as a backend system, providing the necessary infrastructure to train and deploy the model.

---

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system
- A stable internet connection to download the dataset and dependencies

---

### Steps to Set Up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Cleveridiot07/BrainTumorClassificationUsingOpenCV
   cd BrainTumorClassificationUsingOpenCV
   ```

2. **Initialize a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

### Dataset

1. **Download the dataset**:
   - [Brain Tumor Classification Dataset](https://drive.google.com/file/d/1Yu6tPxNmS9JKxBk9KldewiTXCEiCQGl8/view?usp=drive_link)

2. **Unzip the dataset**:
   - After downloading, unzip the dataset:
     - On Windows: Right-click the file and select **Extract All...**.
     - On macOS/Linux: Use the command:
       ```bash
       unzip datasets.zip
       ```

3. **Place the dataset**:
   - After unzipping, place the dataset in the following directory structure:
     ```
     backend/
     ├── model/
     │   ├── maintrain.py
     │   └── <dataset-folder>
     ```

---

### Train the Model

1. Navigate to the `model/` directory:
   ```bash
   cd model
   ```

2. Run the training script:
   ```bash
   python maintrain.py
   ```

3. After training, the `.h5` file for the model will be generated automatically in the `model/` directory.

---

### Running the Project

1. Return to the `backend` directory:
   ```bash
   cd ..
   ```

2. Start the backend:
   ```bash
   uvicorn main:app --reload
   ```

   - This will run the backend at `http://127.0.0.1:8000`.
   - You can proceed to `http://127.0.0.1:8000/docs` to test the app using the interactive API documentation provided by Swagger UI.
   - Press `CTRL+C` to stop the server.

---

## Contribution
Feel free to fork the repository, create a branch, and submit a pull request to contribute to the project.

