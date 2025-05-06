### 🖥️ Running the Project locally

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On MacOS/Linux:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 🚀 Running the Project with Docker

To build and run the project inside a Docker container, use one of the following commands:

#### ⚒️⚙️ Build and Run

```bash
docker-compose up --build
```

Rebuilds the Docker image (required if you've changed the Dockerfile, requirements.txt, or source code).
Then starts the container.

#### ⚙️ Run without Rebuilding

```bash
docker-compose up
```

Starts the most recently built image without rebuilding it.
Any changes to files will not be reflected.
