import matplotlib.pyplot as plt

# Function to get sales data from the user
def get_sales_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = []

    for month in months:
        try:
            sale = float(input(f"Enter total sales for {month}: "))
            sales.append(sale)
        except ValueError:
            print("Invalid input. Please enter a valid sales amount.")

    return months, sales

# Main function to create the graph
def create_sales_graph(months, sales):
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales)
    plt.title("Total Sales ($) per Month")
    plt.xlabel("Months")
    plt.ylabel("Total Sales ($)")
    plt.show()

if __name__ == "__main__":
    months, sales = get_sales_data()
    create_sales_graph(months, sales)
