# Passport Reader Evervault Cage Demo

This demo showcases an Evervault Cage that securely reads and extracts data from passport images in order to determine passport validity using the passporteye library. It was created as part of a team effort for Evervault Developer Days.

## Prerequisites

* Python 3.8+
* Evervault CLI ([https://docs.evervault.com/cli](https://docs.evervault.com/cli))

## Setup

### 1. Clone Repository

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

### 2. Create Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Requirements

Install necessary Python packages:

```bash
pip install -r requirements.txt
```

### 4. Prepare Passport Image

Add your sample passport image as `passport.jpg` in the project's root directory.

```
project-root/
├── passport.jpg
├── app.py
├── cage/
└── requirements.txt
```

## Running Locally

To test the passport reader locally:

```bash
python server.py
```

## Deploying the Evervault Cage

Log in to Evervault CLI:

```bash
evervault login
```

Deploy the cage:

```bash
evervault cages deploy cage
```

Verify deployment:

```bash
evervault cages list
```

## Using the Cage

Once deployed, securely call your cage API to extract passport details from images securely within the Cage so that the data can't be intercepted or accessed.

## Support

Refer to the [Evervault documentation](https://docs.evervault.com/) for additional guidance.
