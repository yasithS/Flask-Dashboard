import csv
from application import app, db
from application.models import IncomeExpenses
from datetime import datetime

def import_from_csv(csv_file_path):
    with app.app_context():
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            print("columns:", csv_reader.fieldnames)
            
            for row in csv_reader:
                # Convert date string to datetime
                date_obj = datetime.strptime(row['date'], '%Y-%m-%d')
                
                # Create a new record
                record = IncomeExpenses(
                    type=row['type'],
                    category=row['category'],
                    date=date_obj,
                    amount=float(row['amount'])
                )
                
                # Add to session
                db.session.add(record)
            
            # Commit all records
            db.session.commit()
            print("Data imported successfully!")

if __name__ == "__main__":
    csv_file = "application/data/expenses.csv"  
    import_from_csv(csv_file)