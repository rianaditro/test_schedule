## Getting Started

To get started with this project, you have two options to set up the environment and install the dependencies: using **`uv`** (recommended for full environment management) or using **`requirements.txt`** for a more traditional setup with `pip`.

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- **Python 3.10+**
- **pip** (Python package installer)
- **Git** (for cloning the repository)
- **UV** (if you prefer using UV for environment management) – [Installation Instructions](https://github.com/pyuv/uv)

### Option 1: Using `uv` (Recommended)

If you prefer to use **UV** to manage the environment and dependencies (as I have done), follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. **Install dependencies using `uv`**:
   UV will automatically create a virtual environment and install the necessary dependencies as specified in the `pyproject.toml` and `uv.lock` files.
   ```bash
   uv install
   ```

3. **Activate the virtual environment**:
   After installation, you can activate the virtual environment:
   ```bash
   uv activate
   ```

4. **Run the project**:
   You can now run the project (e.g., using Uvicorn for FastAPI projects):
   ```bash
   python3 main.py
   ```

### Option 2: Using `requirements.txt` (Manual Setup with `pip`)

If you prefer not to use **UV**, you can manually set up the virtual environment and install the dependencies using **pip**.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. **Create and activate a virtual environment**:
   If you're using **venv**, create and activate a virtual environment:

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   Use **pip** to install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project**:
   You can now run the project (e.g., using Uvicorn for FastAPI projects):
   ```bash
   python3 main.py
   ```

### Additional Notes

- **Using `uv`**: This is the preferred method, as it handles the environment setup automatically, including managing exact versions of dependencies via the `uv.lock` file.
- **Using `pip` with `requirements.txt`**: This is a more traditional setup if you prefer using **pip** for dependency management and don't want to use **UV**.