{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "from joblib import load\n",
    "import pandas as pd\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "modelo = load('modelo_b0rjen.joblib')\n",
    "\n",
    "@app.post(\"/predict\")\n",
    "async def predict(tiempo: int):\n",
    "    # Estamos suponiendo que \"tiempo\" es el número secuencial que necesita el modelo para la predicción\n",
    "    df = pd.DataFrame({'tiempo': [tiempo]})\n",
    "    predicción = modelo.predict(df)\n",
    "    return {\"predicción\": predicción[0]}"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
