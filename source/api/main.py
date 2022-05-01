"""
Creator: Ivanovitch Silva
Date: 17 April 2022
Create API
"""

from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import panda as pd
import joblib
import os
import wandb
import sys
from source.api.pipeline import FeatureSelector, CategoricalTransformer, NumericalTransformer

