{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dc5bc763-9a3f-4798-8953-8c8ce29dff3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4ecfff6e-d483-4696-81e5-e413865f5a05",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "943c8928-17b7-4e8e-ad5e-56d4421608cf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "stp_venv",
   "language": "python",
   "name": "stp_venv"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
