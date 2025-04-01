#!/usr/bin/env python3

from app import app
from models import db, Plant

def seed_plants():
    with app.app_context():
        print("🚀 Starting database seeding...")
        
        # Clear existing data
        print("🧹 Clearing old data...")
        Plant.query.delete()
        
        # Plant data list
        plants_data = [
            {
                "id": 1,
                "name": "Aloe",
                "image": "./images/aloe.jpg",
                "price": 11.50,
                "is_in_stock": True
            },
            {
                "id": 2, 
                "name": "ZZ Plant",
                "image": "./images/zz-plant.jpg",
                "price": 25.98,
                "is_in_stock": False
            },
            {
                "id": 3,
                "name": "Snake Plant",
                "image": "./images/snake-plant.jpg",
                "price": 18.75,
                "is_in_stock": True
            }
        ]

        # Create plant objects
        plants = [Plant(**data) for data in plants_data]
        
        # Add to session and commit
        db.session.add_all(plants)
        db