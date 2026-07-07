{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c0137c0d-15ed-48e0-a3ea-b2616d3eb0ba",
   "metadata": {},
   "source": [
    "def hours():\n",
    "    print(\"Open 9-5 daily\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85f1d47d-87cd-42d5-b425-ee358ef3c5c0",
   "metadata": {},
   "source": [
    "## 11.1\n",
    "\n",
    "Create a file called `zoo.py` with a function named `hours()` that prints the zoo's hours. Import the module and call the function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a953b267-3f61-4a64-99fb-c25ba0e1677c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Open 9-5 daily\n"
     ]
    }
   ],
   "source": [
    "import importlib\n",
    "import zoo\n",
    "\n",
    "importlib.reload(zoo)\n",
    "\n",
    "zoo.hours()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c401526-5d52-4b33-bf89-c9435fcaf682",
   "metadata": {},
   "source": [
    "## 11.2\n",
    "\n",
    "Import the `zoo` module as `menagerie` and call its `hours()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c23b77b7-0b21-4aec-8ec1-561ac93ec12f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Open 9-5 daily\n"
     ]
    }
   ],
   "source": [
    "import zoo as menagerie\n",
    "\n",
    "menagerie.hours()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64ee4e26-935f-4b66-a5c9-ce9cc1e2f120",
   "metadata": {},
   "source": [
    "## 16.4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "68a41d93-d992-42a2-82e7-562191d946e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "books.db and books table created.\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "conn = sqlite3.connect(\"books.db\")\n",
    "cursor = conn.cursor()\n",
    "\n",
    "cursor.execute(\"\"\"\n",
    "CREATE TABLE IF NOT EXISTS books (\n",
    "    title TEXT,\n",
    "    author TEXT,\n",
    "    year INTEGER\n",
    ")\n",
    "\"\"\")\n",
    "\n",
    "conn.commit()\n",
    "\n",
    "print(\"books.db and books table created.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f50b6ae-02e9-4a39-9121-fe7ec009c696",
   "metadata": {},
   "source": [
    "## 16.5\n",
    "\n",
    "Read `books2.csv` and insert its data into the `books` table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a9e8bd9d-fa9e-4184-a781-65955ccdd0bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "books2.csv created.\n"
     ]
    }
   ],
   "source": [
    "csv_text = \"\"\"title,author,year\n",
    "The Weirdstone of Brisingamen,Alan Garner,1960\n",
    "Perdido Street Station,China Miéville,2000\n",
    "Thud!,Terry Pratchett,2005\n",
    "The Spellman Files,Lisa Lutz,2007\n",
    "Small Gods,Terry Pratchett,1992\n",
    "\"\"\"\n",
    "\n",
    "with open(\"books2.csv\", \"w\", encoding=\"utf-8\") as file:\n",
    "    file.write(csv_text)\n",
    "\n",
    "print(\"books2.csv created.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b333b0ff-15b7-47eb-a024-c1c4490db612",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data inserted into books table.\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import sqlite3\n",
    "\n",
    "conn = sqlite3.connect(\"books.db\")\n",
    "cursor = conn.cursor()\n",
    "\n",
    "with open(\"books2.csv\", \"r\", encoding=\"utf-8\") as file:\n",
    "    books = csv.DictReader(file)\n",
    "\n",
    "    for book in books:\n",
    "        cursor.execute(\n",
    "            \"INSERT INTO books (title, author, year) VALUES (?, ?, ?)\",\n",
    "            (book[\"title\"], book[\"author\"], int(book[\"year\"]))\n",
    "        )\n",
    "\n",
    "conn.commit()\n",
    "conn.close()\n",
    "\n",
    "print(\"Data inserted into books table.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41f9aa3c-b444-412c-a156-6c31be6a6ad4",
   "metadata": {},
   "source": [
    "## 16.8\n",
    "\n",
    "Use SQLAlchemy to connect to the `books.db` database and select the book titles in alphabetical order."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4493ebb0-f2a4-4075-a20e-9ce28f9b5f8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Perdido Street Station\n",
      "Small Gods\n",
      "The Spellman Files\n",
      "The Weirdstone of Brisingamen\n",
      "Thud!\n"
     ]
    }
   ],
   "source": [
    "from sqlalchemy import create_engine, text\n",
    "\n",
    "# Connect to the SQLite database\n",
    "engine = create_engine(\"sqlite:///books.db\")\n",
    "\n",
    "# Display the book titles in alphabetical order\n",
    "with engine.connect() as connection:\n",
    "    result = connection.execute(\n",
    "        text(\"SELECT title FROM books ORDER BY title\")\n",
    "    )\n",
    "\n",
    "    for row in result:\n",
    "        print(row[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60a00592-cff1-4842-8382-40559b0af768",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
